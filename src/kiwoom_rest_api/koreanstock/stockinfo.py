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
    
    def reported_low_price_request_ka10016(
        self,
        market_type: str,
        report_type: str,
        high_low_close_type: str,
        stock_condition: str,
        trade_quantity_type: str,
        credit_condition: str,
        updown_include: str,
        period: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """신고저가 요청

        Args:
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥)
            report_type (str): 신고저구분 (1:신고가, 2:신저가)
            high_low_close_type (str): 고저종구분 (1:고저기준, 2:종가기준)
            stock_condition (str): 종목조건 (0:전체조회, 1:관리종목제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기)
            trade_quantity_type (str): 거래량구분 (00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, ...)
            credit_condition (str): 신용조건 (0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체)
            updown_include (str): 상하한포함 (0:미포함, 1:포함)
            period (str): 기간 (5:5일, 10:10일, 20:20일, 60:60일, 250:250일)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "ntl_pric": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "334",
                        "pred_pre_sig": "3",
                        "pred_pre": "0",
                        "flu_rt": "0.00",
                        "trde_qty": "3",
                        "pred_trde_qty_pre_rt": "-0.00",
                        "sel_bid": "0",
                        "buy_bid": "0",
                        "high_pric": "334",
                        "low_pric": "320"
                    },
                    ...
                ]
            }
        """
        
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10016"
        }
        
        # 요청 데이터 구성
        data = {
            "mrkt_tp": market_type,
            "ntl_tp": report_type,
            "high_low_close_tp": high_low_close_type,
            "stk_cnd": stock_condition,
            "trde_qty_tp": trade_quantity_type,
            "crd_cnd": credit_condition,
            "updown_incls": updown_include,
            "dt": period,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)


