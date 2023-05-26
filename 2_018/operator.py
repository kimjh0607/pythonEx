n1 = 10
n2 = 5

res = n1 > n2
print(res)

res = n1 >= n2
print(res)

res = n1 < n2
print(res)

res = n1 <= n2
print(res)

res = n1 == n2
print(res)

res = n1 != n2
print(res)

InputNum1 = int(input('1st 숫자입력 : '))
InputNum2 = int(input('2nd 숫자입력 : '))

print('{} > {} : {}'.format(InputNum1, InputNum2, (InputNum1>InputNum2)))
print('{} >= {} : {}'.format(InputNum1, InputNum2, (InputNum1>=InputNum2)))
print('{} < {} : {}'.format(InputNum1, InputNum2, (InputNum1<InputNum2)))
print('{} == {} : {}'.format(InputNum1, InputNum2, (InputNum1==InputNum2)))
print('{} != {} : {}'.format(InputNum1, InputNum2, (InputNum1!=InputNum2)))