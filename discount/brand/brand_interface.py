import uuid

from discount.brand.brand import Brand


class BrandInterface:
    def get_brand(self, brand_ref) -> Brand:
        # TODO: Implement
        return Brand(id=1, reference=uuid.uuid4())
