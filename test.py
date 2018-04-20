import requests

URL = "http://localhost:5000/sentiment"

payload = {"text": "I'm so sad so very very sad"}

req = requests.post(URL, data=payload)

print(req.text)
