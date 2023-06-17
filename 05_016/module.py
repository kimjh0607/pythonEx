'''
python 자주 쓰이는 모듈
수학관련 math - fabs(), ceil(), floor(), trunc(), gcd(), factorial(), sqrt()
난수관련 random - randint(), sample()
시간관련 time
'''

'''
python 기본 내장함수
sum(), max(), min()
'''
listVar = [2, 5, 3.14, 58, 10, 2]
print(f'sum : {sum(listVar)}')
print(f'max : {max(listVar)}')
print(f'min : {min(listVar)}')

#pow(a,b) 거듭제곱
print(f'pow(10,3) : {pow(10,3)}')
#round(a,b) 반올림
print(f'3.141592 : {round(3.141592, 1)}')
print(f'3.141592 : {round(3.141592, 2)}')
print(f'3.141592 : {round(3.141592, 5)}')

import math

#math 절대값
print(f'\'-10의 절대값\' : {math.fabs(-10)}')

#math 올림
print(f'\'5.21\'의 올림 : {math.ceil(5.21)}')

#math 내림
print(f'\'5.21\'의 올림 : {math.floor(5.21)}')

#math 버림
print(f'\'5.21\'의 올림 : {math.trunc(5.21)}')

#math 최대공약수
print(f'\'14, 21\'의 최대공약수 : {math.gcd(14, 21)}')

#math 팩토리얼
print(f'\'5\'의 팩토리얼 : {math.factorial(5)}')

#math 제곱근
print(f'\'4\'의 제곱근 : {math.sqrt(4)}')

import time

lt = time.localtime()
print(f'localtime : {lt}')
print(f'localtime_mon : {lt.tm_mon}')
print(f'localtime_year : {lt.tm_year}')
print(f'localtime_mday : {lt.tm_mday}')
print(f'localtime_hour : {lt.tm_hour}')