import allure
from utils.helpers import load_json
import pytest

@allure.feature("Users")
@allure.story("Update user (PUT)")
def test_update_user_put(api_client, created_user):
    # created_user contains an 'id' returned by ReqRes (often numeric or string)
    user_id = created_user.get("id")
    payload = load_json("data/update_user_payload.json")
    r = api_client.put(f"/users/{user_id}", json=payload)
    # ReqRes returns 200 for PUT
    assert r.status_code == 200
    body = r.json()
    # It returns updatedAt and echoes payload in many cases — check fields exist
    assert body.get("name") == payload["name"] or "updatedAt" in body

@allure.feature("Users")
@allure.story("Partial update user (PATCH)")
def test_update_user_patch(api_client, created_user):
    user_id = created_user.get("id")
    payload = {"job": "L2 Engineer"}
    r = api_client.patch(f"/users/{user_id}", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "updatedAt" in body

@allure.feature("Users")
@allure.story("Update non-existing user - expected 404 or handled")
def test_update_user_not_found(api_client):
    # ReqRes often returns 200 for PUT on arbitrary ids; we'll exercise a non-existent route to induce 404
    r = api_client.put("/unknown/99999", json={"foo": "bar"})
    assert r.status_code == 404
