import requests
import json

# API endpoint (Update the URL if necessary)
URL = "http://127.0.0.1:8000/suggestions/generate/"

# Load JSON data from file
with open("reportSample.json", "r") as file:
    json_data = json.load(file)


headers = {"Content-Type": "application/json"}
response = requests.post(URL, headers=headers, json=json_data)


print("Status Code:", response.status_code)
print("Response Text:", response.text)


