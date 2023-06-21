'''
try ~ except ~ else
예외가 발생하지 않은 경우에 실해아하는 구문
~else - 예외가 발생하지 않은 경우 실행하는 구문이다. 꼭 필요한 구문은 아니다.
그러나 try except와 꼭 같이 써야한다.
'''

nums = []

n = 1
while n < 6:

    try:
        num = int(input('enter number  :'))
    except: #숫자가 아닌 자료형이 입력되면 예외처리.
        print('exception~!!')
        continue #
    else:
        if num % 2 == 0:
            nums.append(num)
            n += 1
        else:
            print('입력한 수는 홀수입니다.', end='')
            print('다시 입력하세요.')
            continue

print(f'nums : {nums}')

#실습
evenList = []
oddList = []
floatList = []

n = 1
while n < 6:

    try:
        num = float(input('enter number'))
    except:
        print('exception!!!')
        continue
    else:
        if num - int(num) != 0:
            print('float num!!')
            floatList.append(num)
        else:
            if num % 2 == 0:
                print('even num!!')
                evenList.append(int(num))
            else:
                print('odd num!!')
                oddList.append(int(num))

        n += 1

print(f'even : {evenList}')
print(f'odd : {oddList}')
print(f'float : {floatList}')