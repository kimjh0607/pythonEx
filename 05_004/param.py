'''
매개변수 - 인수를 받을 변수형태(변수의 일종)
인수 - 함수에 들어가는 데이터
인수와 매개변수는 각 갯수가 일치해야한다.(짝이 맞아야 한다)
매개변수 개수가 정해지지 않은 경우 '*'를 이용한다.
'''

def greet(customer):
    print(f'{customer} Hi~')

greet('Hong')

def cal(n1, n2):
    print(f'{n1} + {n2} = {n1 + n2}')
    print(f'{n1} - {n2} = {n1 - n2}')
    print(f'{n1} * {n2} = {n1 * n2}')
    print(f'{n1} / {n2} = {n1 / n2}')

cal(10,20)

def printNumber(*numbers): #*numbers 의 타입은 튜플이다.
    for number in numbers:
        print(number, end='')
    print()

printNumber(10, 20, 30, 40)

#실습
def printScore(kor, eng, math):
    sum = kor + eng + math
    avg = sum / 3

    print(f'sum : {sum}')
    print(f'avg : {avg}')

korScore = int(input('enter korean Score : '))
engScore = int(input('enter english Score : '))
mathScore = int(input('enter math Score : '))

printScore(korScore, engScore, mathScore)