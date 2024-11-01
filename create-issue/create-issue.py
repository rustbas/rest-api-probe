import json
import requests
from datetime import date
import os
from dotenv import load_dotenv

dotenv_path = "../.env"
if os.path.exists(dotenv_path):
	load_dotenv(dotenv_path)

GH_TOKEN = os.environ.get('GH_TOKEN')
USERNAME = os.environ.get('USERNAME')
REPO = os.environ.get('REPO')

LOGFILE="log.txt"
GITHUB_BASE_URL = 'https://api.github.com' 

FULL_URL= f"{GITHUB_BASE_URL}/repos/{USERNAME}/{REPO}/issues"

with open(LOGFILE, "r") as f:
    text = f.readlines()

today = date.today()

print(FULL_URL)
# print(GH_TOKEN)

headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GH_TOKEN}", 
        "X-GitHub-Api-Version":"2022-11-28",
}

message = {
        "title": f"Bug {today}",
        "body":f"`{text}`",
}

response = requests.post(FULL_URL, json=message, headers=headers)

# print(response.status_code)
print(response.json())
