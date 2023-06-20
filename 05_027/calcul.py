from abc import ABCMeta
from abc import abstractmethod

class Calculator(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass

class DevCal(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

    def mod(self, n1, n2):
        print(n1 % n2)

    def flo(self, n1, n2):
        print(n1 // n2)

cal = DevCal()
cal.mul(10, 20)
cal.sub(10, 20)
cal.flo(10, 20)
cal.div(10, 20)