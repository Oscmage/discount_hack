import unittest
import uuid

from code import Code


class BatchRepoTest(unittest.TestCase):
    def test_create_code(self):
        batch_ref = uuid.uuid4()
        price_rule_ref = uuid.uuid4()
        code = uuid.uuid4()
        expected_code = Code(
            batch_ref=batch_ref, price_rule_ref=price_rule_ref, code="asd"
        )
        code = self.batch_repo._create_coupon(
            batch_ref=batch_ref, rule_ref=price_rule_ref, code=code
        )
        self.assertEqual(expected_code, code)

    def test_create_batch(self):

        pass

    def test_get_code_from_batch_available(self):
        pass

    def test_get_code_from_batch_unavailable(self):
        pass
