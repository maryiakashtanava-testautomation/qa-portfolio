import pytest
import requests


API_BASE = "https://automationexercise.com/api"


@pytest.mark.api
class TestProductsAPI:

    def test_get_all_products_status_200(self):
        response = requests.get(f"{API_BASE}/productsList")
        assert response.status_code == 200

    def test_get_all_products_returns_list(self):
        response = requests.get(f"{API_BASE}/productsList")
        data = response.json()
        assert "products" in data
        assert isinstance(data["products"], list)
        assert len(data["products"]) > 0

    def test_get_all_brands_status_200(self):
        response = requests.get(f"{API_BASE}/brandsList")
        assert response.status_code == 200

    def test_get_all_brands_returns_list(self):
        response = requests.get(f"{API_BASE}/brandsList")
        data = response.json()
        assert "brands" in data
        assert isinstance(data["brands"], list)

    def test_search_product_by_name(self):
        response = requests.post(
            f"{API_BASE}/searchProduct",
            data={"search_product": "top"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "products" in data

    def test_post_to_products_list_returns_405(self):
        response = requests.post(f"{API_BASE}/productsList")
        data = response.json()
        assert data.get("responseCode") == 405
