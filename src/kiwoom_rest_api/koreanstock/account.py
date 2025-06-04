from kiwoom_rest_api.core.base_api import KiwoomBaseAPI
from typing import Union, Dict, Any, Awaitable

class Account(KiwoomBaseAPI):
    """한국 주식 계좌 관련 API를 제공하는 클래스"""
    
    def __init__(
        self, 
        base_url: str = None, 
        token_manager=None, 
        use_async: bool = False,
        resource_url: str = "/api/dostk/acnt"
    ):
        """
        Account 클래스 초기화
        
        Args:
            base_url (str, optional): API 기본 URL
            token_manager: 토큰 관리자 객체
            use_async (bool): 비동기 클라이언트 사용 여부 (기본값: False)
        """
        super().__init__(
            base_url=base_url,
            token_manager=token_manager,
            use_async=use_async,
            resource_url=resource_url
        )
        
    def realized_profit_by_date_stock_request_ka10072(
        self,
        stock_code: str,
        start_date: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        일자별종목별실현손익요청 (ka10072)

        Args:
            stock_code (str): 종목코드 (6자리)
            start_date (str): 시작일자 (YYYYMMDD)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 일자별종목별실현손익 데이터
                {
                    "dt_stk_div_rlzt_pl": [
                        {
                            "stk_nm": str,  # 종목명
                            "cntr_qty": str,  # 체결량
                            "buy_uv": str,  # 매입단가
                            "cntr_pric": str,  # 체결가
                            "tdy_sel_pl": str,  # 당일매도손익
                            "pl_rt": str,  # 손익율
                            "stk_cd": str,  # 종목코드
                            "tdy_trde_cmsn": str,  # 당일매매수수료
                            "tdy_trde_tax": str,  # 당일매매세금
                            "wthd_alowa": str,  # 인출가능금액
                            "loan_dt": str,  # 대출일
                            "crd_tp": str,  # 신용구분
                            "stk_cd_1": str,  # 종목코드1
                            "tdy_sel_pl_1": str,  # 당일매도손익1
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.realized_profit_by_date_stock_request_ka10072(
            ...     stock_code="005930",
            ...     start_date="20241128"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10072",
        }
        data = {
            "stk_cd": stock_code,
            "strt_dt": start_date,
        }
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def realized_profit_by_period_stock_request_ka10073(
        self,
        stock_code: str,
        start_date: str,
        end_date: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        일자별종목별실현손익요청_기간 (ka10073)

        Args:
            stock_code (str): 종목코드 (6자리)
            start_date (str): 시작일자 (YYYYMMDD)
            end_date (str): 종료일자 (YYYYMMDD)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 일자별종목별실현손익 데이터
                {
                    "dt_stk_rlzt_pl": [
                        {
                            "dt": str,  # 일자
                            "tdy_htssel_cmsn": str,  # 당일hts매도수수료
                            "stk_nm": str,  # 종목명
                            "cntr_qty": str,  # 체결량
                            "buy_uv": str,  # 매입단가
                            "cntr_pric": str,  # 체결가
                            "tdy_sel_pl": str,  # 당일매도손익
                            "pl_rt": str,  # 손익율
                            "stk_cd": str,  # 종목코드
                            "tdy_trde_cmsn": str,  # 당일매매수수료
                            "tdy_trde_tax": str,  # 당일매매세금
                            "wthd_alowa": str,  # 인출가능금액
                            "loan_dt": str,  # 대출일
                            "crd_tp": str,  # 신용구분
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.realized_profit_by_period_stock_request_ka10073(
            ...     stock_code="005930",
            ...     start_date="20241128",
            ...     end_date="20241128"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10073",
        }
        data = {
            "stk_cd": stock_code,
            "strt_dt": start_date,
            "end_dt": end_date,
        }
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def daily_realized_profit_request_ka10074(
        self,
        start_date: str,
        end_date: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        일자별실현손익요청 (ka10074)

        Args:
            start_date (str): 시작일자 (YYYYMMDD)
            end_date (str): 종료일자 (YYYYMMDD)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 일자별실현손익 데이터
                {
                    "tot_buy_amt": str,  # 총매수금액
                    "tot_sell_amt": str,  # 총매도금액
                    "rlzt_pl": str,  # 실현손익
                    "trde_cmsn": str,  # 매매수수료
                    "trde_tax": str,  # 매매세금
                    "dt_rlzt_pl": [
                        {
                            "dt": str,  # 일자
                            "buy_amt": str,  # 매수금액
                            "sell_amt": str,  # 매도금액
                            "tdy_sel_pl": str,  # 당일매도손익
                            "tdy_trde_cmsn": str,  # 당일매매수수료
                            "tdy_trde_tax": str,  # 당일매매세금
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.daily_realized_profit_request_ka10074(
            ...     start_date="20241128",
            ...     end_date="20241128"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10074",
        }
        data = {
            "strt_dt": start_date,
            "end_dt": end_date,
        }
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )