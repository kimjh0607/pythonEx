'''
site-packages 에 저장하면 어디서나 쓸 수 있는 범용 모듈을 만들 수 있다.
어느 프로젝트 에서든 (독립된 가상환경을 넘어서 범용성있게)
'''

#파이썬 제공 모듈 중, sys 모듈 - system에 대한 정보를 갖고있는 모듈
# import sys
#
# for path in sys.path:
#     print(path)

from calculator import cal
print(f'cal.add(10, 20) : {cal.add(10, 20)}')
print(f'cal.add(10, 20) : {cal.sub(10, 20)}')
print(f'cal.add(10, 20) : {cal.mul(10, 20)}')
print(f'cal.add(10, 20) : {cal.div(10, 20)}')

print('-' * 30)
from divisor_pac import divisor_mod as dm

print(f'10의 약수 : {dm.divisor(10)}')
print(f'50까지의 소수 : {dm.prime_number(50)}')