# Purpose: Abstract Application class
from abc import ABC, abstractmethod
from .service_factory import IServiceFactory


class AbstractApplication(ABC):
    def __init__(self, service_factory: IServiceFactory):
        self.service = service_factory.create_service()

    @abstractmethod
    def run(self):
        pass
