"""

A custom add-on to our app which adds FrenchCustomer and
French Greeter.

"""
from dataclasses import dataclass

from wired import ServiceRegistry, ServiceContainer
from .models import Customer, Greeter, Datastore
from .utils import register_dataclass


@dataclass
class FrenchCustomer(Customer):
    pass


@dataclass
class FrenchGreeter(Greeter):
    greeting: str = 'Bonjour'


def setup(registry: ServiceRegistry, container: ServiceContainer):
    register_dataclass(
        registry, container,
        FrenchGreeter, Greeter,
        context=FrenchCustomer
    )

    # Grab the Datastore and add a FrenchCustomer
    datastore: Datastore = container.get(Datastore)
    henri = FrenchCustomer(name='henri', title='Henri')
    datastore.customers['henri'] = henri
