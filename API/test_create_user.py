import json
import os
from utils.api_client import Base_Url


def test_create_user(api_client, headers):
    print("Base URL USED:", Base_Url)
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # # Then it goes to the payloads folder next to it
    # payload_path = os.path.join(current_dir, "payloads", "create_user.json")
    payload_path = os.path.join("API", "payloads", "create_user.json")
    with open(payload_path) as f:
        payload = json.load(f)

    response = api_client.post(
        url=f"{Base_Url}/Users",
        headers=headers,
        payload=payload
    )
    print("Base URL USED:", Base_Url)

    print("Status:", response.status_code)
    print("Headers:", response.headers)
    print("Text:", response.text)

    if "application/json" in response.headers.get("Content-Type", ""):
        print(response.json())
    else:
        print("Response is NOT JSON")



# def test_create_user(api_client,headers):
#     payload_path = os.path.join("API", "payloads", "create_user.json")
#     with open(payload_path) as f:
#         payload=json.load(f)

#     response= api_client.post(
#         url=f"{Base_Url}/users",
#         headers=headers,
#         payload=payload
#     )

#     print(response.json())
#     print("Status Code:", response.status_code)
#     print("Response Text:", response.text)


#     assert response.status_code == 201

#     assert response.json()["name"] == payload["name"]
#     assert "id" in response.json()