str = 'Hi! '
result = str * 7 #문자열을 이용한 곱셈
print(result)

n1 = 10
n2 = 3
divide = n1 / n2
print('result : {}'.format(divide)) #포맷형식
print('result : %.2f' %divide) #형식문자로 자릿수를 정할 수도 있다.

n1 = 0
n2 = 3
divide = n1 / n2
#divide2 = n2 / n1
print(divide) #0은 무엇으로 나누어도 0이다.
#print(divide2) #ZeroDivisionError: division by zero 0으로 나눌 수 없다.

#나눗셈의 결과는 항상 실수형(float)이다.
#정수형을 원하면 타입캐스팅을 해주면 된다. input을 정수형을 캐스팅하든, 연산결과출력을 정수형으로 캐스팅하든.
korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
mathScore = int(input('수학 점수 : '))
avg = (korScore + engScore + mathScore) / 3
print(f'평균점수 : {avg}')