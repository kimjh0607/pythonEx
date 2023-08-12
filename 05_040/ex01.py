

def add(a,b):
    print(f'{a} + {b} = {a+b}')

def sub(a,b):
    print(f'{a} - {b} = {a-b}')

def mul(a,b):
    print(f'{a} * {b} = {a*b}')

def div(a,b):
    print(f'{a} / {b} = {a/b}')

def mod(a,b):
    print(f'{a} % {b} = {a%b}')

def flo(a,b):
    print(f'{a} // {b} = {a//b}')

def exp(a,b):
    print(f'{a} ** {b} = {a**b}')

while True:
    print('-'*60)
    choice = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.나머지, 6.몫, 7.제곱승, 8.종료'))
    if choice ==8 :
        print('Bye')
        break

    a = int(input('첫 번째 숫자 입력 : '))
    b = int(input('두 번째 숫자 입력 : '))
    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mul(a, b)
    elif choice == 4:
        div(a, b)
    elif choice == 5:
        mod(a, b)
    elif choice == 6:
        flo(a, b)
    elif choice == 7:
        exp(a, b)
