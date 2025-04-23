from dotenv import load_dotenv
import logging


# 로깅 설정
logging.basicConfig(level=logging.DEBUG)
# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.stockinfo import StockInfo
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()
print(f"\n\n★@token_manager: {token_manager}\n\n")
# StockInfo 인스턴스 생성 (base_url 수정)
stock_info = StockInfo(base_url="https://api.kiwoom.com", token_manager=token_manager)

try:
    result = stock_info.basic_stock_information_request_ka10001("005930")
    print("API 응답:", result)
except Exception as e:
    print("에러 발생:", str(e))
