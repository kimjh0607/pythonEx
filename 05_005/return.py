'''
함수 실행 결과 반환
return 키워드 - 함수 '실행 결과를 호출부로 반환'할 수 있다.
반환만으로는 출력이 안된다. print()로 감싸주던지, 변수에 할당해서 그 변수를 출력하면된다
return 으로 데이터를 반환해주고 나면, 그 이후에 실행문은 실행되지않는다.(실행종료)
'''

def cal(n1,n2):
    result = n1 + n2
    return result

returnValue = cal(20,10)
print(returnValue)
print(cal(10,10))

def divide(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

    print('이것이 출력이 될까?') #return은 다음을 실행하지 않는다.

returnValue = divide(5)
print(f'return value is : {returnValue}')

#실습 - cm를 mm로
def cm(a):
    mm = a*10
    return mm

length = float(input('enter cm : '))
value = cm(length)
print(f'{length}cm -> {value}mm')

#실습 - 1~100정수 중 홀수인 난수를 반환
import random

def getOddNum():
    while True:
        n = random.randint(1,100)
        if n % 2 != 0:
            break
    return n
print(f'number is {getOddNum()}') # - 1함수 호출을 바로때리거나, 2변수에 담아서 프린트 하거나..