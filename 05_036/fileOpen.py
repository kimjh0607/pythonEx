'''
파일모드 - 파일을 어떤 목적으로 open할 지 결정한다.
'w' - 쓰기 전용(파일이 있으면 덮어씌움)
'a' - 쓰기 전용(파일이 있으면 덧붙임) ex로그를 쌓을 때
'x' - 쓰기 전용(파일이 있으면 에러 발생)
'r' - 읽기 전용(파일이 없으면 에러 발생)
'''

# uri = 'C:/pythonTxt/'

# # 'w' 다 날리고 덮어씌움
# file = open(uri + 'hello.txt', 'w')
# file.write('Hello Python~')
# file.close()

# # 'a'
# file = open(uri + 'hello.txt', 'a')
# file.write('\nNice to meet you!!')
# file.close()

# # 'x'
# file = open(uri + 'hello_01.txt', 'x')
# file.write('\nNice to meet you!!')
# file.close()

# 'r'
# file = open(uri + 'hello_01.txt', 'r')
# str = file.read()
# print(f'string : {str}')
# file.close()

#실습
uri = 'C:/pythonTxt/'

def writePrimeNumber(n):
    file = open(uri + 'primeNumbers.txt', 'a')
    file.write(str(n))
    file.write('\n')
    file.close()
inputNum = int(input('enter number(>0)'))
for number in range(2, (inputNum + 1)):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break

    if flag:
        writePrimeNumber(number)
