'''
for문이 적합한경우
횟수에 의한 반복이라면.
1부터 10까지의 합을 구하는 경우는 for문이 낫다.

while문이 적합한 경우
조건에 의한 반복이라면.
1부터 시작해서 7의 배수의 합이 50이상인 최초의 정수 출력.
'''

#실습
'''
자동자 바퀴가 한번구를때 0.15mm 마모
현재 바퀴두께는 30mm 최소운행가능바퀴두께는 20mm
앞으로 구를 수 있는 횟수는 얼마인가?
'''
thick = 30
min = 20
once = 0.15
count = 0

while (thick - (once * count)) > min:
    thick -= (once * count)
    count += 1

print('운행중지. 바퀴수 {}회'.format(count))


