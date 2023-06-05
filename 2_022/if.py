'''
A if 조건식 else B
조건식의 결과가 True이면 A실행, 그렇지 않으면 B실행
True 앞 False 뒤
'''

n1 = 10
n2 = 100

numRes = True if n1 > n2 else False
#3항 연산자 같은것임.
print('n1은 n2보다 크다.') if numRes else print('n1은 n2보다 작다.')
#풀어쓰면 아래

# if numRes:
#     print('n1은 n2보다 크다.')
# else:
#     print('n1은 n2보다 작다.')

print('n1 > n2 : {}'.format(numRes))

print('\'n1은 n2보다 크다.\'') if numRes else print('\'n1은 n2보다 작다.\'')

