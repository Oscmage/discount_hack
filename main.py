import dataclasses
import uuid
from http import HTTPStatus

from fastapi import FastAPI

from discount.batch.batch_interface import BatchInterface
from discount.error_codes import NO_CODE_AVAILABLE_ERROR
from discount.responses import SuccessGetAvailableCodeResponse, Message, CreateBatchResponse

app = FastAPI()
batch_interface = BatchInterface()


@app.get("/ping")
def read_root():
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
        CreateBatchResponse(
            batch_ref=batch.batch_ref,
            number_of_codes=batch.number_of_codes,
            price_rule_ref=price_rule_ref,
        )
    )


@app.get(
    "/v1/retrieve_code/{batch_ref}/{user_id}",
    response_model=SuccessGetAvailableCodeResponse,
    responses={404: {"model": Message}},
)
def get_available_code(batch_ref: uuid.UUID, user_id: uuid.UUID):
    code = batch_interface.get_available_code(
        batch_ref=batch_ref,
        user_id=user_id,
    )
    if not code:
        return NO_CODE_AVAILABLE_ERROR

    return SuccessGetAvailableCodeResponse(code=code.code)
