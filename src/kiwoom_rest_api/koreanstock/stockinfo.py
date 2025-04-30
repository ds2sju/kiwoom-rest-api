from typing import Dict, Optional, Any, List, Union, Callable, Awaitable

from kiwoom_rest_api.core.sync_client import make_request
from kiwoom_rest_api.core.async_client import make_request_async


class StockInfo:
    """한국 주식 종목 정보 관련 API를 제공하는 클래스"""
    
    def __init__(
        self, 
        base_url: str = None, 
        token_manager=None, 
        use_async: bool = False
    ):
        """
        StockInfo 클래스 초기화
        
        Args:
            base_url (str, optional): API 기본 URL
            token_manager: 토큰 관리자 객체
            use_async (bool): 비동기 클라이언트 사용 여부 (기본값: False)
        """
        self.base_url = base_url
        self.token_manager = token_manager
        self.use_async = use_async
        
        # 사용할 request 함수 결정
        self._request_func = make_request_async if use_async else make_request
    
    def _get_access_token(self) -> Optional[str]:
        """토큰 매니저로부터 액세스 토큰을 가져옵니다."""
        if self.token_manager:
            return self.token_manager.get_token()
        return None
    
    async def _get_access_token_async(self) -> Optional[str]:
        """토큰 매니저로부터 비동기적으로 액세스 토큰을 가져옵니다."""
        if self.token_manager and hasattr(self.token_manager, 'get_token_async'):
            return await self.token_manager.get_token_async()
        return self._get_access_token()  # 비동기 메서드가 없으면 동기 버전 사용
    
    def _make_request(self, method: str, url: str, **kwargs):
        """API 요청을 실행합니다."""
        headers = kwargs.pop("headers", {})
        headers["content-type"] = "application/json;charset=UTF-8"
        
        # Check if there's a nested headers in kwargs (e.g. in json payload)
        if "json" in kwargs and "headers" in kwargs.get("json", {}):
            headers.update(kwargs["json"]["headers"])
            del kwargs["json"]["headers"]
        elif "headers" in kwargs:
            headers.update(kwargs["headers"])
            del kwargs["headers"]
        
        if self.token_manager:
            access_token = self._get_access_token()
            headers["Authorization"] = f"Bearer {access_token}"
            
        return make_request(
            endpoint=url,
            method=method,
            headers=headers,
            **kwargs
        )
    
    async def _make_request_async(self, method: str, url: str, **kwargs):
        """API 요청을 비동기적으로 실행합니다."""
        headers = kwargs.pop("headers", {})

        headers["content-type"] = "application/json;charset=UTF-8"
        
        if self.token_manager:
            access_token = await self._get_access_token_async()
            headers["Authorization"] = f"Bearer {access_token}"
        
        return await make_request_async(
            endpoint=url,
            method=method,
            headers=headers,
            **kwargs
        )
    
    def _execute_request(self, method: str, **kwargs):
        """동기 또는 비동기 요청을 실행합니다."""
        url = f"{self.base_url}/api/dostk/stkinfo" if self.base_url else "/api/dostk/stkinfo"
        
        if self.use_async:
            return self._make_request_async(method, url, **kwargs)

        return self._make_request(method, url, **kwargs)
    

    def basic_stock_information_request_ka10001(
        self, stock_code: str, cont_yn: str = "N", next_key: str = "0"
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """
        주식기본정보요청
        API ID: ka10001

        Args:
            stock_code (str): 종목코드 (예: '005930')

        Returns:
            Dict[str, Any] or Awaitable[Dict[str, Any]]: 주식 기본 정보
        """
        
        headers = {
            "cont-yn": cont_yn, 
            "next-key": next_key,
            "api-id": "ka10001"
        }

        body = {
            "stk_cd": stock_code, 
        }
        

        
        return self._execute_request("POST", json=body, headers=headers)
    
    def stock_trading_agent_request_ka10002(
        self, stock_code: str, cont_yn: str = "N", next_key: str = "0"
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """
        주식 거래원 요청
        API ID (TR_ID): ka10002 (명세서 예시 ID, 실제 TR ID 확인 필요)

        Args:
            stock_code (str): 종목코드 (예: '005930', 'KRX:039490')
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Dict[str, Any] or Awaitable[Dict[str, Any]]: 현재가 정보 딕셔너리 또는 Awaitable 객체
        """
        
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10002"
        }
        
        body = {
            "stk_cd": stock_code,
        }

        return self._execute_request("POST", json=body, headers=headers)
    
    def daily_stock_price_request_ka10003(
        self,
        stock_code: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """
        체결 정보 요청
        API ID (TR_ID): ka10003 (명세서 예시 ID, 실제 TR ID 확인 필요)

        Args:
            stock_code (str): 종목코드 (예: '005930', 'KRX:039490')
            cont_yn (str, optional): 연속조회여부. 응답 헤더의 값을 사용. Defaults to "N".
            next_key (str, optional): 연속조회키. 응답 헤더의 값을 사용. Defaults to "".

        Returns:
            Dict[str, Any] or Awaitable[Dict[str, Any]]: 체결 정보 딕셔너리 또는 Awaitable 객체
        """
        
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10003"
        }
        
        body = {
            "stk_cd": stock_code,
        }
        
        return self._execute_request("POST", json=body, headers=headers)

    def credit_trading_trend_request_ka10013(
        self,
        stock_code: str,
        date: str,
        query_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """신용매매동향 요청

        Args:
            stock_code (str): 종목코드 (예: "005930")
            date (str): 조회 일자 (YYYYMMDD 형식)
            query_type (str): 조회구분 (1:융자, 2:대주)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "crd_trde_trend": [
                    {
                        "dt": "20241101",
                        "cur_prc": "65100",
                        "pred_pre_sig": "0",
                        "pred_pre": "0",
                        "trde_qty": "0",
                        "new": "",
                        "rpya": "",
                        "remn": "",
                        "amt": "",
                        "pre": "",
                        "shr_rt": "",
                        "remn_rt": ""
                    },
                    ...
                ]
            }
        """
        
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10013"
        }
        
        body = {
            "stk_cd": stock_code,
            "dt": date,
            "qry_tp": query_type,
        }
        
        return self._execute_request("POST", json=body, headers=headers)
    
    def daily_transaction_details_request_ka10015(
        self,
        stock_code: str,
        start_date: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """일별거래상세요청

        Args:
            stock_code (str): 종목코드 (예: "005930")
            start_date (str): 시작일자 (YYYYMMDD 형식)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "daly_trde_dtl": [
                    {
                        "dt": "20241105",
                        "close_pric": "135300",
                        "pred_pre_sig": "0",
                        "pred_pre": "0",
                        "flu_rt": "0.00",
                        "trde_qty": "0",
                        "trde_prica": "0",
                        "bf_mkrt_trde_qty": "",
                        "bf_mkrt_trde_wght": "",
                        "opmr_trde_qty": "",
                        "opmr_trde_wght": "",
                        "af_mkrt_trde_qty": "",
                        "af_mkrt_trde_wght": "",
                        "tot_3": "0",
                        "prid_trde_qty": "0",
                        "cntr_str": "",
                        "for_poss": "",
                        "for_wght": "",
                        "for_netprps": "",
                        "orgn_netprps": "",
                        "ind_netprps": "",
                        "frgn": "",
                        "crd_remn_rt": "",
                        "prm": "",
                        "bf_mkrt_trde_prica": "",
                        "bf_mkrt_trde_prica_wght": "",
                        "opmr_trde_prica": "",
                        "opmr_trde_prica_wght": "",
                        "af_mkrt_trde_prica": "",
                        "af_mkrt_trde_prica_wght": ""
                    },
                    ...
                ]
            }
        """
        
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10015"
        }
        
        # 요청 데이터 구성
        data = {
            "stk_cd": stock_code,
            "strt_dt": start_date
        }

        return self._execute_request("POST", json=data, headers=headers)

