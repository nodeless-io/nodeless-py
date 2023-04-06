import requests
import json

url = 'http://localhost/api/v1/paywall/9ff30e10-2949-4735-8ea3-56eb42a1306d/request'
headers = {
  'Authorization': 'Bearer {YOUR_AUTH_KEY}',
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request('POST', url, headers=headers)
response.json()