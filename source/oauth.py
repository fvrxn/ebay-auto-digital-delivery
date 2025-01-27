import requests
from base64 import b64encode
from dotenv import load_dotenv
from source.output import output
import os

# Load environment variables
load_dotenv()

# Configuration
EBAY_CLIENTID = os.getenv("EBAY_CLIENTID")
EBAY_CLIENTSECRET = os.getenv("EBAY_CLIENTSECRET")
EBAY_RUNAME = os.getenv("EBAY_RUNAME")
TOKEN_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"

def get_oauth_token(authorization_code):
    """
    Exchanges the authorization code for an OAuth access token.
    Args:
        authorization_code (str): The authorization code received after authorization.
    Returns:
        str: The access token if successful, None otherwise.
    """
    output("Exchanging authorization code for access token...", "INFO")

    if not EBAY_CLIENTID or not EBAY_CLIENTSECRET or not EBAY_RUNAME:
        output("Missing Client ID, Client Secret, or Redirect Name in environment variables.", "ERROR")
        return None

    # Base64-Encode for basic auth
    auth_header = b64encode(f"{EBAY_CLIENTID}:{EBAY_CLIENTSECRET}".encode()).decode()

    # Request-header and data
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": EBAY_RUNAME,
    }

    # API call
    response = requests.post(TOKEN_URL, headers=headers, data=data)

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        output("Access Token successfully generated.", "INFO")
        return access_token
    else:
        output(f"Failed to generate access token. Status Code: {response.status_code}", "ERROR")
        output(f"Response: {response.text}", "ERROR")
        return None

if __name__ == "__main__":
    authorization_code = input("Enter the authorization code: ").strip()
    token = get_oauth_token(authorization_code)
    if token:
        print(f"Generated Access Token: {token}")
    else:
        print("Failed to generate access token.")