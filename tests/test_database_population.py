import httpx
import pytest

list_unit = [
    {"name": "Unidade", "slug": "un"},
    {"name": "Metros", "slug": "m"},
    {"name": "Litros", "slug": "l"},
    {"name": "Metro Quadrado", "slug": "m2"},
    {"name": "Kilograma", "slug": "kg"},
]


@pytest.mark.skip("Não utilizar")
def test_insert_unit_base():
    url = "http://127.0.0.1:8000/units"
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = httpx.post(url, json=list_unit[2], headers=headers)
    assert response.status_code == 201
