korScore = int(input('국어점수입력 : '))
engScore = int(input('영어점수입력 : '))
mathScore = int(input('수학점수입력 : '))
total = korScore+engScore+mathScore
avg = total / 3

max = korScore
maxSub = 'korean'

if engScore > max:
    max = engScore
    maxSub = 'english'

if mathScore > max:
    max = mathScore
    maxSub = 'math'

min = korScore
minSub = 'korean'

if engScore < min:
    min = engScore
    minSub = 'english'

if mathScore < min:
    min = mathScore
    minSub = 'math'

diff = max - min
print('-' * 30)
print('총점 : {}'.format(total))
print('평균 : %.2f' %(avg))
print('최고점 : {}{}, 최저점 : {}{}, 최고최저차이 : {}'.format(max, maxSub, min, minSub, diff))
print('-' * 30)


