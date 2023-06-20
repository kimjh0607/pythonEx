'''
다중상속 2개 이상의 클래스를 상속
다중상속을 너무 남발하면 안된다.
'''

class Car01:

    def drive(self):
        print('drive() method called!!')

class Car02:

    def turbo(self):
        print('turbo() method called!!')

class Car03:

    def fly(self):
        print('fly() method called!!')

class Car(Car01, Car02, Car03):
    def __init__(self):
        pass

# myCar = Car()
# myCar.drive()
# myCar.turbo()
# myCar.fly()

class BasicCal:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2


class DevCal:

    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

class Calculator(BasicCal, DevCal):
    def __init__(self):
        pass

cal1 = Calculator()
print(f'mod - {cal1.mod(10,3)}')
print(f'exp - {cal1.exp(10,3)}')
print(f'flo - {cal1.flo(10,3)}')
print(f'div - {cal1.div(10,3)}')