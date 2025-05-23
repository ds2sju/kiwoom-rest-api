from kiwoom_rest_api.core.base_api import KiwoomBaseAPI
from typing import Union, Dict, Any, Awaitable

class ELW(KiwoomBaseAPI):
    """한국 주식 ELW 관련 API를 제공하는 클래스"""
    
    def __init__(
        self, 
        base_url: str = None, 
        token_manager=None, 
        use_async: bool = False,
        resource_url: str = "/api/dostk/elw"
    ):
        """
        ELW 클래스 초기화
        
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
        
          
    def elw_daily_sensitivity_indicator_request_ka10048(
        self,
        stk_cd: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """ELW 일별 민감도 지표를 조회합니다.

        Args:
            stk_cd (str): 종목코드 (예: "57JBHH")
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: ELW 일별 민감도 지표 데이터
                {
                    "elwdaly_snst_ix": [  # ELW일별민감도지표
                        {
                            "dt": str,  # 일자
                            "iv": str,  # IV (Implied Volatility)
                            "delta": str,  # 델타
                            "gam": str,  # 감마
                            "theta": str,  # 쎄타
                            "vega": str,  # 베가
                            "law": str,  # 로
                            "lp": str,  # LP
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.elw.elw_daily_sensitivity_indicator_request_ka10048(
            ...     stk_cd="57JBHH"  # ELW 종목코드
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10048",
        }

        data = {
            "stk_cd": stk_cd,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def elw_sensitivity_indicator_request_ka10050(
        self,
        stk_cd: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """ELW 민감도 지표를 조회합니다.

        Args:
            stk_cd (str): 종목코드 (예: "57JBHH")
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: ELW 민감도 지표 데이터
                {
                    "elwsnst_ix_array": [  # ELW민감도지표배열
                        {
                            "cntr_tm": str,  # 체결시간
                            "cur_prc": str,  # 현재가
                            "elwtheory_pric": str,  # ELW이론가
                            "iv": str,  # IV (Implied Volatility)
                            "delta": str,  # 델타
                            "gam": str,  # 감마
                            "theta": str,  # 쎄타
                            "vega": str,  # 베가
                            "law": str,  # 로
                            "lp": str,  # LP
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.elw.elw_sensitivity_indicator_request_ka10050(
            ...     stk_cd="57JBHH"  # ELW 종목코드
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10050",
        }

        data = {
            "stk_cd": stk_cd,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def elw_price_spike_request_ka30001(
        self,
        flu_tp: str,
        tm_tp: str,
        tm: str,
        trde_qty_tp: str,
        isscomp_cd: str,
        bsis_aset_cd: str,
        rght_tp: str,
        lpcd: str,
        trde_end_elwskip: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """ELW 가격 급등락 정보를 조회합니다.

        Args:
            flu_tp (str): 등락구분 (1:급등, 2:급락)
            tm_tp (str): 시간구분 (1:분전, 2:일전)
            tm (str): 시간 (분 혹은 일입력, 예: 1, 3, 5)
            trde_qty_tp (str): 거래량구분
                - 0: 전체
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
                - 300: 30만주이상
                - 500: 50만주이상
                - 1000: 백만주이상
            isscomp_cd (str): 발행사코드
                - 000000000000: 전체
                - 3: 한국투자증권
                - 5: 미래대우
                - 6: 신영
                - 12: NK투자증권
                - 17: KB증권
            bsis_aset_cd (str): 기초자산코드
                - 000000000000: 전체
                - 201: KOSPI200
                - 150: KOSDAQ150
                - 005930: 삼성전자
                - 030200: KT
            rght_tp (str): 권리구분
                - 000: 전체
                - 001: 콜
                - 002: 풋
                - 003: DC
                - 004: DP
                - 005: EX
                - 006: 조기종료콜
                - 007: 조기종료풋
            lpcd (str): LP코드
                - 000000000000: 전체
                - 3: 한국투자증권
                - 5: 미래대우
                - 6: 신영
                - 12: NK투자증권
                - 17: KB증권
            trde_end_elwskip (str): 거래종료ELW제외 (0:포함, 1:제외)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: ELW 가격 급등락 데이터
                {
                    "base_pric_tm": str,  # 기준가시간
                    "elwpric_jmpflu": [  # ELW가격급등락
                        {
                            "stk_cd": str,  # 종목코드
                            "rank": str,  # 순위
                            "stk_nm": str,  # 종목명
                            "pre_sig": str,  # 대비기호
                            "pred_pre": str,  # 전일대비
                            "trde_end_elwbase_pric": str,  # 거래종료ELW기준가
                            "cur_prc": str,  # 현재가
                            "base_pre": str,  # 기준대비
                            "trde_qty": str,  # 거래량
                            "jmp_rt": str,  # 급등율
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Raises:
            ValueError: 필수 파라미터가 누락되었거나 유효하지 않은 경우

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.elw.elw_price_spike_request_ka30001(
            ...     flu_tp="1",  # 급등
            ...     tm_tp="2",  # 일전
            ...     tm="1",  # 1일
            ...     trde_qty_tp="0",  # 전체
            ...     isscomp_cd="000000000000",  # 전체
            ...     bsis_aset_cd="000000000000",  # 전체
            ...     rght_tp="000",  # 전체
            ...     lpcd="000000000000",  # 전체
            ...     trde_end_elwskip="0"  # 포함
            ... )
        """
        # 파라미터 유효성 검증
        if flu_tp not in ["1", "2"]:
            raise ValueError("flu_tp must be '1' (급등) or '2' (급락)")
        if tm_tp not in ["1", "2"]:
            raise ValueError("tm_tp must be '1' (분전) or '2' (일전)")
        if not tm.isdigit() or len(tm) > 2:
            raise ValueError("tm must be a 1-2 digit number")
        if trde_qty_tp not in ["0", "10", "50", "100", "300", "500", "1000"]:
            raise ValueError("Invalid trde_qty_tp value")
        if not isscomp_cd.isdigit() or len(isscomp_cd) != 12:
            raise ValueError("isscomp_cd must be a 12-digit number")
        if not bsis_aset_cd.isdigit() or len(bsis_aset_cd) != 12:
            raise ValueError("bsis_aset_cd must be a 12-digit number")
        if rght_tp not in ["000", "001", "002", "003", "004", "005", "006", "007"]:
            raise ValueError("Invalid rght_tp value")
        if not lpcd.isdigit() or len(lpcd) != 12:
            raise ValueError("lpcd must be a 12-digit number")
        if trde_end_elwskip not in ["0", "1"]:
            raise ValueError("trde_end_elwskip must be '0' (포함) or '1' (제외)")

        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka30001",
        }

        data = {
            "flu_tp": flu_tp,
            "tm_tp": tm_tp,
            "tm": tm,
            "trde_qty_tp": trde_qty_tp,
            "isscomp_cd": isscomp_cd,
            "bsis_aset_cd": bsis_aset_cd,
            "rght_tp": rght_tp,
            "lpcd": lpcd,
            "trde_end_elwskip": trde_end_elwskip,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )