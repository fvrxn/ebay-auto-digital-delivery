import requests
from base64 import b64encode
# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()

# Konfiguration
EBAY_CLIENTID = os.getenv("EBAY_CLIENTID")
EBAY_CLIENTSECRET = os.getenv("EBAY_CLIENTSECRET")


# Base64-Encode für Basic Auth
auth_header = b64encode(f"{EBAY_CLIENTID}:{EBAY_CLIENTSECRET}".encode()).decode()

# Token-Endpunkt
url = "https://api.ebay.com/identity/v1/oauth2/token"
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {
    "grant_type": "client_credentials",
    "scope": "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
}

response = requests.post(url, headers=headers, data=data)
if response.status_code == 200:
    access_token = response.json().get("access_token")
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code} - {response.text}")