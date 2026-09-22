import pytest
from fastapi.testclient import TestClient
from app import app  # Assumes your FastAPI code is in main.py

client = TestClient(app)

# List the (route, expected_json) pairs to test
@pytest.mark.parametrize("route, expected_response", [
        ("/", {"message": "Hello, World!"}),
        ("/hello", {"message": "hello , from the hello route"}),
        ("/jenkins", {"message": "hello , jenkins this side"})
        ])
def test_all_routes(route, expected_response):
        response = client.get(route)
        assert response.status_code == 200
        assert response.json() == expected_response

