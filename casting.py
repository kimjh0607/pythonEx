# str() 함수 typeCasting 형변환
# type() 함수 타입확인
iNum = 10
fNum = 3.14

print(iNum)
print(type(iNum))

print(fNum)
print(type(fNum))

iNum = str(iNum)
fNum = str(fNum)

print(iNum)
print(type(iNum))

print(fNum)
print(type(fNum))

flag = True
print(flag)
print(type(flag))

flag = str(flag)
print(flag)
print(type(flag))

num1 = 123
num2 = 456
print(num1+num2)

num1 = str(num1)
num2 = str(num2)
print(num1+num2)

fNum1 = 3.14
fNum2 = 0.123
print(fNum1+fNum2)
print(type(fNum1+fNum2))

fNum1 = str(fNum1)
fNum2 = str(fNum2)
print(fNum1+fNum2)
print(type(fNum1+fNum2))

