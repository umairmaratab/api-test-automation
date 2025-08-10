import allure

@allure.feature("Users")
@allure.story("List users")
def test_list_users(api_client):
    r = api_client.get("/users", params={"page": 2})
    assert r.status_code == 200
    payload = r.json()
    assert "data" in payload
    assert isinstance(payload["data"], list)
    assert len(payload["data"]) > 0

@allure.feature("Users")
@allure.story("Get single user")
def test_get_single_user(api_client):
    r = api_client.get("/users/2")
    assert r.status_code == 200
    payload = r.json()
    assert "data" in payload
    assert payload["data"]["id"] == 2

@allure.feature("Users")
@allure.story("Get single user - not found")
def test_get_user_not_found(api_client):
    r = api_client.get("/users/999999")
    assert r.status_code == 404
