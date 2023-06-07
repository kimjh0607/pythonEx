'''
조건식(삼항연산자)
'''

num1 = 20
num2 = 10
numRes = num1 > num2
#1 조건식 결과에 따른 실행만 하는 경우
print('num1은 num2보다 크다.') if numRes else print('num1은 num2보다 작다.')
#2 조건식 결과를 변수에 할당하는 경우
numRes = True if num1 > num2 else False

#모든 조건식은 if~else로 바꿀수 있다. 1조건식을 if~else로
if num1 > num2:
    print('num1은 num2보다 크다.')
else:
    print('num1은 num2보다 작다.')

#모든 if~else문을 조건식으로 바꿀수 있는건 아니다.
# if~else에서 실행문이 복잡하면 삼항연산자로 옮기기 애매할 수 있음.

#실습
lowtemp = float(input('최저기온입력 : '))
hightemp = float(input('최고기온입력 : '))
if hightemp-lowtemp>=11:
    print('일교차 : ',(hightemp-lowtemp))
    print('감기조심!')
else:
    print('일교차 : ', (hightemp - lowtemp))
    print('좋은날씨!')