import requests
import json
from yaml import safe_load


def get_api_from_config(config_file):
    try:
        if config_file:
            with open(config_file, "rb") as f:
                cfile = safe_load(f)
                api_key = cfile["apikey"]
                return api_key
            f.close()
    except Exception as e:
        return e


YOUR_AUTH_KEY = get_api_from_config("config.yml")
print("api key from config file: " + YOUR_AUTH_KEY)


url = "http://testnet.nodeless.io/api/v1/paywall/9ff30e10-2949-4735-8ea3-56eb42a1306d/request"
headers = {
    f"Authorization": "Bearer {YOUR_AUTH_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

response = requests.request("POST", url, headers=headers)
print(response.json())
