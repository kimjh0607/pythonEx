n1 = 10

n1 += 5  #== n1 = n1 + 5
print('num : {}'.format(n1))

n1 -= 5
print('num : {}'.format(n1))

n1 *= 2
print('num : {}'.format(n1))

n1 /= 2
print('num : {}'.format(n1)) #나누면 실수형

n1 %= 6
print('num : {}'.format(n1))

n1 //= 2
print('num : {}'.format(n1))

n1 **= 2
print('num : {}'.format(n1))

'''
누적강수량 출력해보기
1월 30
2월 45
3월 47
4월 55
5월 65
6월 100
7월 128
8월 209
9월 204
10월 186
11월 67
12월 25
'''

total = 0
#1월
rain = 30
total += rain
print('1월 누적 강수량 :',total)

#2
rain = 45
total += rain
print('2월 누적 강수량 :',total)

#3
rain = 47
total += rain
print('3월 누적 강수량 :',total)

#4
rain = 55
total += rain
print('4월 누적 강수량 :',total)

#5
rain = 65
total += rain
print('5월 누적 강수량 :',total)

#6
rain = 100
total += rain
print('6월 누적 강수량 :',total)

#7
rain = 128
total += rain
print('7월 누적 강수량 :',total)

#8
rain = 209
total += rain
print('8월 누적 강수량 :',total)

#9
rain = 204
total += rain
print('9월 누적 강수량 :',total)

#10
rain = 186
total += rain
print('10월 누적 강수량 :',total)

#11
rain = 67
total += rain
print('11월 누적 강수량 :',total)

#12
rain = 25
total += rain
print('12월 누적 강수량 :',total)

print('-'*30)
print('연간누적 강수량 :',format(total, ','))
print('평균 강수량 :',total/12)
print('-'*30)