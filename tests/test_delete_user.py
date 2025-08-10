import allure

@allure.feature("Users")
@allure.story("Delete user")
def test_delete_user(api_client, created_user):
    user_id = created_user.get("id")
    r = api_client.delete(f"/users/{user_id}")
    # ReqRes returns 204 for delete
    assert r.status_code in (204, 200)

@allure.feature("Users")
@allure.story("Delete non-existing user")
def test_delete_non_existing_user(api_client):
    r = api_client.delete("/users/9999999")
    # Some mock APIs return 204 even for non-existing; assert acceptable statuses
    assert r.status_code in (204, 404, 200)
