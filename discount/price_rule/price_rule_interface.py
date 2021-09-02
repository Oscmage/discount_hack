import uuid

from discount.price_rule.price_rule import PriceRule


class PriceRuleInterface:
    def get_price_rule(self, price_rule_ref) -> PriceRule:
        return PriceRule(id=1, reference=uuid.uuid4())
