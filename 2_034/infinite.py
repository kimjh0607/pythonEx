'''
무한반복실행 -반복문을 빠져 나올 수 없는 경우, while문에서 조건식의 결과가 항상 True인 경우
논리형 데이터 사용
'''
n=1
while n < 10:
    print('hi')
    n+=1 #없으면 무한루프

flag = True
num = 0
sum = 0

while flag:
    num += 1
    sum += num
    print('{}까지의 합: {}'.format(num, sum))

    if sum >=1000:
        flag = False

#실습
'''
하루에 독감환자가 50-100명사이로 오는 병원이있다.
누적 환자수가 10000명이 넘는 날짜를 구하라
'''
import random
day = 0
sum = 0
#once = random.randint(50, 100)
#
# while sum<10000:
#     sum += once
#     day += 1
#
# print('{}째날 10000명 돌파'.format(day))

flag = True
while flag:
    once = random.randint(50, 100)
    sum += once
    day += 1
    print('{}째날 오늘{}명 누적{}명'.format(day,once,sum))

    if sum>10000:
        flag = False