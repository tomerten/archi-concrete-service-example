from abc import ABC, abstractmethod


class IService(ABC):
    @abstractmethod
    def do_something(self):
        pass
