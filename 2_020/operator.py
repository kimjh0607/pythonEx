'''
and연산 - A and B A와 B 모두 True인 경우만 결과값이 True
or연산 - A or B A와 B 둘중 하나만 True인 경우 결과값이 True
'''
print('{} and {} : {}'.format(True, True, (True and True)))
print('{} and {} : {}'.format(False, True, (False and True)))
print('{} and {} : {}'.format(True, False, (True and False)))
print('{} and {} : {}'.format(False, False, (False and False)))

print('{} or {} : {}'.format(True, True, (True or True)))
print('{} or {} : {}'.format(False, True, (False or True)))
print('{} or {} : {}'.format(True, False, (True or False)))
print('{} or {} : {}'.format(False, False, (False or False)))

print('not {} : {}'.format(True, (not True)))
print('not {} : {}'.format(False, (not False)))

#실습
#백신접종 대상자는 20세미만 또는 65세 이상자에 한합니다.
age = int(input('나이 입력 : '))
vaccine = age < 20 or age >=65
print('age : {}, 백신대상자 : {}'.format(age, vaccine))

#실습
#korean english math 점수입력받아서 평균70점 이상이면 True를 출력하는 코드
#(단, 과목별 최소점수가 60점 이상인 경우여야함)
kor = int(input('korScore : '))
eng = int(input('engScore : '))
math = int(input('mathScore : '))
avg = (kor+eng+math) / 3

print(f'평균 : {avg}, 최종결과 : {avg>=70 and kor>=60 and eng>=60 and math>=60}')