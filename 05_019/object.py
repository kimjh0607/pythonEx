'''
객체 속성 변경
'''
class NewGenerationPC:

    def __init__(self, name, cpu, memory, ssd):
        self.name = name # 앞의 name은 NewGenerationPC클래스로부터 만들어질 객체의 속성, 뒤의 name은 매개변수
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print('Excel Run!!')

    def doPhotoshop(self):
        print('Photoshop Run!!')

    def Info(self):
        print(f'name : {self.name}')
        print(f'cpu : {self.cpu}')
        print(f'memory : {self.memory}')
        print(f'ssd : {self.ssd}')

myPC = NewGenerationPC('myPc', 'i5', '16G', '256G')
myPC.Info()

friendPC = NewGenerationPC('friendPc', 'i7', '32G', '512G')
myPC.Info()

myPC.cpu = 'i9' # 속성에 접근, 변경 '.'(접근 연산자)
myPC.memory = '64G'
myPC.ssd = '1T'
myPC.Info()

#실습
class Calculator:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def add(self):
        self.result = self.num1 + self.num2
        return self.result

    def sub(self):
        self.result = self.num1 - self.num2
        return self.result

    def mul(self):
        self.result = self.num1 * self.num2
        return self.result

    def div(self):
        self.result = self.num1 / self.num2
        return self.result

calculator = Calculator()
calculator.num1 = 10
calculator.num2 = 20
print(f'10, 20을 대입 : {calculator.add()}')
print(f'10, 20을 대입 : {calculator.sub()}')
print(f'10, 20을 대입 : {calculator.mul()}')
print(f'10, 20을 대입 : {calculator.div()}')

calculator.num1 = 3
calculator.num2 = 5
print(f'10, 20을 대입 : {calculator.add()}')
print(f'10, 20을 대입 : {calculator.sub()}')
print(f'10, 20을 대입 : {calculator.mul()}')
print(f'10, 20을 대입 : {calculator.div()}')

