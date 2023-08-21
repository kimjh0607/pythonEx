
# 두 수의 공약수
num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

common = []

for index in range(1, (num1 + 1)):
    if num1 % index == 0 and num2 % index == 0:
        common.append(index)

if len(common) > 0:
    try:
        with open('C:/pythonTxt/common.txt', 'a') as f:
            f.write(f'{num1}과 {num2}의 공약수 : ')
            f.write(f'{common}\n')
    except Exception as e:
        print(e)
    else:
        print('common factor write complete!!')

# 두 수의 최대 공약수
num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

maxComNum = 0

for index in range(1, (num1 + 1)):
    if num1 % index == 0 and num2 % index == 0:
        maxComNum = index

try:
    with open('C:/pythonTxt/maxComNum.txt', 'a') as f:
        f.write(f'{num1}과 {num2}의 최대 공약수 {maxComNum}\n')
except Exception as e:
    print(e)
else:
    print('Max common factor write complete!!')