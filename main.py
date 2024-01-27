# Purpose: main program
from concrete.my_application import MyApplication
from concrete.concrete_service_factory import ConcreteServiceFactory

if __name__ == "__main__":
    service_factory = ConcreteServiceFactory()
    app = MyApplication(service_factory)
    app.run()
