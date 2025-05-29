from dotenv import load_dotenv
import json
# import logging


# # 로깅 설정
# logging.basicConfig(level=logging.DEBUG)
# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.chart import Chart
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# Chart 인스턴스 생성 (base_url 수정)
chart = Chart(base_url="https://api.kiwoom.com", token_manager=token_manager)

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
    
    print_result("ka10060_result", chart.stockwise_investor_institution_chart_request_ka10060(
        dt="20241107",  # 일자 YYYYMMDD
        stk_cd="005930",  # 종목코드
        amt_qty_tp="1",  # 금액수량구분 1:금액, 2:수량
        trde_tp="0",  # 매매구분 0:순매수, 1:매수, 2:매도
        unit_tp="1000"  # 단위구분 1000:천주, 1:단주
    ), print_result=False)

    print_result("ka10064_result", chart.intraday_investor_trading_chart_request_ka10064(
        mrkt_tp="000",
        amt_qty_tp="1",
        trde_tp="0",
        stk_cd="005930"
    ), print_result=False)

    print_result("ka10079_result", chart.stock_tick_chart_request_ka10079(
        stk_cd="005930",  # 종목코드
        tic_scope="1",    # 틱범위 (1:1틱)
        upd_stkpc_tp="1"  # 수정주가구분
    ), print_result=False)

except Exception as e:
    print("에러 발생:", str(e))



