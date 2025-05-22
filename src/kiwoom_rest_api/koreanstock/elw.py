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