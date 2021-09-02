import dataclasses
import uuid


@dataclasses.dataclass
class CreateBatchResponse:
    batch_ref: uuid.UUID
    number_of_codes: int
    price_rule_ref: uuid.UUID


@dataclasses.dataclass
class SuccessGetAvailableCodeResponse:
    code: str


@dataclasses.dataclass
class Message:
    message: str
