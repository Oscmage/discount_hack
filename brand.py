import dataclasses
import uuid


@dataclasses.dataclass
class Brand:
    id: int
    reference: uuid.UUID
