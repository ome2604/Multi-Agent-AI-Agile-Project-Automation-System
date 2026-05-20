import requests

BASE_URL = "http://127.0.0.1:8000/api"


def login(username, password):

    response = requests.post(

        f"{BASE_URL}/login",

        json={
            "username": username,
            "password": password
        }
    )

    return response.json()


def execute_workflow(goal, token):

    response = requests.post(

        f"{BASE_URL}/execute-workflow",

        json={
            "goal": goal
        },

        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    return response.json()