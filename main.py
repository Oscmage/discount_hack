import dataclasses
import uuid
from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# TODO: remake to post
@app.get("/v1/create_batch/{number_of_codes}/{price_rule_ref}", status_code=HTTPStatus.ACCEPTED)
def create_batch(number_of_codes: int, price_rule_ref: str = ""):
    return dataclasses.asdict(
        CreateBatchResponse(
            batch_ref=uuid.uuid4(),
            number_of_codes=number_of_codes,
            price_rule_ref=uuid.UUID(price_rule_ref),
        )
    )


@dataclasses.dataclass
class CreateBatchResponse:
    batch_ref: uuid.UUID
    number_of_codes: int
    price_rule_ref: uuid.UUID
