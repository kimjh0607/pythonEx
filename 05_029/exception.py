'''
예외처리 - 발생된 예외를 별도 처리함으로써 프로그램 전체의 실행에 문제가 없도로 함.
프로그램 전체 실행에 영향이 없도록 처리.
'''

n1 = 10; n2 = 0

try:
    print(n1 / n2) #들여쓰기
except:
    print('예외발생') #처리할 실행문
    
print(n1 * n2)
print(n1 - n2)
print(n1 + n2)

#실습
nums = []

n = 1
while n < 6:
    try:
        num = int(input('enter number  :'))
    except: #숫자가 아닌 자료형이 입력되면 예외처리.
        print('exception~!!')
        continue #

    nums.append(num)
    n += 1

print(f'nums : {nums}')