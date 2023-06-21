'''
with ~ as 구문
파일 닫기(close)를 생략할 수 있다.
'''
uri = 'C:/pythonTxt/'

# file = open(uri + '5_037.txt', 'a')
# file.write('python study!!!!')
# file.close()
#
# file = open(uri + '5_037.txt', 'r')
# print(file.read())
# file.close()

with open(uri + '5_037.txt', 'a') as file:   #코드가 더 간결해진다
    file.write('python study!!!!!!')

with open(uri + '5_037.txt', 'r') as file:
    print(file.read())