'''
호출하기
호출 후 다음실행문 실행.
함수 내 또다른 함수 호출
'''
# def fun1():
#     print('function1 호출!!')
#     fun2()
#     print('function2 실행 후 호출')
#
# def fun2():
#     print('function2 호출!!')
#     fun3()
#
# def fun3():
#     print('function3 호출!!')
#
# fun1()

# def printTodayWeather():
#     print('today is sunny') #실행문 없으면 Error , pass 키워드를 쓸 수 있다.
#
# printTodayWeather()

def guguDan2():
    for i in range(1, 10):
        print('2 * {} = {}'.format(i, 2 * i))
    guguDan3()
def guguDan3():
    for i in range(1, 10):
        print('3 * {} = {}'.format(i, 3 * i))
    guguDan4()
def guguDan4():
    for i in range(1, 10):
        print('4 * {} = {}'.format(i, 4 * i))

guguDan2()
