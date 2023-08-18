
from arithmetic import basic_operator
from arithmetic import developer_operator
from shape import triangle_square_area
from shape import circle_area

n1 = float(input('숫자 1 입력 : '))
n2 = float(input('숫자 2 입력 : '))

print(f'{n1} + {n2} = {basic_operator.add(n1,n2)}')
print(f'{n1} - {n2} = {basic_operator.sub(n1,n2)}')
print(f'{n1} * {n2} = {basic_operator.mul(n1,n2)}')
print(f'{n1} / {n2} = {basic_operator.div(n1,n2)}')

print(f'{n1} % {n2} = {developer_operator.div2(n1,n2)}')
print(f'{n1} // {n2} = {developer_operator.mod(n1,n2)}')
print(f'{n1} ** {n2} = {developer_operator.jegob(n1,n2)}')


