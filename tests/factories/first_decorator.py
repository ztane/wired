"""
Handle simple case with a decorator.
"""

from wired import ServiceRegistry, wired_factory


@wired_factory
class LoginService:
    def __init__(self):
        ...


registry = ServiceRegistry()
