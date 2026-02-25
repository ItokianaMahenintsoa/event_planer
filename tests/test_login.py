import httpx
import pytest

@pytest.mark.asyncio(loop_scope="session")
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser@packt.com",
        "password": "testpassword",
        "events": []
    }
    headers={
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    test_response = {
        "message": "User created successfully"
    }

    response = await default_client.post("/user/signup", json=payload, headers=headers)
    print("Status:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert response.json() == test_response
    

@pytest.mark.asyncio(loop_scope="session")
async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser@packt.com",
        "password": "testpassword",
    } 
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = await default_client.post("/user/signin", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["token_type"].lower() == "bearer"
