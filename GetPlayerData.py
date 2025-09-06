# CallTacticusAPI.py
# Date: 2025-09-05
# Author: Jamie
#
# Description: A simple script to call the Tacticus API and save the player data to a JSON file.
#
# Requires requests and python-dotenv packages. 
# Make sure to set your API key in a .env file with the variable name API_KEY.

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
# Environment variable needs to have API_KEY set to your API key
load_dotenv()

# Make a GET request to the API endpoint with the API key in headers
url = "https://api.tacticusgame.com/api/v1/player"
headers = {
    "accept": "application/json",
    "X-API-KEY": os.getenv("API_KEY")
}

# Perform the GET request
response = requests.get(url, headers=headers)

# Print the status code and JSON response
print(response.status_code)
print(response.json())


# Save the JSON response to a file
with open("player_data.json", "w") as file:
    json.dump(response.json(), file, indent=4)