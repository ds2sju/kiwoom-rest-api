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
        
    def unfilled_split_order_detail_request_ka10088(
        self,
        order_no: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        미체결 분할주문 상세 요청 (ka10088)

        Args:
            order_no (str): 주문번호 (20자리)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 미체결 분할주문 상세 데이터
                {
                    "osop": [
                        {
                            "stk_cd": str,  # 종목코드
                            "acnt_no": str,  # 계좌번호
                            "stk_nm": str,  # 종목명
                            "ord_no": str,  # 주문번호
                            "ord_qty": str,  # 주문수량
                            "ord_pric": str,  # 주문가격
                            "osop_qty": str,  # 미체결수량
                            "io_tp_nm": str,  # 주문구분
                            "trde_tp": str,  # 매매구분
                            "sell_tp": str,  # 매도/수 구분
                            "cntr_qty": str,  # 체결량
                            "ord_stt": str,  # 주문상태
                            "cur_prc": str,  # 현재가
                            "stex_tp": str,  # 거래소구분 (0:통합, 1:KRX, 2:NXT)
                            "stex_tp_txt": str,  # 거래소구분텍스트 (통합,KRX,NXT)
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.unfilled_split_order_detail_request_ka10088(
            ...     order_no="8"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10088",
        }
        data = {
            "ord_no": order_no,
        }
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def today_trading_journal_request_ka10170(
        self,
        ottks_tp: str,
        ch_crd_tp: str,
        base_dt: str = "",
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        당일매매일지 요청 (ka10170)

        Args:
            ottks_tp (str): 단주구분 (1:당일매수에 대한 당일매도, 2:당일매도 전체)
            ch_crd_tp (str): 현금신용구분 (0:전체, 1:현금매매만, 2:신용매매만)
            base_dt (str, optional): 기준일자 (YYYYMMDD). 공백입력시 금일데이터, 최근 2개월까지 제공. Defaults to "".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 당일매매일지 데이터
                {
                    "tot_sell_amt": str,  # 총매도금액
                    "tot_buy_amt": str,  # 총매수금액
                    "tot_cmsn_tax": str,  # 총수수료_세금
                    "tot_exct_amt": str,  # 총정산금액
                    "tot_pl_amt": str,  # 총손익금액
                    "tot_prft_rt": str,  # 총수익률
                    "tdy_trde_diary": [  # 당일매매일지
                        {
                            "stk_nm": str,  # 종목명
                            "buy_avg_pric": str,  # 매수평균가
                            "buy_qty": str,  # 매수수량
                            "sel_avg_pric": str,  # 매도평균가
                            "sell_qty": str,  # 매도수량
                            "cmsn_alm_tax": str,  # 수수료_제세금
                            "pl_amt": str,  # 손익금액
                            "sell_amt": str,  # 매도금액
                            "buy_amt": str,  # 매수금액
                            "prft_rt": str,  # 수익률
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
            >>> result = api.account.today_trading_journal_request_ka10170(
            ...     ottks_tp="1",
            ...     ch_crd_tp="0",
            ...     base_dt="20241120"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10170",
        }
        data = {
            "ottks_tp": ottks_tp,
            "ch_crd_tp": ch_crd_tp,
        }
        if base_dt:
            data["base_dt"] = base_dt
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
    
    def deposit_detail_status_request_kt00001(
        self,
        qry_tp: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        예수금상세현황 요청 (kt00001)

        Args:
            qry_tp (str): 조회구분 (3:추정조회, 2:일반조회)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 예수금상세현황 데이터
                {
                    "entr": str,  # 예수금
                    "profa_ch": str,  # 주식증거금현금
                    "bncr_profa_ch": str,  # 수익증권증거금현금
                    "nxdy_bncr_sell_exct": str,  # 익일수익증권매도정산대금
                    "fc_stk_krw_repl_set_amt": str,  # 해외주식원화대용설정금
                    "crd_grnta_ch": str,  # 신용보증금현금
                    "crd_grnt_ch": str,  # 신용담보금현금
                    "add_grnt_ch": str,  # 추가담보금현금
                    "etc_profa": str,  # 기타증거금
                    "uncl_stk_amt": str,  # 미수확보금
                    "shrts_prica": str,  # 공매도대금
                    "crd_set_grnta": str,  # 신용설정평가금
                    "chck_ina_amt": str,  # 수표입금액
                    "etc_chck_ina_amt": str,  # 기타수표입금액
                    "crd_grnt_ruse": str,  # 신용담보재사용
                    "knx_asset_evltv": str,  # 코넥스기본예탁금
                    "elwdpst_evlta": str,  # ELW예탁평가금
                    "crd_ls_rght_frcs_amt": str,  # 신용대주권리예정금액
                    "lvlh_join_amt": str,  # 생계형가입금액
                    "lvlh_trns_alowa": str,  # 생계형입금가능금액
                    "repl_amt": str,  # 대용금평가금액(합계)
                    "remn_repl_evlta": str,  # 잔고대용평가금액
                    "trst_remn_repl_evlta": str,  # 위탁대용잔고평가금액
                    "bncr_remn_repl_evlta": str,  # 수익증권대용평가금액
                    "profa_repl": str,  # 위탁증거금대용
                    "crd_grnta_repl": str,  # 신용보증금대용
                    "crd_grnt_repl": str,  # 신용담보금대용
                    "add_grnt_repl": str,  # 추가담보금대용
                    "rght_repl_amt": str,  # 권리대용금
                    "pymn_alow_amt": str,  # 출금가능금액
                    "wrap_pymn_alow_amt": str,  # 랩출금가능금액
                    "ord_alow_amt": str,  # 주문가능금액
                    "bncr_buy_alowa": str,  # 수익증권매수가능금액
                    "20stk_ord_alow_amt": str,  # 20%종목주문가능금액
                    "30stk_ord_alow_amt": str,  # 30%종목주문가능금액
                    "40stk_ord_alow_amt": str,  # 40%종목주문가능금액
                    "100stk_ord_alow_amt": str,  # 100%종목주문가능금액
                    "ch_uncla": str,  # 현금미수금
                    "ch_uncla_dlfe": str,  # 현금미수연체료
                    "ch_uncla_tot": str,  # 현금미수금합계
                    "crd_int_npay": str,  # 신용이자미납
                    "int_npay_amt_dlfe": str,  # 신용이자미납연체료
                    "int_npay_amt_tot": str,  # 신용이자미납합계
                    "etc_loana": str,  # 기타대여금
                    "etc_loana_dlfe": str,  # 기타대여금연체료
                    "etc_loan_tot": str,  # 기타대여금합계
                    "nrpy_loan": str,  # 미상환융자금
                    "loan_sum": str,  # 융자금합계
                    "ls_sum": str,  # 대주금합계
                    "crd_grnt_rt": str,  # 신용담보비율
                    "mdstrm_usfe": str,  # 중도이용료
                    "min_ord_alow_yn": str,  # 최소주문가능금액
                    "loan_remn_evlt_amt": str,  # 대출총평가금액
                    "dpst_grntl_remn": str,  # 예탁담보대출잔고
                    "sell_grntl_remn": str,  # 매도담보대출잔고
                    "d1_entra": str,  # d+1추정예수금
                    "d1_slby_exct_amt": str,  # d+1매도매수정산금
                    "d1_buy_exct_amt": str,  # d+1매수정산금
                    "d1_out_rep_mor": str,  # d+1미수변제소요금
                    "d1_sel_exct_amt": str,  # d+1매도정산금
                    "d1_pymn_alow_amt": str,  # d+1출금가능금액
                    "d2_entra": str,  # d+2추정예수금
                    "d2_slby_exct_amt": str,  # d+2매도매수정산금
                    "d2_buy_exct_amt": str,  # d+2매수정산금
                    "d2_out_rep_mor": str,  # d+2미수변제소요금
                    "d2_sel_exct_amt": str,  # d+2매도정산금
                    "d2_pymn_alow_amt": str,  # d+2출금가능금액
                    "50stk_ord_alow_amt": str,  # 50%종목주문가능금액
                    "60stk_ord_alow_amt": str,  # 60%종목주문가능금액
                    "stk_entr_prst": [  # 종목별예수금
                        {
                            "crnc_cd": str,  # 통화코드
                            "fx_entr": str,  # 외화예수금
                            "fc_krw_repl_evlta": str,  # 원화대용평가금
                            "fc_trst_profa": str,  # 해외주식증거금
                            "pymn_alow_amt": str,  # 출금가능금액
                            "pymn_alow_amt_entr": str,  # 출금가능금액(예수금)
                            "ord_alow_amt_entr": str,  # 주문가능금액(예수금)
                            "fc_uncla": str,  # 외화미수(합계)
                            "fc_ch_uncla": str,  # 외화현금미수금
                            "dly_amt": str,  # 연체료
                            "d1_fx_entr": str,  # d+1외화예수금
                            "d2_fx_entr": str,  # d+2외화예수금
                            "d3_fx_entr": str,  # d+3외화예수금
                            "d4_fx_entr": str,  # d+4외화예수금
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.deposit_detail_status_request_kt00001(
            ...     qry_tp="3"  # 추정조회
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "kt00001",
        }
        data = {
            "qry_tp": qry_tp,
        }
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def daily_estimated_deposit_asset_status_request_kt00002(
        self,
        start_dt: str,
        end_dt: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        일별추정예탁자산현황 요청 (kt00002)

        Args:
            start_dt (str): 시작조회기간 (YYYYMMDD)
            end_dt (str): 종료조회기간 (YYYYMMDD)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 일별추정예탁자산현황 데이터
                {
                    "daly_prsm_dpst_aset_amt_prst": [  # 일별추정예탁자산현황
                        {
                            "dt": str,  # 일자
                            "entr": str,  # 예수금
                            "grnt_use_amt": str,  # 담보대출금
                            "crd_loan": str,  # 신용융자금
                            "ls_grnt": str,  # 대주담보금
                            "repl_amt": str,  # 대용금
                            "prsm_dpst_aset_amt": str,  # 추정예탁자산
                            "prsm_dpst_aset_amt_bncr_skip": str,  # 추정예탁자산수익증권제외
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.daily_estimated_deposit_asset_status_request_kt00002(
            ...     start_dt="20241111",
            ...     end_dt="20241125"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "kt00002",
        }
        data = {
            "start_dt": start_dt,
            "end_dt": end_dt,
        }
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def estimated_asset_inquiry_request_kt00003(
        self,
        qry_tp: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> dict:
        """
        추정자산조회요청 (kt00003)

        Args:
            qry_tp (str): 상장폐지조회구분 (0:전체, 1:상장폐지종목제외)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 추정자산 데이터
                {
                    "prsm_dpst_aset_amt": str,  # 추정예탁자산
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.account.estimated_asset_inquiry_request_kt00003(
            ...     qry_tp="0"  # 전체 조회
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "kt00003",
        }
        data = {
            "qry_tp": qry_tp,
        }
            
        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )