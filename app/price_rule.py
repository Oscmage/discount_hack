import dataclasses
import uuid


@dataclasses.dataclass
class PriceRule:
    id: int
    reference: uuid.UUID
