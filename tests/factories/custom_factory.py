"""
Class with a __wired_factory class method but registered imperatively.

This method gets passed the container and returns a constructed instance.
"""

from wired import wired_factory, ServiceContainer, ServiceRegistry


@wired_factory()
class Customer:
    def __init__(self):
        self.name = 'Some Customer'


class LoginService:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def __wired_factory__(cls, container: ServiceContainer):
        customer: Customer = container.get(Customer)
        return cls(customer_name=customer.name)


registry = ServiceRegistry()
registry.register_service(LoginService)