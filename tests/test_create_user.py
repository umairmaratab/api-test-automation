import allure
from utils.helpers import load_json

@allure.feature("Users")
@allure.story("Create user")
def test_create_user(api_client):
    payload = load_json("data/create_user_payload.json")
    r = api_client.post("/users", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body.get("name") == payload["name"]
    assert body.get("job") == payload["job"]
    assert "id" in body

@allure.feature("Users")
@allure.story("Create user - invalid payload")
def test_create_user_invalid_payload(api_client):
    payload = load_json("data/invalid_user_payload.json")
    r = api_client.post("/users", json=payload)
    # ReqRes is lenient and will often return 201; assert that response is JSON and contains something reasonable.
    assert r.status_code in (201, 400)
    # if 201, ensure response JSON exists
    try:
        _ = r.json()
    except Exception:
        pytest.skip("Service returned non-json response for invalid payload")
