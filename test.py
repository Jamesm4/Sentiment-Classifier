import requests

BASE_URL = "http://localhost:5000/"

print("Beginning test suite.\n")

# Test 1
print("Test 1")
payload = {"text": "I'm so sad so very very sad"}
req = requests.post(BASE_URL + "sentiment", data=payload)
print("Classification: " + req.text + "\n")

# Test 2
print("Test 2")
payload = {"text": "These shoes are fabulous!"}
req = requests.post(BASE_URL + "sentiments", data=payload)
print("Probabilities:")
print(req.json())
print("\n")

# Test 3
print("Test 3")
req = requests.get(BASE_URL + "accuracy")
print("Accuracy on test set: " + req.text + "\n")

