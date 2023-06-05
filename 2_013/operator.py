'''
연산자 : +, -, *, /, %, //, **
할당연산자 : =, +=, -=, *=, /=, %=, //=
비교연산자 : >, >=, <, <=, ==, !=,
논리연산자 : and, or, not
1문자끼리 더할수있다. 2문자끼리 뺄수 없다 3문자와 숫자는 더할 수 없다
'''

n1 = 3.14
n2 = 0.12
n3 = 3
sum = n1 + n2
#형식문자열
print('sum : %.3f' %sum)
print('sum : %.1f' %(n1 + n2))
#포맷문자열
print(f'sum : {sum}')

s1 = 'good'
s2 = ' '
s3 = 'morning'
result = s1 + s2 + s3
print(s1+s2+s3)
print(result)
print('-'*30)

# 문자와 문자는 더할 수 있다.
# print(s1-s2-s3) 문자열 뺴기는 불가하다
# print(n3+s1) 숫자와 문자는 결합이 불가하다.

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
mathScore = int(input('수학 점수 : '))
total = korScore + engScore + mathScore
avg = (korScore + engScore + mathScore) / 3
print('국어 : {}, 영어 : {}, 수학 : {}'.format(korScore,engScore,mathScore))
print('총점수 : {}, 평균점수 : {}'.format(total, avg))
print('-'*30)

income = int(input('수익입력(단위만원) : '))
outcome = int(input('지출입력(단위만원) : '))
total = income - outcome
print('수입 : %d , 지출 : %d, 순소득 : %d' %(income, outcome, total))

