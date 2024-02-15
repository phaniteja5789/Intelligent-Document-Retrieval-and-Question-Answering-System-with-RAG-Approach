
import requests

def ValidateHuggingFaceKEY(api_key):

    response = requests.get(
    "https://huggingface.co/api/whoami-v2",
    params={},
    headers={"Authorization":f"Bearer {api_key}"}
    )

    return response.status_code