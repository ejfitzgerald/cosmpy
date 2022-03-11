# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

import json
from datetime import datetime
from typing import Any, Optional

from cosmpy.aerial.client import LedgerClient
from cosmpy.aerial.contract.cosmwasm import (
    create_cosmwasm_execute_msg,
    create_cosmwasm_instantiate_msg,
    create_cosmwasm_store_code_msg,
)
from cosmpy.aerial.tx import SigningCfg, Transaction
from cosmpy.aerial.tx_helpers import SubmittedTx
from cosmpy.aerial.wallet import Wallet
from cosmpy.crypto.address import Address
from cosmpy.crypto.hashfuncs import sha256
from cosmpy.protos.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest
from cosmpy.protos.cosmwasm.wasm.v1.query_pb2 import (
    QueryCodesRequest,
    QuerySmartContractStateRequest,
)


def _compute_digest(path: str) -> bytes:
    with open(path, "rb") as input_file:
        return sha256(input_file.read())


def _generate_label(digest: bytes) -> str:
    now = datetime.utcnow()
    return f"{digest.hex()[:14]}-{now.strftime('%Y%m%d%H%M%S')}"


class LedgerContract:
    def __init__(
        self, path: str, client: LedgerClient, address: Optional[Address] = None
    ):
        self._path = path
        self._client = client
        self._digest = _compute_digest(self._path)
        self._code_id = self._find_contract_id_by_digest(self._digest)
        self._address = address

    @property
    def path(self) -> str:
        return self._path

    @property
    def digest(self) -> bytes:
        return self._digest

    @property
    def code_id(self) -> Optional[int]:
        return self._code_id

    @property
    def address(self) -> Optional[Address]:
        return self._address

    def store(self, sender: Wallet, gas_limit: Optional[int] = None) -> int:

        # query the account information for the sender
        account = self._client.query_account(sender.address())

        # estimate the fee required for this transaction
        gas_limit = (
            gas_limit or 2000000
        )  # TODO: Need to interface to the simulation engine
        fee = self._client.estimate_fee_from_gas(gas_limit)

        # build up the store transaction
        tx = Transaction()
        tx.add_message(create_cosmwasm_store_code_msg(self._path, sender.address()))
        tx.seal(
            SigningCfg.direct(sender.public_key(), account.sequence),
            fee=fee,
            gas_limit=gas_limit,
        )
        tx.sign(sender.signer(), self._client.network_config.chain_id, account.number)
        tx.complete()

        # broadcast the store transaction
        submitted_tx = self._client.broadcast_tx(tx).wait_to_complete()

        # extract the code id
        self._code_id = submitted_tx.contract_code_id
        if self._code_id is None:
            raise RuntimeError("Unable to extract contract code id")

        return self._code_id

    def instantiate(
        self,
        code_id: int,
        args: Any,
        sender: Wallet,
        label: Optional[str] = None,
        gas_limit: Optional[int] = None,
        admin_address: Optional[Address] = None,
        funds: Optional[str] = None,
    ) -> Address:
        # query the account information for the sender
        account = self._client.query_account(sender.address())
        label = label or _generate_label(self._digest)

        # estimate the fee required for this transaction
        gas_limit = (
            gas_limit or 2000000
        )  # TODO: Need to interface to the simulation engine
        fee = self._client.estimate_fee_from_gas(gas_limit)

        # build up the store transaction
        tx = Transaction()
        tx.add_message(
            create_cosmwasm_instantiate_msg(
                code_id,
                args,
                label,
                sender.address(),
                admin_address=admin_address,
                funds=funds,
            )
        )
        tx.seal(
            SigningCfg.direct(sender.public_key(), account.sequence),
            fee=fee,
            gas_limit=gas_limit,
        )
        tx.sign(sender.signer(), self._client.network_config.chain_id, account.number)
        tx.complete()

        # broadcast the store transaction
        submitted_tx = self._client.broadcast_tx(tx).wait_to_complete()

        # store the contract address
        self._address = submitted_tx.contract_address
        if self._address is None:
            raise RuntimeError("Unable to extract contract code id")

        return self._address

    def deploy(
        self,
        args: Any,
        sender: Wallet,
        label: Optional[str] = None,
        store_gas_limit: Optional[int] = None,
        instantiate_gas_limit: Optional[int] = None,
        admin_address: Optional[Address] = None,
        funds: Optional[str] = None,
    ) -> Address:

        # in the case where the contract is already deployed
        if self._address is not None and self._code_id is not None:
            return self._address

        assert self._address is None

        if self._code_id is None:
            self.store(sender, gas_limit=store_gas_limit)

        assert self._code_id is not None

        return self.instantiate(
            self._code_id,
            args,
            sender,
            label=label,
            gas_limit=instantiate_gas_limit,
            admin_address=admin_address,
            funds=funds,
        )

    def execute(
        self,
        args: Any,
        sender: Wallet,
        gas_limit: Optional[int] = None,
        funds: Optional[str] = None,
    ) -> SubmittedTx:
        if self._address is None:
            raise RuntimeError("Contract appears not to be deployed currently")

        # query the account information for the sender
        account = self._client.query_account(sender.address())

        # estimate the fee required for this transaction
        gas_limit = (
            gas_limit or 2000000
        )  # TODO: Need to interface to the simulation engine
        fee = self._client.estimate_fee_from_gas(gas_limit)

        # build up the store transaction
        tx = Transaction()
        tx.add_message(
            create_cosmwasm_execute_msg(
                sender.address(), self._address, args, funds=funds
            )
        )
        tx.seal(
            SigningCfg.direct(sender.public_key(), account.sequence),
            fee=fee,
            gas_limit=gas_limit,
        )
        tx.sign(sender.signer(), self._client.network_config.chain_id, account.number)
        tx.complete()

        # broadcast the store transaction
        return self._client.broadcast_tx(tx)

    def query(self, args: Any) -> Any:
        if self._address is None:
            raise RuntimeError("Contract appears not to be deployed currently")

        req = QuerySmartContractStateRequest(
            address=str(self._address), query_data=json.dumps(args).encode("UTF8")
        )
        resp = self._client.wasm.SmartContractState(req)
        return json.loads(resp.data)

    def _find_contract_id_by_digest(self, digest: bytes) -> Optional[int]:
        code_id = None

        pagination = None
        while True:
            req = QueryCodesRequest(pagination=pagination)
            resp = self._client.wasm.Codes(req)

            for code_info in resp.code_infos:
                if code_info.data_hash == digest:
                    code_id = int(code_info.code_id)
                    break

            # exit the search loop if we have successfully found our code id
            if code_id is not None:
                break

            # exit the search loop when we can't iterate any further
            if len(resp.pagination.next_key) == 0:
                break

            # proceed to the next page
            pagination = PageRequest(key=resp.pagination.next_key)

        return code_id