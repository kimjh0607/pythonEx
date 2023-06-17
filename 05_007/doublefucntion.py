'''
중첩함수 - 함수안에 또 다른 함수를 선언
 내부 함수를 함수 밖에서 호출할 수 없다.
'''
def out_function():
    print('out function called!')

    def in_function(): #out_function()에 귀속되어 있는 중첩함수
        print('in function called!')

    in_function()

out_function()

#in_function()
# -> 내부함수를 밖에서 호출할 수 없다. - NameError : name 'in_function' is not defined

#실습
def calculator(a, b, operator):

    def add():
        print(f'add oper : {a + b}')

    def sub():
        print(f'add oper : {a - b}')

    def mul():
        print(f'add oper : {a * b}')

    def div():
        print(f'add oper : {a / b}')

    if operator == 1:
        add()
    elif operator == 2:
        sub()
    elif operator == 3:
        mul()
    elif operator == 4:
        div()

while True:
    a = float(input('enter float a : '))
    b = float(input('enter float b : '))
    operatorNum = int(input('1.add 2.sub 3.mul 4.div 5.exit'))

    if operatorNum == 5:
        print('Bye')
        break

    calculator(a, b, operatorNum)

calculator(10, 10, 1)
calculator(10, 10, 2)
calculator(10, 10, 3)
calculator(10, 10, 4)