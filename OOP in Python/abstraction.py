# abstraction means hidden

from abc import ABC, abstractmethod

class BankApp(ABC):
    def database(self):
        print("connected to database")

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):

    def mobileLogin(self):
        print("login into mobile")

    def security(self):
        print("secured")


mob = MobileApp()

mob.database()


