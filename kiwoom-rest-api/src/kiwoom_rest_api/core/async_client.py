from typing import Any, Dict, Optional

import httpx

from kiwoom_rest_api.core.base import prepare_request_params, process_response

async def make_request_async(
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, Any]] = None,
    access_token: Optional[str] = None,
    timeout: Optional[float] = None,
) -> Dict[str, Any]:
    """Make an asynchronous HTTP request to the Kiwoom API"""
    request_params = prepare_request_params(
        endpoint=endpoint,
        method=method,
        params=params,
        data=data,
        headers=headers,
        access_token=access_token,
        timeout=timeout,
    )
    
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request_params["method"],
            url=request_params["url"],
            params=request_params.get("params"),
            json=request_params.get("json"),
            headers=request_params["headers"],
            timeout=request_params["timeout"],
        )
        
        return process_response(response)
