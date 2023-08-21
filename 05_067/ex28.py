
#약수
inputNumber = int(input('0보다 큰 정수 입력 : '))

divisor = []
for num in range(1, (inputNumber+1)):
    if inputNumber % num == 0:
        divisor.append(num)

if len(divisor) > 0 :
    try:
        with open('C:/pythonTxt/divisor.txt', 'a') as f:
            f.write(f'{inputNumber}의 약수 : ')
            f.write(f'{divisor}\n')
    except Exception as e:
        print(e)
    else:
        print('divisor write complete!!')

#소수
inputNumber = int(input('0보다 큰 정수 입력 : '))
prime = []
for num in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2, num):
        if num % n == 0:
            flag = False
            break

    if flag:
        prime.append(num)

if len(prime) > 0:
    try:
        with open('C:/pythonTxt/prime.txt', 'a') as f:
             f.write(f'{inputNumber}까지의 소수 : ')
             f.write(f'{prime}\n')
    except Exception as e:
        print(e)
    else:
        print('prime write complete!!')