'''
선언 - def addCal() : #키워드, 함수명, ':', 들여쓰기
    (들여쓰기)실행부
호출 - 정의만 하면 함수를 쓰는 것이 X 호출을 해야 함.

선언부와 호출부 가 있다.
'''

# def add():
#     n1 = int(input('enter n1 : '))
#     n2 = int(input('enter n2 : '))
#     print(f'n1 + n2 = {n1 + n2}')
#
# add()
# add()
# add()
#
# def printWeatherInfo():
#     print('today is sunny')
#
# printWeatherInfo()
# printWeatherInfo()
# printWeatherInfo()

def calFun():
    n1 = int(input('enter n1 : '))
    n2 = int(input('enter n2 : '))

    print(f'n1 * n2 = {n1 * n2}')
    print(f'n1 / n2 = {round(n1 / n2 , 2)}') #round()함수 - 소수점 2번째까지

calFun()