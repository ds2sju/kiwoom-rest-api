# deploy

## prodution
```
    pip install kiwoom-rest-api
    uv add kiwoom-rest-api
```

### deploy to pypi [site](https://pypi.org/project/kiwoom-rest-api/)
```
    poetry shell
    poetry publish --build
```


## test
```
    pip install -i https://test.pypi.org/simple/ kiwoom-rest-api
```
```
    uv add -i https://test.pypi.org/simple/ kiwoom-rest-api
```

### deploy to test-pypi [site](https://test.pypi.org/project/kiwoom-rest-api/)
```
    poetry shell
    poetry publish --build -r test-pypi
```


# docs
[pypi-keys]()
