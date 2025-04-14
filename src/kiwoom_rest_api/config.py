import os
from typing import Optional

# Base URLs
DEFAULT_BASE_URL = "https://openapi.kiwoom.com/v1"
SANDBOX_BASE_URL = "https://openapivts.kiwoom.com/v1"

# API Credentials
API_KEY = os.environ.get("KIWOOM_API_KEY", "")
API_SECRET = os.environ.get("KIWOOM_API_SECRET", "")

# Authentication
TOKEN_URL = "/oauth2/token"
AUTH_URL = "/oauth2/authorize"

# Timeouts
DEFAULT_TIMEOUT = 30.0  # seconds

# Environment setting
USE_SANDBOX = os.environ.get("KIWOOM_USE_SANDBOX", "false").lower() == "true"

def get_base_url() -> str:
    """Return the base URL based on environment settings"""
    if USE_SANDBOX:
        return SANDBOX_BASE_URL
    return DEFAULT_BASE_URL

def get_api_key() -> str:
    """Return the API key"""
    return API_KEY

def get_api_secret() -> str:
    """Return the API secret"""
    return API_SECRET

def get_headers(access_token: Optional[str] = None) -> dict:
    """Return common headers for API requests"""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    else:
        headers["appkey"] = get_api_key()
        headers["appsecret"] = get_api_secret()
    
    return headers
