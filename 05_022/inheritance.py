'''
상속
클래스는 또 다른 클래스를 상속해서 내 것처럼 사용할 수 있다.
상속받을 클래스는 클래스이름 옆에 클래스명뒤에 '(상속해주는 클래스)' 를 붙인다.
'''
class NormalCar:

    def drive(self):
        print('normalCar drive() called!!')

    def back(self):
        print('normalCar back() called!!')

class TurboCar(NormalCar): #상속문법확인.

    def turbo(self):
        print('turboCar turbo() called!!')

myTurboCar = TurboCar()

myTurboCar.turbo()
myTurboCar.drive()
myTurboCar.back()

#실습
class CalSuper:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

class CalChild(CalSuper):

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

calchild = CalChild()
print(f'cal add : {calchild.add(10,20)}') #상속
print(f'cal sub : {calchild.sub(10,20)}') #상속
print(f'cal mul : {calchild.mul(10,20)}')
print(f'cal div : {calchild.div(10,20)}')