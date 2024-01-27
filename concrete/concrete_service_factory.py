# Purpose: Concrete service factory class
from ..application.service_factory import IServiceFactory
from .concrete_service import ConcreteService


class ConcreteServiceFactory(IServiceFactory):
    def create_service(self):
        return ConcreteService()
