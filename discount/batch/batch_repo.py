import uuid
from collections import defaultdict
from typing import Optional, Dict, List, Set

from discount.batch.batch import Batch, BatchStatus
from discount.batch.code import Code


class BatchRepository:
    def __init__(self):
        self._batch_id_counter = 0
        self._used_codes_for_batch_by_user_id: Dict[
            uuid.UUID, Dict[uuid.UUID, Code]
        ] = defaultdict(dict)
        self._available_codes_for_batch: Dict[uuid.UUID, List[Code]] = {}
        self._batches: Dict[uuid.UUID, Batch] = {}
        # self._brand_batches = Dict[int, Set[Batch]] = {}

    def get_available_code(self, user_id: uuid.UUID, batch_ref) -> Optional[Code]:
        already_consumed_code = self._get_already_consumed_code(
            user_id=user_id, batch_ref=batch_ref
        )
        if already_consumed_code:
            return already_consumed_code

        codes_available_for_batch = self._available_codes_for_batch.get(batch_ref)
        if not codes_available_for_batch:
            return None

        code = codes_available_for_batch[-1]
        self._available_codes_for_batch[batch_ref] = codes_available_for_batch[:-1]
        self._used_codes_for_batch_by_user_id[batch_ref][user_id] = code

        return code

    def _get_already_consumed_code(self, user_id: uuid.UUID, batch_ref: uuid.UUID):
        used_codes_for_batch = self._used_codes_for_batch_by_user_id.get(batch_ref, {})
        user_consumed_code = used_codes_for_batch.get(user_id)
        if not user_consumed_code:
            return None

        return user_consumed_code

    def create_batch(
        self, number_of_codes: int, brand_id: int, price_rule_id: int
    ) -> Batch:
        batch_ref = uuid.uuid4()
        batch = Batch(
            id=self._get_and_increment_batch_id(),
            number_of_codes=number_of_codes,
            batch_ref=batch_ref,
            price_rule_id=price_rule_id,
            brand_id=brand_id,
            status=BatchStatus.PROCESSING,
        )
        self._batches[batch_ref] = batch
        # batches = self._brand_batches.get(brand_id)
        # if not batches:
        #     self._brand_batches[brand_id] = {batch}
        # else:
        #     batches.add(batch)

        return batch

    def _get_and_increment_batch_id(self) -> int:
        batch_id = self._batch_id_counter
        self._batch_id_counter += 1
        return batch_id

    def create_codes(self, batch: Batch, codes: List[Code]):
        self._available_codes_for_batch[batch.batch_ref] = codes
        # self._batches[batch.batch_ref].status = BatchStatus.COMPLETE
