import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "Hello chatbot!"}

response = requests.post(url, json=data)
print(response.json())
