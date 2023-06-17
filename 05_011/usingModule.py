'''
import
as - 별칭을 붙인다(간단하게)
from ~as 키워드 - 모듈의 특정 기능만 사용할 수 있다.
'''

# import calculator as cal #alias 'cal'
#
# cal.add(10, 20)
# cal.sub(10, 20)
# cal.mul(10, 20)
# cal.div(10, 20)


from calculator import add
from calculator import sub
#from calculator import sub, mul, div => 배열 형태로 나열하여 함수를 가져올 수도 있다.
#from calculator import * => 모듈의 기능 전부 가져오기


add(10, 20) # from 키워드로 가져오면 module명을 적지 않고 함수를 호출가능
sub(20, 5)

import scores #별칭을 쓸수도, from scores as 함수 형태로 - 함수명만 호출할 수도.
scores.addScore(70)
scores.addScore(80)
scores.addScore(100) #값을 직접 입력할 수도.
scores.addScore(90)
scores.addScore(60)

print(scores.getScores())
print(scores.getTotalScore())
print(scores.getAvgScore())

kor = int(input('enter kor score : '))
eng = int(input('enter eng score : '))
math = int(input('enter math score : '))

# 이런식으로 값을 입력받을수도
# scores.addScore(kor)
# scores.addScore(eng)
# scores.addScore(math)