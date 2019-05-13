# app.py
from app import App
from configure import register
from request import process_request


def test_greeter():
    # start-after
    # Application starts up
    app = App()
    register(app.registry)
    # Later, a request comes in
    result = process_request(app.registry)
    assert 'Hello Larry my name is Mary' == result
