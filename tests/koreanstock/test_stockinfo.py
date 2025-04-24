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
    ka10002_result = stock_info.stock_price_request_ka10002("005930")
    
    if isinstance(ka10001_result, dict):
        print("\n\n\nka10001_result 응답:\n", json.dumps(ka10001_result, indent=4, ensure_ascii=False))
    else:
        print("\n\n\nka10001_result is not a dictionary.")
        
    if isinstance(ka10002_result, dict):
        print("\n\n\nka10002_result 응답:\n", json.dumps(ka10002_result, indent=4, ensure_ascii=False))
    else:
        print("\n\n\nka10002_result is not a dictionary.")
except Exception as e:
    print("에러 발생:", str(e))
