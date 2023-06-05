'''
operator Module
+ - add()
- - sub()
* - mul()
/ - truediv()
% - mod() 나머지
// - floordiv() 몫
** - pow()
'''

import operator #operator 모듈 가져오기
n1 = 8
n2 = 3
print('{} + {} = {}'.format(n1, n2, (operator.add(n1,n2))))
print('{} - {} = {}'.format(n1, n2, (operator.sub(n1,n2))))
print('{} * {} = {}'.format(n1, n2, (operator.mul(n1,n2))))
print('{} / {} = {}'.format(n1, n2, (operator.truediv(n1,n2))))
print('{} % {} = {}'.format(n1, n2, (operator.mod(n1,n2))))
print('{} // {} = {}'.format(n1, n2, (operator.floordiv(n1,n2))))
print('{} ** {} = {}'.format(n1, n2, (operator.pow(n1,n2))))

print('{} == {} = {}'.format(n1, n2, (operator.eq(n1,n2)))) #==
print('{} != {} = {}'.format(n1, n2, (operator.ne(n1,n2)))) #!=
print('{} > {} = {}'.format(n1, n2, (operator.gt(n1,n2)))) #>
print('{} >= {} = {}'.format(n1, n2, (operator.ge(n1,n2)))) #>=
print('{} < {} = {}'.format(n1, n2, (operator.lt(n1,n2)))) #<
print('{} <= {} = {}'.format(n1, n2, (operator.le(n1,n2)))) #<=

flag1 = True
flag2 = False
print('{} and {} : {}'.format(flag1, flag2, (operator.and_(flag1,flag2))))
print('{} or {} : {}'.format(flag1, flag2, (operator.or_(flag1,flag2))))
print('not {} : {}'.format(flag1, flag2, (operator.not_(flag1))))

#실습
age = int(input('나이 입력 : '))
vac = operator.or_(operator.lt(age, 20), operator.ge(age, 65))
#or_() 함수 안에 두가지 조건을 넣음. 둘중 하나만 참이면 참.
print('age : {} / 대상자 : {}'.format(age, vac))

#10~100사이의 난수중 십의 자리와 일의 자리가 각각 3의 배수인지 판단하는 코드
import random
#1
ran = random.randint(10,100)
print(ran)
t = operator.floordiv(ran, 10)
o = operator.mod(ran, 10)
print(t)
print(o)
print(f'10의 자리는 3의 배수인가? {t%3==0}')
print(f'1의 자리는 3의 배수인가? {o%3==0}')

#2
int = random.randint(10,100)
print(int)
divint = divmod(int, 10)
#10의 자리
tens = divint[0]
print(tens)
#1의자리
ones = divint[1]
print(ones)
#3의 배수인지 판단
print(f'10의 자리는 3의 배수 {tens%3==0}, 1의 자리는 3의 배수 {ones%3==0}')