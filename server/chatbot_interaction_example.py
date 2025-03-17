import requests

# URL of the chatbot service
CHATBOT_URL = "http://localhost:5000/chatbot"

# Sample data to send to the chatbot
data = {
    "pregunta": "What is the weather like today?",
    "product_id": 1
}

# Sending a POST request to the chatbot
response = requests.post(CHATBOT_URL, json=data)

# Print the response from the chatbot
print(response.json())
