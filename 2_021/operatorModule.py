'''
operator Module
'''
import operator
n1 = 8
n2 = 3
print('{} + {} = {}'.format(n1, n2, (operator.add(n1,n2))))
print('{} - {} = {}'.format(n1, n2, (operator.sub(n1,n2))))
print('{} * {} = {}'.format(n1, n2, (operator.mul(n1,n2))))
print('{} / {} = {}'.format(n1, n2, (operator.truediv(n1,n2))))
print('{} % {} = {}'.format(n1, n2, (operator.mod(n1,n2))))
print('{} // {} = {}'.format(n1, n2, (operator.floordiv(n1,n2))))
print('{} ** {} = {}'.format(n1, n2, (operator.pow(n1,n2))))

print('{} == {} = {}'.format(n1, n2, (operator.eq(n1,n2))))
print('{} != {} = {}'.format(n1, n2, (operator.ne(n1,n2))))
print('{} > {} = {}'.format(n1, n2, (operator.gt(n1,n2))))
print('{} >= {} = {}'.format(n1, n2, (operator.ge(n1,n2))))
print('{} < {} = {}'.format(n1, n2, (operator.lt(n1,n2))))
print('{} <= {} = {}'.format(n1, n2, (operator.le(n1,n2))))

flag1 = True
flag2 = False
print('{} and {} : {}'.format(flag1, flag2, (operator.and_(flag1,flag2))))
print('{} or {} : {}'.format(flag1, flag2, (operator.or_(flag1,flag2))))
print('not {} : {}'.format(flag1, flag2, (operator.not_(flag1))))

age = int(input('나이 입력 : '))
vac = operator.or_(operator.lt(age, 20), operator.ge(age, 65))
print('age : {} / 대상자 : {}'.format(age, vac))