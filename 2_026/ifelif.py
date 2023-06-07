'''
if~elif문 - 여러가지 조건식 결과에 따라 실행문이 결정됨.
'''
Score = int(input('시험 성적 입력 : '))
grades = ''

if Score >= 90:
    grades = 'A'
elif Score >= 80:
    grades = 'B'
elif Score >= 70:
    grades = 'C'
elif Score >= 60:
    grades = 'D'
else:
    grades = 'F'

print('성적 : {} \t 학점 : {}'.format(Score, grades))

'''
주의할점 조건식 순서가 중요하다
'''
Score = int(input('시험 성적 입력 : '))
grades = ''

if Score >= 60:
    grades = 'D'
elif Score >= 70:
    grades = 'C'
elif Score >= 80:
    grades = 'B'
elif Score >= 90:
    grades = 'A'
else:
    grades = 'F' #어떤 점수든지 F아니면 C를 받게된다
                #and를 써서 정확한 범위를 지정하여 쓰던지 순서를 지키던지 한다.