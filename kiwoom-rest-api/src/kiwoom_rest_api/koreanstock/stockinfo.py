from typing import Dict, Optional, Any, List

from kiwoom_rest_api.core.sync_client import make_request

def get_basic_stock_info(
    stock_code: str,
    access_token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    주식 기본정보 요청 (KA-STOCK-002)
    
    Args:
        stock_code: 종목코드 (6자리)
        access_token: OAuth 액세스 토큰
    
    Returns:
        주식 기본정보 데이터
    """
    endpoint = "/stock/basic"
    params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": stock_code}
    
    return make_request(
        endpoint=endpoint,
        params=params,
        access_token=access_token,
    )

def get_stock_price(
    stock_code: str,
    access_token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    주식 현재가 조회 (KA-STOCK-001)
    
    Args:
        stock_code: 종목코드 (6자리)
        access_token: OAuth 액세스 토큰
    
    Returns:
        주식 현재가 데이터
    """
    endpoint = "/stock/price"
    params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": stock_code}
    
    return make_request(
        endpoint=endpoint,
        params=params,
        access_token=access_token,
    )

def get_daily_price(
    stock_code: str,
    period: str = "D",
    adj_price: str = "1",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    access_token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    일별 주가 조회 (KA-STOCK-004)
    
    Args:
        stock_code: 종목코드 (6자리)
        period: 기간분류코드 (D:일봉, W:주봉, M:월봉, Y:년봉)
        adj_price: 수정주가 여부 (0:수정없음, 1:수정주가)
        start_date: 조회 시작 날짜 (YYYYMMDD)
        end_date: 조회 끝 날짜 (YYYYMMDD)
        access_token: OAuth 액세스 토큰
    
    Returns:
        일/주/월/년별 주가 데이터
    """
    endpoint = "/stock/dailyprice"
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": stock_code,
        "FID_PERIOD_DIV_CODE": period,
        "FID_ORG_ADJ_PRC": adj_price,
    }
    
    if start_date:
        params["FID_INPUT_DATE_1"] = start_date
    
    if end_date:
        params["FID_INPUT_DATE_2"] = end_date
    
    return make_request(
        endpoint=endpoint,
        params=params,
        access_token=access_token,
    )

def get_multiple_stock_prices(
    stock_codes: List[str],
    access_token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    복수종목 현재가 조회 (KA-STOCK-003)
    
    Args:
        stock_codes: 종목코드 리스트 (최대 50개)
        access_token: OAuth 액세스 토큰
    
    Returns:
        복수종목 현재가 데이터
    """
    if len(stock_codes) > 50:
        raise ValueError("Maximum of 50 stock codes can be requested at once")
    
    endpoint = "/stock/multiquote"
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD_LIST": ";".join(stock_codes),
    }
    
    return make_request(
        endpoint=endpoint,
        params=params,
        access_token=access_token,
    )
