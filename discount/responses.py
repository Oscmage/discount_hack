import dataclasses
import uuid


@dataclasses.dataclass
class CreateBatchSuccessResponse:
    batch_ref: uuid.UUID
    number_of_codes: int
    price_rule_ref: uuid.UUID


@dataclasses.dataclass
class GetAvailableCodeSuccessResponse:
    code: str


@dataclasses.dataclass
class Message:
    message: str
