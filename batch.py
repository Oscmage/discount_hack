import dataclasses
import uuid
from enum import Enum


class BatchStatus(Enum):
    PROCESSING = 1
    COMPLETE = 2

@dataclasses.dataclass(frozen=True, eq=True)
class Batch:
    id: int
    number_of_codes: int
    batch_ref: uuid.UUID
    price_rule_id: int
    brand_id: int
    status: BatchStatus
