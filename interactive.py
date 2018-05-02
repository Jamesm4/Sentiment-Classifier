import requests

BASE_URL = "http://localhost:5000/"

print("Enter sentence to classify, or enter STOP")
while True:
  text = input("Sentence: ")
  if text == "STOP":
    break
  else:
    payload = {"text": text}
    req = requests.post(BASE_URL + "sentiments", data=payload)
    print(req.json())
    print("\n")

