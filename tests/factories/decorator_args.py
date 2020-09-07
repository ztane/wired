"""
Decorator to override built-in registered service.
"""

from wired import wired_factory


class LoginService:
    """ Generic for any context """

    def __init__(self):
        ...


@wired_factory(for_=LoginService)
class CustomLoginService:
    """ Override the default LoginService """

    def __init__(self):
        ...