import dataclasses
import uuid
from http import HTTPStatus

from fastapi import FastAPI

from discount.batch.batch_interface import BatchInterface
from discount.batch.batch_repo import BatchRepository
from discount.brand.brand_interface import BrandInterface
from discount.error_codes import NO_CODE_AVAILABLE_ERROR
from discount.price_rule.price_rule_interface import PriceRuleInterface
from discount.responses import (
    GetAvailableCodeSuccessResponse,
    Message,
    CreateBatchSuccessResponse,
)


def start():
    app = FastAPI()
    batch_interface = BatchInterface(
        batch_repository=BatchRepository(),
        brand_interface=BrandInterface(),
        price_rule_interface=PriceRuleInterface(),
    )

    @app.get("/ping")
    def ping():
        return {"Hello": "World"}

    @app.post(
        "/v1/create_batch/{number_of_codes}/{price_rule_ref}/{brand_ref}",
        status_code=HTTPStatus.ACCEPTED,
    )
    def create_batch(
        number_of_codes: int,
        price_rule_ref: uuid.UUID = uuid.uuid4(),
        brand_ref: uuid.UUID = uuid.uuid4(),
    ):
        batch = batch_interface.create_batch(
            number_of_codes=number_of_codes,
            price_rule_ref=price_rule_ref,
            brand_ref=brand_ref,
        )
        return dataclasses.asdict(
            CreateBatchSuccessResponse(
                batch_ref=batch.batch_ref,
                number_of_codes=batch.number_of_codes,
                price_rule_ref=price_rule_ref,
            )
        )

    @app.get(
        "/v1/retrieve_code/{batch_ref}/{user_id}",
        response_model=GetAvailableCodeSuccessResponse,
        responses={404: {"model": Message}},
    )
    def get_available_code(batch_ref: uuid.UUID, user_id: uuid.UUID):
        code = batch_interface.get_available_code(
            batch_ref=batch_ref,
            user_id=user_id,
        )
        if not code:
            return NO_CODE_AVAILABLE_ERROR

        return GetAvailableCodeSuccessResponse(code=code.code)

    return app

start()
