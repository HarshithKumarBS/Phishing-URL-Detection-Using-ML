import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "url": "http://secure-login-verify.com"
}

response = requests.post(url, json=data)

print("Response from server:")
print(response.json())
