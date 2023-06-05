n1 = 10 ; n2 = 5

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

#자동차의 전장과 전폭을 입력하면 자동차 기계 세차 가능여부를 출력하는 코드를 작성
#전장최대 : 5200, 전폭최대 : 1985
maxLength = 5200
maxWidth = 1985

myLength = int(input('전장입력 : '))
myWidth = int(input('전폭입력 : '))
Length = maxLength >= myLength
Width = maxWidth >= myWidth
print(f'전장가능여부 {Length}, 전폭가능여부 {Width}')