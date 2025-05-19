from dotenv import load_dotenv
import json

# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.rank_info import RankInfo
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# RankInfo 인스턴스 생성
rank_info = RankInfo(base_url="https://api.kiwoom.com", token_manager=token_manager)

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
    
    print_result("ka10020_result", rank_info.top_order_book_volume_request_ka10020(
        mrkt_tp="001",  # 코스피
        sort_tp="1",  # 순매수잔량순
        trde_qty_tp="0000",  # 장시작전(0주이상)
        stk_cnd="0",  # 전체조회
        crd_cnd="0",  # 전체조회
        stex_tp="1"  # KRX
    ), print_result=False)
    
    print_result("ka10021_result", rank_info.sudden_increase_order_book_volume_request_ka10021(
        mrkt_tp="001",  # 코스피
        trde_tp="1",  # 매수잔량
        sort_tp="1",  # 급증량
        tm_tp="30",  # 30분
        trde_qty_tp="1",  # 천주이상
        stk_cnd="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10022_result", rank_info.sudden_increase_order_ratio_request_ka10022(
        mrkt_tp="001",  # 코스피
        rt_tp="1",  # 매수/매도비율
        tm_tp="1",  # 1분
        trde_qty_tp="5",  # 5천주이상
        stk_cnd="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10023_result", rank_info.sudden_increase_trading_volume_request_ka10023(
        mrkt_tp="000",  # 전체
        sort_tp="1",  # 급증량
        tm_tp="2",  # 전일
        trde_qty_tp="5",  # 5천주이상
        stk_cnd="0",  # 전체조회
        pric_tp="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)

except Exception as e:
    print("에러 발생:", str(e)) 