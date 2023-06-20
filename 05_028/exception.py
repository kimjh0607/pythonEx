'''
예외란? 예상하지 못한 문제로 프로그램 실행이 어려운 상태
문법적인 문제는 없으나 실행 중 발생하는 예상하지 못한 문제이다.

에러와 예외는 다름.
에러 - 소프트웨어적으로 해결할 수 없는 - syntax error, network error
예외 - 문법적인 오류는 없으나 예상할 수 없는.

Exception이 예외의 최상의 클래스
'''


def add(n1, n2):
    print(n1 + n2)

def sub(n1, n2):
    print(n1 - n2)

def mul(n1, n2):
    print(n1 * n2)

def div(n1, n2):
    print(n1 / n2)

num1 = int(input('first number : '))
num2 = int(input('second number : '))

add(num1, num2)
sub(num1, num2)
mul(num1, num2)
div(num1, num2)

