str = 'Hi '
result = str * 10
print(result)

n1 = 10
n2 = 3
nanum = n1 / n2
print('resut : {}'.format(nanum)) #포맷형식
print('result : %.2f' %nanum) #형식문자
#나눗셈의 결과는 항상 실수형이다
#정수형을 원하면 타입캐스팅하면된다.

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
mathScore = int(input('수학 점수 : '))
avg = (korScore + engScore + mathScore) / 3
print(f'평균점수 : {avg}')