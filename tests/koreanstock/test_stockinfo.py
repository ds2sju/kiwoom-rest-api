from kiwoom_rest_api.koreanstock.stockinfo import StockInfo
from kiwoom_rest_api.auth.token import TokenManager

# 테스트용 토큰 매니저 생성
token_manager = TokenManager()

# 동기 방식 사용
stock_info = StockInfo(base_url="https://api.kiwoom.com", token_manager=token_manager)
result = stock_info.basic_stock_information_request_ka10001("005930")
print(result)

# 비동기 방식 사용
async def get_stock_info():
    stock_info_async = StockInfo(base_url="https://api.kiwoom.com", token_manager=token_manager, use_async=True)
    result = await stock_info_async.basic_stock_information_request_ka10001("005930")
    print(result)

import asyncio
asyncio.run(get_stock_info())