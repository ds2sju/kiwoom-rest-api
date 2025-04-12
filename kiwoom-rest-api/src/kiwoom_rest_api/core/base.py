from typing import Any, Dict, Optional, Union
import json
from urllib.parse import urljoin

from kiwoom_rest_api.config import get_base_url, get_headers, DEFAULT_TIMEOUT

class APIError(Exception):
    """Exception raised for API errors"""
    def __init__(self, status_code: int, error_message: str, error_data: Any = None):
        self.status_code = status_code
        self.error_message = error_message
        self.error_data = error_data
        super().__init__(f"API Error (HTTP {status_code}): {error_message}")

def make_url(endpoint: str) -> str:
    """Create a full URL from an endpoint"""
    if endpoint.startswith(('http://', 'https://')):
        return endpoint
    
    # Ensure endpoint starts with a forward slash
    if not endpoint.startswith('/'):
        endpoint = f"/{endpoint}"
    
    return urljoin(get_base_url(), endpoint)

def process_response(response: Any) -> Dict[str, Any]:
    """Process API response and handle errors"""
    if not hasattr(response, 'status_code'):
        raise ValueError(f"Invalid response object: {response}")
    
    if 200 <= response.status_code < 300:
        if not response.text:
            return {}
        
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"content": response.text}
    
    # Handle error responses
    error_message = "Unknown error"
    error_data = None
    
    try:
        error_data = response.json()
        error_message = error_data.get("message", "Unknown error")
    except (json.JSONDecodeError, AttributeError):
        if response.text:
            error_message = response.text
    
    raise APIError(response.status_code, error_message, error_data)

def prepare_request_params(
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, Any]] = None,
    access_token: Optional[str] = None,
    timeout: Optional[float] = None,
) -> Dict[str, Any]:
    """Prepare common request parameters"""
    url = make_url(endpoint)
    
    request_headers = get_headers(access_token)
    if headers:
        request_headers.update(headers)
    
    request_params = {
        "url": url,
        "method": method,
        "headers": request_headers,
        "timeout": timeout or DEFAULT_TIMEOUT,
    }
    
    if params:
        request_params["params"] = params
    
    if data:
        if method.upper() in ["GET", "DELETE"]:
            if not params:
                request_params["params"] = data
            else:
                request_params["params"].update(data)
        else:
            request_params["json"] = data
    
    return request_params
