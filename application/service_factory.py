from abc import ABC, abstractmethod


class IServiceFactory(ABC):
    @abstractmethod
    def create_service(self):
        pass
