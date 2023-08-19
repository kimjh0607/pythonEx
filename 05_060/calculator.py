
def add(n1, n2):
    try:
        n1 = int(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = int(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} + {n2} = {n1+n2}')

def sub(n1, n2):
    try:
        n1 = int(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = int(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} - {n2} = {n1-n2}')

def mul(n1, n2):
    try:
        n1 = int(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = int(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} * {n2} = {n1*n2}')

def div(n1, n2):
    try:
        n1 = int(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = int(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return
    
    try:
        print(f'{n1} / {n2} = {n1/n2}')
    except ZeroDivisionError as e:
        print(e)
        print(f'0으로 나눌 수 없습니다.')

def mod(n1, n2):
    try:
        n1 = int(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = int(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return
    
    try:
        print(f'{n1} % {n2} = {n1%n2}')
    except ZeroDivisionError as e:
        print(e)
        print(f'0으로 나눌 수 없습니다.')

def flo(n1, n2):
    try:
        n1 = int(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = int(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        print(f'{n1} // {n2} = {n1//n2}')
    except ZeroDivisionError as e:
        print(e)
        print(f'0으로 나눌 수 없습니다.')

def exp(n1, n2):
    try:
        n1 = int(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return

    try:
        n2 = int(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{n1} ** {n2} = {n1**n2}')
