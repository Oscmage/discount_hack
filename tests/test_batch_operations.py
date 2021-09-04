import uuid
from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestBatchOperations:
    def test_create_batch_success(self):
        number_of_codes = 100
        price_rule_ref = str(uuid.uuid4())
        brand_ref = str(uuid.uuid4())
        response = client.post(
            f"/v1/create_batch/{number_of_codes}/{price_rule_ref}/{brand_ref}"
        )
        assert response.status_code == HTTPStatus.ACCEPTED
        response_dict = response.json()
        assert response_dict.get("number_of_codes") == number_of_codes
        assert response_dict.get("price_rule_ref") == price_rule_ref
        assert response_dict.get("batch_ref"), "Expecting batch _ref"

    def test_create_batch_invalid_input(self):
        number_of_codes = "invalid_input"
        price_rule_ref = str(uuid.uuid4())
        brand_ref = str(uuid.uuid4())
        response = client.post(
            f"/v1/create_batch/{number_of_codes}/{price_rule_ref}/{brand_ref}"
        )

        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    @staticmethod
    def _create_batch() -> str:
        number_of_codes = 100
        price_rule_ref = str(uuid.uuid4())
        brand_ref = str(uuid.uuid4())
        response = client.post(
            f"/v1/create_batch/{number_of_codes}/{price_rule_ref}/{brand_ref}"
        )
        response_dict = response.json()
        return response_dict["batch_ref"]

    def test_get_available_code_success(self):
        batch_ref = self._create_batch()
        user_id = str(uuid.uuid4())

        response = client.get(f"/v1/retrieve_code/{batch_ref}/{user_id}")

        assert response.status_code == HTTPStatus.OK
        response_dict = response.json()
        assert response_dict["code"]

    def test_get_available_code_for_user_twice(self):
        batch_ref = self._create_batch()
        user_id = str(uuid.uuid4())
        response = client.get(f"/v1/retrieve_code/{batch_ref}/{user_id}")
        response_2 = client.get(f"/v1/retrieve_code/{batch_ref}/{user_id}")

        assert response.status_code == HTTPStatus.OK
        assert response_2.status_code == HTTPStatus.OK
        response_dict = response.json()
        response_dict_2 = response_2.json()
        assert response_dict["code"]
        assert response_dict_2["code"]

        assert response_dict["code"] == response_dict_2["code"]

    def test_get_available_code_non_available(self):
        batch_ref = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        response = client.get(f"/v1/retrieve_code/{batch_ref}/{user_id}")

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_get_available_code_invalid_input(self):
        batch_ref = "invalid_batch_ref"
        user_id = str(uuid.uuid4())
        response = client.get(f"/v1/retrieve_code/{batch_ref}/{user_id}")

        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
