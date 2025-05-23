from dotenv import load_dotenv
import json
# import logging


# # 로깅 설정
# logging.basicConfig(level=logging.DEBUG)
# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.elw import ELW
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# StockInfo 인스턴스 생성 (base_url 수정)
elw = ELW(base_url="https://api.kiwoom.com", token_manager=token_manager)

def print_result(result_name, result, print_result):
    if isinstance(result, dict):
        if str(result.get("return_code")) == "0":
            if print_result:
                print(f"{result_name} 응답:\n", json.dumps(result, indent=4, ensure_ascii=False))
            else:
                print(f"{result_name} 응답: 성공")
        else:
            print(f"{result_name} 응답: 실패\n", json.dumps(result, indent=4, ensure_ascii=False))
    else:
        print(f"{result_name} is not a dictionary.")


try:
    print("\n\n test 실행")
    
    print_result("ka10048_result", elw.elw_daily_sensitivity_indicator_request_ka10048(
        stk_cd="57KBAW"
    ), print_result=False)
    
    print_result("ka10050_result", elw.elw_sensitivity_indicator_request_ka10050(
        stk_cd="57KBAW"
    ), print_result=False)
    
    print_result("ka30001_result", elw.elw_price_spike_request_ka30001(
        flu_tp="1",  # 급등
        tm_tp="2",  # 일전
        tm="1",  # 1일
        trde_qty_tp="0",  # 전체
        isscomp_cd="000000000000",  # 전체
        bsis_aset_cd="000000000000",  # 전체
        rght_tp="000",  # 전체
        lpcd="000000000000",  # 전체
        trde_end_elwskip="0"  # 포함
    ), print_result=False)

except Exception as e:
    print("에러 발생:", str(e))



