'''
나머지 연산자,
divmod() 함수  - 몫,나머지 구해준다.
'''

n1 = 10
n2 = 3
res1 = n1 / n2
res2 = n1 % n2 #나머지연산
res3 = n1 // n2 #몫연산
print(res1)
print(res2)
print(res3)

res4 = divmod(n1, n2) #division mode
print(res4)
print('result: {}'.format(res4))
print('몫: {}'.format(res4[0]))
print('나머지: {}'.format(res4[1]))

all = int(input('전체 학생 수 입력 : '))
part = int(input('한 집단 학생 수 입력 : '))
group = divmod(all, part)
print('반 : {}, 남는학생 : {}'.format(group[0], group[1]))
print('반 : %d, 남는학생 : %d' %(group[0], group[1]))