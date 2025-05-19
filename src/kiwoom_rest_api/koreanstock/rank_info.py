from kiwoom_rest_api.core.base_api import KiwoomBaseAPI
from typing import Union, Dict, Any, Awaitable

class RankInfo(KiwoomBaseAPI):
    """한국 주식 랭크 정보 API를 제공하는 클래스"""
    
    def __init__(
        self, 
        base_url: str = None, 
        token_manager=None, 
        use_async: bool = False,
        resource_url: str = "/api/dostk/rkinfo"
    ):
        """
        RankInfo 클래스 초기화
        
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
        
   
        

    def top_order_book_volume_request_ka10020(
        self,
        mrkt_tp: str,
        sort_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        crd_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """호가잔량상위를 조회합니다.

        Args:
            mrkt_tp (str): 시장구분 (001:코스피, 101:코스닥)
            sort_tp (str): 정렬구분
                - 1: 순매수잔량순
                - 2: 순매도잔량순
                - 3: 매수비율순
                - 4: 매도비율순
            trde_qty_tp (str): 거래량구분
                - 0000: 장시작전(0주이상)
                - 0010: 만주이상
                - 0050: 5만주이상
                - 00100: 10만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
            crd_cnd (str): 신용조건
                - 0: 전체조회
                - 1: 신용융자A군
                - 2: 신용융자B군
                - 3: 신용융자C군
                - 4: 신용융자D군
                - 9: 신용융자전체
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 호가잔량상위 데이터
                {
                    "bid_req_upper": [  # 호가잔량상위
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "trde_qty": str,  # 거래량
                            "tot_sel_req": str,  # 총매도잔량
                            "tot_buy_req": str,  # 총매수잔량
                            "netprps_req": str,  # 순매수잔량
                            "buy_rt": str,  # 매수비율
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_order_book_volume_request_ka10020(
            ...     mrkt_tp="001",
            ...     sort_tp="1",
            ...     trde_qty_tp="0000",
            ...     stk_cnd="0",
            ...     crd_cnd="0",
            ...     stex_tp="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10020",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_tp": sort_tp,
            "trde_qty_tp": trde_qty_tp,
            "stk_cnd": stk_cnd,
            "crd_cnd": crd_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def sudden_increase_order_book_volume_request_ka10021(
        self,
        mrkt_tp: str,
        trde_tp: str,
        sort_tp: str,
        tm_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """호가잔량급증을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분 (001:코스피, 101:코스닥)
            trde_tp (str): 매매구분
                - 1: 매수잔량
                - 2: 매도잔량
            sort_tp (str): 정렬구분
                - 1: 급증량
                - 2: 급증률
            tm_tp (str): 시간구분 (분 입력)
            trde_qty_tp (str): 거래량구분
                - 1: 천주이상
                - 5: 5천주이상
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 호가잔량급증 데이터
                {
                    "bid_req_sdnin": [  # 호가잔량급증
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "int": str,  # 기준률
                            "now": str,  # 현재
                            "sdnin_qty": str,  # 급증수량
                            "sdnin_rt": str,  # 급증률
                            "tot_buy_qty": str,  # 총매수량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.sudden_increase_order_book_volume_request_ka10021(
            ...     mrkt_tp="001",
            ...     trde_tp="1",
            ...     sort_tp="1",
            ...     tm_tp="30",
            ...     trde_qty_tp="1",
            ...     stk_cnd="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10021",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "trde_tp": trde_tp,
            "sort_tp": sort_tp,
            "tm_tp": tm_tp,
            "trde_qty_tp": trde_qty_tp,
            "stk_cnd": stk_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def sudden_increase_order_ratio_request_ka10022(
        self,
        mrkt_tp: str,
        rt_tp: str,
        tm_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """잔량율급증을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분 (001:코스피, 101:코스닥)
            rt_tp (str): 비율구분
                - 1: 매수/매도비율
                - 2: 매도/매수비율
            tm_tp (str): 시간구분 (분 입력)
            trde_qty_tp (str): 거래량구분
                - 5: 5천주이상
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 잔량율급증 데이터
                {
                    "req_rt_sdnin": [  # 잔량율급증
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "int": str,  # 기준률
                            "now_rt": str,  # 현재비율
                            "sdnin_rt": str,  # 급증률
                            "tot_sel_req": str,  # 총매도잔량
                            "tot_buy_req": str,  # 총매수잔량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.sudden_increase_order_ratio_request_ka10022(
            ...     mrkt_tp="001",
            ...     rt_tp="1",
            ...     tm_tp="1",
            ...     trde_qty_tp="5",
            ...     stk_cnd="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10022",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "rt_tp": rt_tp,
            "tm_tp": tm_tp,
            "trde_qty_tp": trde_qty_tp,
            "stk_cnd": stk_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
    
    def sudden_increase_trading_volume_request_ka10023(
        self,
        mrkt_tp: str,
        sort_tp: str,
        tm_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        pric_tp: str,
        stex_tp: str,
        tm: str = "",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """거래량급증을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            sort_tp (str): 정렬구분
                - 1: 급증량
                - 2: 급증률
                - 3: 급감량
                - 4: 급감률
            tm_tp (str): 시간구분
                - 1: 분
                - 2: 전일
            trde_qty_tp (str): 거래량구분
                - 5: 5천주이상
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
                - 200: 20만주이상
                - 300: 30만주이상
                - 500: 50만주이상
                - 1000: 백만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 3: 우선주제외
                - 11: 정리매매종목제외
                - 4: 관리종목,우선주제외
                - 5: 증100제외
                - 6: 증100만보기
                - 13: 증60만보기
                - 12: 증50만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
                - 17: ETN제외
                - 14: ETF제외
                - 18: ETF+ETN제외
                - 15: 스팩제외
                - 20: ETF+ETN+스팩제외
            pric_tp (str): 가격구분
                - 0: 전체조회
                - 2: 5만원이상
                - 5: 1만원이상
                - 6: 5천원이상
                - 8: 1천원이상
                - 9: 10만원이상
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            tm (str, optional): 시간(분 입력). Defaults to "".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 거래량급증 데이터
                {
                    "trde_qty_sdnin": [  # 거래량급증
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "prev_trde_qty": str,  # 이전거래량
                            "now_trde_qty": str,  # 현재거래량
                            "sdnin_qty": str,  # 급증량
                            "sdnin_rt": str,  # 급증률
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.sudden_increase_trading_volume_request_ka10023(
            ...     mrkt_tp="000",
            ...     sort_tp="1",
            ...     tm_tp="2",
            ...     trde_qty_tp="5",
            ...     stk_cnd="0",
            ...     pric_tp="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10023",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_tp": sort_tp,
            "tm_tp": tm_tp,
            "trde_qty_tp": trde_qty_tp,
            "tm": tm,
            "stk_cnd": stk_cnd,
            "pric_tp": pric_tp,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        