import requests

BASE_URL = "http://127.0.0.1:8000"


def test_create_user():
    query = """
    mutation {
        createUser(name: "Shikha Pandey") {
            id
            name
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    assert "data" in data
    user = data["data"]["createUser"]
    assert user["name"] == "Shikha Pandey"


def test_update_user():
    query = """
    mutation {
        updateUser(id: 1, name: "Yogesh Singh") {
            id
            name
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    assert "data" in data
    user = data["data"]["updateUser"]
    assert user["name"] == "Yogesh Singh"


def test_delete_user():
    query = """
    mutation {
        deleteUser(id: 1) {
            id
            name
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    assert "data" in data
    user = data["data"]["deleteUser"]
    assert user["name"] == "Shikha Pandey"


def test_get_all_users():
    query = """
    query {
        users {
            id
            name
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    assert "data" in data
    users = data["data"]["users"]
    print(users)
    assert len(users) > 0


def test_get_user_by_id():
    query = """
    query {
        user(id: 1) {
            id
            name
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    assert "data" in data
    user = data["data"]["user"]
    assert len(user) > 0


# Run the test cases
test_create_user()
test_update_user()
test_delete_user()
test_get_all_users()
test_get_user_by_id()
