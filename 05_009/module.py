'''
모듈이란 이미 만들어진 훌륭한 기능으로 사용자는 쉽게 사용할 수 있다.
ex)계산모듈, 난수모듈, 날짜/시간모듈 => 사용자는 내것처럼 사용할 수 있다.
내부(내장)모듈 / 외부모듈 / 사용자모듈 정도로 구분
내부 - 파이썬 설치 시 기본적으로 사용할 수 있는 모듈
외부 - numPy, Pandas처럼 별도 설치 후 사용할 수 있는 모듈
'''

#random 모듈 - 1~10까지 정수중 난수 1개발생
import random
rNum = random.randint(1, 10)
print(f'random number : {rNum}')

#random 모듈 - 1~100까지 정수중 난수 10개발생
rNums = random.sample(range(1, 101), 10) # 값이 여러개인 'List' type 으로 반환
print(f'random number : {rNums}')


