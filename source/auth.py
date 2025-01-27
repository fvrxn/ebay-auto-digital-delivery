import os
from urllib.parse import urlencode
from dotenv import load_dotenv
from source.output import output

# Load environment variables
load_dotenv()

# Configuration
EBAY_CLIENTID = os.getenv("EBAY_CLIENTID")
EBAY_RUNAME = os.getenv("EBAY_RUNAME")
EBAY_SCOPES = [
    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
    "https://api.ebay.com/oauth/api_scope/sell.account",
    "https://api.ebay.com/oauth/api_scope/sell.inventory",
]

def get_authorization_url():
    """
    Generates the eBay authorization URL for OAuth.
    Returns:
        str: The authorization URL.
    """
    if not EBAY_CLIENTID or not EBAY_RUNAME:
        output("Client ID or Redirect Name not found in environment variables.", "ERROR")
        return None

    base_url = "https://auth.sandbox.ebay.com/oauth2/authorize"
    params = {
        "client_id": EBAY_CLIENTID,
        "response_type": "code",
        "redirect_uri": EBAY_RUNAME,
        "scope": " ".join(EBAY_SCOPES),
    }
    authorization_url = f"{base_url}?{urlencode(params)}"
    output(f"Authorization URL generated: {authorization_url}", "INFO")
    return authorization_url

if __name__ == "__main__":
    url = get_authorization_url()
    if url:
        print(f"Visit this URL to authorize the app:\n{url}")
    else:
        print("Failed to generate authorization URL.")