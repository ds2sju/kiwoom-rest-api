import httpx
import asyncio
import inspect

async def check_httpx():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get('https://httpbin.org/get')
            print(f"Status Code: {response.status_code}")
            print(f"Type of response: {type(response)}")
            json_method = getattr(response, 'json', None)
            text_method = getattr(response, 'text', None)
            print(f"Type of response.json: {type(json_method)}")
            print(f"Type of response.text: {type(text_method)}")
            print(f"Is response.json a coroutine func? {inspect.iscoroutinefunction(json_method)}")
            print(f"Is response.text a coroutine func? {inspect.iscoroutinefunction(text_method)}")

            # 실제 호출 시도
            try:
                data = await response.json()
                print("await response.json() succeeded.")
            except Exception as e_json:
                print(f"await response.json() failed: {e_json}")

            try:
                text = await response.text()
                print("await response.text() succeeded.")
            except Exception as e_text:
                print(f"await response.text() failed: {e_text}")

        except Exception as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    asyncio.run(check_httpx())