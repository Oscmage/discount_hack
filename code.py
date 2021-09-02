import dataclasses
import uuid
from typing import Optional


@dataclasses.dataclass
class Code:
    batch_ref: uuid.UUID
    price_rule_id: int
    code: str
    user_id: Optional[str] = None

    def to_external_response(self):
        return dict(code=self.code)
