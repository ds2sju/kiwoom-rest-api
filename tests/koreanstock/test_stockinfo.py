from dotenv import load_dotenv
import json
# import logging


# # 로깅 설정
# logging.basicConfig(level=logging.DEBUG)
# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.stockinfo import StockInfo
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# StockInfo 인스턴스 생성 (base_url 수정)
stock_info = StockInfo(base_url="https://api.kiwoom.com", token_manager=token_manager)

try:
    ka10001_result = stock_info.basic_stock_information_request_ka10001("005930")
    ka10002_result = stock_info.stock_trading_agent_request_ka10002("005930")
    ka10003_result = stock_info.daily_stock_price_request_ka10003("005930")
    ka10013_result = stock_info.credit_trading_trend_request_ka10013("005930", "20241101", "1")
    ka10015_result = stock_info.daily_transaction_details_request_ka10015("005930", "20241101")
    ka10016_result = stock_info.reported_low_price_request_ka10016("000", "1", "1", "0", "00000", "0", "0", "5", "1")
    ka10017_result = stock_info.upper_lower_limit_price_request_ka10017("000", "1", "1", "0", "00000", "0", "0", "5", "1")
    ka10018_result = stock_info.near_high_low_price_request_ka10018("000", "1", "1", "0", "00000", "0", "0", "5", "1")
    ka10019_result = stock_info.rapid_price_change_request_ka10019("000", "1", "1", "0", "00000", "0", "0", "5", "0", "1")
    ka10024_result = stock_info.trading_volume_update_request_ka10024("000", "5", "5", "1")
    
    # 50% 이상 매물이 집중된 종목 조회 (50일 주기)
    ka10025_result = stock_info.supply_concentration_request_ka10025(
        market_type="000",               # 전체 시장
        supply_concentration_rate="50",  # 50% 이상 집중
        current_price_entry="0",         # 현재가 매물대 진입 포함안함
        supply_count="10",               # 매물대수 10개
        cycle_type="50",                 # 50일 주기
        stock_exchange_type="3"          # 통합 거래소
    )
    # 저PBR 종목 조회
    ka10026_result = stock_info.high_low_per_request_ka10026(
        per_type="1",                # 1: 저PBR
        stock_exchange_type="3"      # 통합 거래소
    )

    
        
        
    
    
    print("\n\n")
    
    if isinstance(ka10001_result, dict):
        if str(ka10001_result.get("return_code")) == "0":
            print("ka10001_result 응답: 성공")
        else:
            print("ka10001_result 응답: 실패")
        # print("ka10001_result 응답:\n", json.dumps(ka10001_result, indent=4, ensure_ascii=False))
    else:
        print("ka10001_result is not a dictionary.")
        
    if isinstance(ka10002_result, dict):
        if str(ka10002_result.get("return_code")) == "0":
            print("ka10002_result 응답: 성공")
        else:
            print("ka10002_result 응답: 실패")
        # print("ka10002_result 응답:\n", json.dumps(ka10002_result, indent=4, ensure_ascii=False))
    else:
        print("ka10002_result is not a dictionary.")
    
    if isinstance(ka10003_result, dict):
        if str(ka10003_result.get("return_code")) == "0":
            print("ka10003_result 응답: 성공")
        else:
            print("ka10003_result 응답: 실패")
        # print("ka10003_result 응답:\n", json.dumps(ka10003_result, indent=4, ensure_ascii=False))
    else:
        print("ka10003_result is not a dictionary.")
        
    if isinstance(ka10013_result, dict):
        if str(ka10013_result.get("return_code")) == "0":
            print("ka10013_result 응답: 성공")
        else:
            print("ka10013_result 응답: 실패")
        # print("ka10013_result 응답:\n", json.dumps(ka10013_result, indent=4, ensure_ascii=False))
        
    if isinstance(ka10015_result, dict):
        if str(ka10015_result.get("return_code")) == "0":
            print("ka10015_result 응답: 성공")
        else:
            print("ka10015_result 응답: 실패")
        # print("ka10015_result 응답:\n", json.dumps(ka10015_result, indent=4, ensure_ascii=False))
    else:
        print("ka10015_result is not a dictionary.")
        
    if isinstance(ka10016_result, dict):
        if str(ka10016_result.get("return_code")) == "0":
            print("ka10016_result 응답: 성공")
        else:
            print("ka10016_result 응답: 실패")
        # print("ka10016_result 응답:\n", json.dumps(ka10016_result, indent=4, ensure_ascii=False))
    else:
        print("ka10016_result is not a dictionary.")
    
    if isinstance(ka10017_result, dict):
        if str(ka10017_result.get("return_code")) == "0":
            print("ka10017_result 응답: 성공")
        else:
            print("ka10017_result 응답: 실패")
        # print("ka10017_result 응답:\n", json.dumps(ka10017_result, indent=4, ensure_ascii=False))
    else:
        print("ka10017_result is not a dictionary.")
        
    if isinstance(ka10018_result, dict):
        if str(ka10018_result.get("return_code")) == "0":
            print("ka10018_result 응답: 성공")
        else:
            print("ka10018_result 응답: 실패")
        # print("ka10018_result 응답:\n", json.dumps(ka10018_result, indent=4, ensure_ascii=False))
    else:
        print("ka10018_result is not a dictionary.")
        
    if isinstance(ka10019_result, dict):
        if str(ka10019_result.get("return_code")) == "0":
            print("ka10019_result 응답: 성공")
        else:
            print("ka10019_result 응답: 실패")
        # print("ka10019_result 응답:\n", json.dumps(ka10019_result, indent=4, ensure_ascii=False))
    else:
        print("ka10019_result is not a dictionary.")
        
    if isinstance(ka10024_result, dict):
        if str(ka10024_result.get("return_code")) == "0":
            print("ka10024_result 응답: 성공")
        else:
            print("ka10024_result 응답: 실패")
        # print("ka10024_result 응답:\n", json.dumps(ka10024_result, indent=4, ensure_ascii=False))
    else:
        print("ka10024_result is not a dictionary.")
        
    if isinstance(ka10025_result, dict):
        if str(ka10025_result.get("return_code")) == "0":
            print("ka10025_result 응답: 성공")
        else:
            print("ka10025_result 응답: 실패")
        # print("ka10025_result 응답:\n", json.dumps(ka10025_result, indent=4, ensure_ascii=False))
    else:
        print("ka10025_result is not a dictionary.")
        
    if isinstance(ka10026_result, dict):
        if str(ka10026_result.get("return_code")) == "0":
            print("ka10026_result 응답: 성공")
        else:
            print("ka10026_result 응답: 실패")
        # print("ka10026_result 응답:\n", json.dumps(ka10026_result, indent=4, ensure_ascii=False))
    else:
        print("ka10026_result is not a dictionary.")
except Exception as e:
    print("에러 발생:", str(e))
