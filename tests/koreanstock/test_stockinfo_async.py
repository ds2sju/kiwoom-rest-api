from dotenv import load_dotenv
import logging
from pytest_httpx import HTTPXMock
import pytest
import asyncio
import os

from kiwoom_rest_api.koreanstock.stockinfo import StockInfo
from kiwoom_rest_api.auth.token import TokenManager



# 비동기 방식 사용
async def get_stock_info():
    """실제 비동기 API 호출을 수행하는 함수"""

    # TokenManager 인스턴스 생성 (실제 키 사용)
    # base_url은 TokenManager 내부 또는 Config에서 가져오므로 명시적 전달 불필요할 수 있음
    token_manager = TokenManager()

    # StockInfo 인스턴스 생성 (비동기 모드 활성화)
    # 실제 키움 API URL 사용 확인
    stock_info_async = StockInfo(
        base_url="https://api.kiwoom.com", # 실제 API URL 확인
        token_manager=token_manager,
        use_async=True
    )

    print("실제 비동기 API 호출 시작: basic_stock_information_request_ka10001('005930')")
    try:
        # 실제 비동기 API 호출
        result = await stock_info_async.basic_stock_information_request_ka10001("005930")
        print("\n--- API 호출 결과 ---")
        print(result)
        print("--------------------")
    except Exception as e:
        print(f"\nAPI 호출 중 오류 발생: {type(e).__name__}")
        print(f"오류 메시지: {e}")
        # 상세 에러 로깅이 필요하면 여기서 추가


# 이 스크립트 파일을 직접 실행할 때 get_stock_info 함수를 실행
if __name__ == "__main__":
    load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

    print("스크립트 직접 실행 시작...")
    asyncio.run(get_stock_info())
    print("스크립트 실행 완료.")