# Purpose: concrete application class
from ..application.abstract_application import AbstractApplication


class MyApplication(AbstractApplication):
    def run(self):
        print("MyApplication.run()")
        self.service.do_something()
