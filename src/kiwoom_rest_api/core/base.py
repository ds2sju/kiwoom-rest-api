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
        
    print("\n\n##  full url  ##\n\n", urljoin(get_base_url(), endpoint))
    
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
    """Prepare request parameters for HTTP request"""
    # 헤더 정규화
    normalized_headers = {}
    if headers:
        for key, value in headers.items():
            # 모든 헤더 키를 소문자로 변환하여 중복 방지
            normalized_headers[key.lower()] = value
    
    # 기본 헤더 설정
    default_headers = {
        "content-type": "application/json;charset=UTF-8",
    }
    
    # API 키 추가
    from kiwoom_rest_api.config import get_api_key, get_api_secret
    default_headers["appkey"] = get_api_key()
    default_headers["appsecret"] = get_api_secret()
    
    # 헤더 병합 (사용자 정의 헤더가 기본 헤더보다 우선)
    merged_headers = {**default_headers, **normalized_headers}
    
    # 액세스 토큰 추가
    if access_token:
        merged_headers["authorization"] = f"Bearer {access_token}"
    
    # URL 구성
    from kiwoom_rest_api.config import get_base_url
    url = endpoint if endpoint.startswith(("http://", "https://")) else f"{get_base_url()}{endpoint}"
    
    # 요청 파라미터 구성
    request_params = {
        "url": url,
        "method": method,
        "headers": merged_headers,
        "timeout": timeout or DEFAULT_TIMEOUT,
    }
    
    # 쿼리 파라미터 추가
    if params:
        request_params["params"] = params
    
    # POST/PUT/PATCH 요청용 데이터 추가
    if method in ["POST", "PUT", "PATCH"] and data:
        if merged_headers.get("content-type", "").startswith("application/json"):
            request_params["json"] = data
        else:
            request_params["data"] = data
    
    return request_params
