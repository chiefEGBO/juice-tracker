import requests
import os

BASE_URL = "http://localhost:3000"
TOKEN_FILE = "token.txt"

def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return f.read().strip()
    return None

def login(email, password):
    url = f"{BASE_URL}/rest/user/login" 

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(url, json=payload)

    try:
        data = response.json()
    except Exception:
        print("Server did not return JSON")
        print("Response text (truncated):", response.text[:300])
        return None

    if "authentication" in data:
        token = data["authentication"]["token"]
        save_token(token)
        print("Login successful!")
        return token

    print("Login failed:", data)
    return None

def get_challenges(token=None):
    url = f"{BASE_URL}/api/challenges"

    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(url, headers=headers)

    try:
        return response.json()['data']
    except Exception:
        print("Failed to get challenges. Server returned non-JSON response:")
        print(response.text[:300])
        return []
