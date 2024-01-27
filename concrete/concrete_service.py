# Purpose: Concrete service class
from ..application.service import IService


class ConcreteService(IService):
    def do_something(self):
        print("Concrete service is doing something")
