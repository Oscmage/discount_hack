import uuid

from brand import Brand


class BrandInterface:
    def get_brand(self, brand_ref) -> Brand:
        return Brand(id=1, reference=uuid.uuid4())
