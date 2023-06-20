'''
상위클래스의 기능은 상속만하면 바로 쓸 수 있는데,
상위클래스의 속성은 '__init__' 메서드가 호출을 하여야 속성을 초기화 할 수 있다.
상위클래스의 '__init__' 메서드를 호출할 때는 1. 강제호출, 2. super()를 쓰면 된다.
'''
class Calculator:

    def __init__(self, n1, n2):
        print('[Calculator] __init__() called!!')
        self.num1 = n1
        self.num2 = n2

cal = Calculator(10, 20) #속성이 있을때, 생성자에 속성값을 넣어줘야한다. - 속성초기화.
print(f'num1 : {cal.num1}')
print(f'num2 : {cal.num2}')

class Pclass:

    def __init__(self, pn1, pn2):
        print('[Pclass] __init__() called!!')
        self.pn1 = pn1
        self.pn2 = pn2

class Cclass(Pclass):

    def __init__(self, cn1, cn2):
        print('[Cclass] __init__() called!!')
        self.cn1 = cn1
        self.cn2 = cn2

        #Pclass.__init__(self, cn1, cn2) #방법1, '부모클래스.생성자' 강제호출
        super().__init__(cn1, cn2) #방법2, 'super()' 이용

cls = Cclass(10, 20)

class Car:

    def __init__(self, color, type):
        self.color = color
        self.type = type

    def drive(self):
        print('Let\'s go!!!!')

    def reverse(self):
        print('Let\'s back~~~~')

class Suv(Car):

    def __init__(self, color, type):
        super().__init__(color, type)

suv1 = Suv('blue', 'benz')

print(f'color is {suv1.color}')
print(f'color is {suv1.type}')
suv1.drive()

