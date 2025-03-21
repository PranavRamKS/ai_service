import requests

API_KEY = ""  # Replace with your actual API key
url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
headers = {"Authorization": f"Bearer {API_KEY}"}
# Improved prompt based on your use case
prompt = """Given the following topics and their awarded scores, suggest areas of improvement:
1. SDLC Basics (Max: 10, Awarded: 4)
2. Functions and Arguments (Max: 10, Awarded: 4)
3. OOP Concepts (Max: 15, Awarded: 7)
4. Python IDE Usage (Max: 5, Awarded: 2.5)
5. String Manipulations (Max: 5, Awarded: 1)
"""

data = {"inputs": prompt}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.json())
