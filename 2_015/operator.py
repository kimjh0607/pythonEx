'''
나머지 연산자 % 몫 연산자 //
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

res4 = divmod(n1, n2)
#division mode - 첫번째 데이터를 두번째 데이터로 나누어준다
#튜플 형태로 반환, 인덱스0이 몫 인덱스1이 나머지
print(res4)
print('result: {}'.format(res4))
print('몫: {}'.format(res4[0])) #
print('나머지: {}'.format(res4[1])) #

all = int(input('전체 학생 수 입력 : '))
part = int(input('한 반 학생 수 입력 : '))
group = divmod(all, part)
print('반 개수 : {}, 남는학생 : {}'.format(group[0], group[1])) #포맷함수
print('반 개수 : %d, 남는학생 : %d' %(group[0], group[1])) #형식문자열
print(f'반 개수 : {group[0]}, 남는학생 : {group[1]}') #포맷문자열

#123개의 사과를 4개씩 직원들에게 나누어준다. 나누어줄 수 있는 직원수와 남는 사과개수 출력
result = divmod(123,4)
employee = result[0]
apple = result[1]
print(f'나누어 줄 수 있는 직원수 : {employee}, 남는 사과 수 : {apple}')

