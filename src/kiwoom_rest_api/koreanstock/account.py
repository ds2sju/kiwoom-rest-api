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
        
    def unfilled_orders_request_ka10075(
        self,
        all_stk_tp: str,
        trde_tp: str,
        stex_tp: str,
        stock_code: str = None,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        미체결요청 (ka10075)

        Args:
            all_stk_tp (str): 전체종목구분 (0:전체, 1:종목)
            trde_tp (str): 매매구분 (0:전체, 1:매도, 2:매수)
            stex_tp (str): 거래소구분 (0:통합, 1:KRX, 2:NXT)
            stock_code (str, optional): 종목코드 (6자리). Required when all_stk_tp is "1".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 미체결 데이터
                {
                    "oso": [
                        {
                            "acnt_no": str,  # 계좌번호
                            "ord_no": str,  # 주문번호
                            "mang_empno": str,  # 관리사번
                            "stk_cd": str,  # 종목코드
                            "tsk_tp": str,  # 업무구분
                            "ord_stt": str,  # 주문상태
                            "stk_nm": str,  # 종목명
                            "ord_qty": str,  # 주문수량
                            "ord_pric": str,  # 주문가격
                            "oso_qty": str,  # 미체결수량
                            "cntr_tot_amt": str,  # 체결누계금액
                            "orig_ord_no": str,  # 원주문번호
                            "io_tp_nm": str,  # 주문구분
                            "trde_tp": str,  # 매매구분
                            "tm": str,  # 시간
                            "cntr_no": str,  # 체결번호
                            "cntr_pric": str,  # 체결가
                            "cntr_qty": str,  # 체결량
                            "cur_prc": str,  # 현재가
                            "sel_bid": str,  # 매도호가
                            "buy_bid": str,  # 매수호가
                            "unit_cntr_pric": str,  # 단위체결가
                            "unit_cntr_qty": str,  # 단위체결량
                            "tdy_trde_cmsn": str,  # 당일매매수수료
                            "tdy_trde_tax": str,  # 당일매매세금
                            "ind_invsr": str,  # 개인투자자
                            "stex_tp": str,  # 거래소구분
                            "stex_tp_txt": str,  # 거래소구분텍스트
                            "sor_yn": str,  # SOR 여부값
                            "stop_pric": str,  # 스톱가
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.unfilled_orders_request_ka10075(
            ...     all_stk_tp="1",
            ...     trde_tp="0",
            ...     stex_tp="0",
            ...     stock_code="005930"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10075",
        }
        data = {
            "all_stk_tp": all_stk_tp,
            "trde_tp": trde_tp,
            "stex_tp": stex_tp,
        }
        if stock_code:
            data["stk_cd"] = stock_code
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def filled_orders_request_ka10076(
        self,
        qry_tp: str,
        sell_tp: str,
        stex_tp: str,
        stock_code: str = None,
        order_no: str = None,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        체결요청 (ka10076)

        Args:
            qry_tp (str): 조회구분 (0:전체, 1:종목)
            sell_tp (str): 매도수구분 (0:전체, 1:매도, 2:매수)
            stex_tp (str): 거래소구분 (0:통합, 1:KRX, 2:NXT)
            stock_code (str, optional): 종목코드 (6자리). Required when qry_tp is "1".
            order_no (str, optional): 주문번호. 검색 기준 값으로 입력한 주문번호 보다 과거에 체결된 내역이 조회됩니다.
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 체결 데이터
                {
                    "cntr": [
                        {
                            "ord_no": str,  # 주문번호
                            "stk_nm": str,  # 종목명
                            "io_tp_nm": str,  # 주문구분
                            "ord_pric": str,  # 주문가격
                            "ord_qty": str,  # 주문수량
                            "cntr_pric": str,  # 체결가
                            "cntr_qty": str,  # 체결량
                            "oso_qty": str,  # 미체결수량
                            "tdy_trde_cmsn": str,  # 당일매매수수료
                            "tdy_trde_tax": str,  # 당일매매세금
                            "ord_stt": str,  # 주문상태
                            "trde_tp": str,  # 매매구분
                            "orig_ord_no": str,  # 원주문번호
                            "ord_tm": str,  # 주문시간
                            "stk_cd": str,  # 종목코드
                            "stex_tp": str,  # 거래소구분
                            "stex_tp_txt": str,  # 거래소구분텍스트
                            "sor_yn": str,  # SOR 여부값
                            "stop_pric": str,  # 스톱가
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.filled_orders_request_ka10076(
            ...     qry_tp="1",
            ...     sell_tp="0",
            ...     stex_tp="0",
            ...     stock_code="005930"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10076",
        }
        data = {
            "qry_tp": qry_tp,
            "sell_tp": sell_tp,
            "stex_tp": stex_tp,
        }
        if stock_code:
            data["stk_cd"] = stock_code
        if order_no:
            data["ord_no"] = order_no
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def today_realized_profit_detail_request_ka10077(
        self,
        stock_code: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        당일실현손익상세요청 (ka10077)

        Args:
            stock_code (str): 종목코드 (6자리)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 당일실현손익 상세 데이터
                {
                    "tdy_rlzt_pl": str,  # 당일실현손익
                    "tdy_rlzt_pl_dtl": [
                        {
                            "stk_nm": str,  # 종목명
                            "cntr_qty": str,  # 체결량
                            "buy_uv": str,  # 매입단가
                            "cntr_pric": str,  # 체결가
                            "tdy_sel_pl": str,  # 당일매도손익
                            "pl_rt": str,  # 손익율
                            "tdy_trde_cmsn": str,  # 당일매매수수료
                            "tdy_trde_tax": str,  # 당일매매세금
                            "stk_cd": str,  # 종목코드
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.today_realized_profit_detail_request_ka10077(
            ...     stock_code="005930"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10077",
        }
        data = {
            "stk_cd": stock_code,
        }
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def account_return_rate_request_ka10085(
        self,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        계좌수익률요청 (ka10085)

        Args:
            stex_tp (str): 거래소구분 (0:통합, 1:KRX, 2:NXT)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 계좌수익률 데이터
                {
                    "acnt_prft_rt": [
                        {
                            "dt": str,  # 일자
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pur_pric": str,  # 매입가
                            "pur_amt": str,  # 매입금액
                            "rmnd_qty": str,  # 보유수량
                            "tdy_sel_pl": str,  # 당일매도손익
                            "tdy_trde_cmsn": str,  # 당일매매수수료
                            "tdy_trde_tax": str,  # 당일매매세금
                            "crd_tp": str,  # 신용구분
                            "loan_dt": str,  # 대출일
                            "setl_remn": str,  # 결제잔고
                            "clrn_alow_qty": str,  # 청산가능수량
                            "crd_amt": str,  # 신용금액
                            "crd_int": str,  # 신용이자
                            "expr_dt": str,  # 만기일
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.account_return_rate_request_ka10085(
            ...     stex_tp="0"  # 통합 거래소
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10085",
        }
        data = {
            "stex_tp": stex_tp,
        }
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )