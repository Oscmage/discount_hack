import uuid
from typing import List, Optional

from batch import Batch
from batch_repo import BatchRepository
from brand import Brand
from brand_interface import BrandInterface
from code import Code
from code_repository import CodeRepository
from price_rule import PriceRule
from price_rule_interface import PriceRuleInterface


class BatchInterface:
    def __init__(self):
        self._batch_repository = BatchRepository()
        self._brand_interface = BrandInterface()
        self._price_rule_interface = PriceRuleInterface()
        self._code_repository = CodeRepository()

    def create_batch(
        self,
        number_of_codes: int,
        price_rule_ref: uuid.UUID,
        brand_ref: uuid.UUID,
    ) -> Batch:
        brand: Brand = self._brand_interface.get_brand(brand_ref=brand_ref)
        price_rule: PriceRule = self._price_rule_interface.get_price_rule(
            price_rule_ref
        )
        # TODO Make sure we only support creating one batch at a time for a brand
        batch: Batch = self._batch_repository.create_batch(
            number_of_codes=number_of_codes,
            brand_id=brand.id,
            price_rule_id=price_rule.id,
        )
        # TODO: This should be a scheduled asynchronous task
        self.create_codes_async(
            batch=batch,
            number_of_codes=number_of_codes,
        )

        return batch

    def create_codes_async(self, batch: Batch, number_of_codes: int):
        codes: List[Code] = []
        for i in range(0, number_of_codes):
            codes.append(
                Code(
                    batch_ref=batch.batch_ref,
                    price_rule_id=batch.price_rule_id,
                    code=str(uuid.uuid4()),
                )
            )

        self._batch_repository.create_codes(batch=batch, codes=codes)

    def get_available_code(
        self, user_id: uuid.UUID, batch_ref: uuid.UUID
    ) -> Optional[Code]:
        return self._batch_repository.get_available_code(
            user_id=user_id, batch_ref=batch_ref
        )
