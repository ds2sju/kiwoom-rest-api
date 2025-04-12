# Kiwoom REST API

Python client for interacting with Kiwoom Securities REST API.

## Installation

```bash
pip install kiwoom-rest-api
```

## Usage

```python
from kiwoom_rest_api.api import KiwoomAPI

api = KiwoomAPI()
result = api.get_basic_stock_info("005930")
print(result)
```

## CLI Usage

```bash
kiwoom --help
```

## License

This project is licensed under the terms of the MIT license.
