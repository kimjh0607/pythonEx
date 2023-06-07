'''
1반복문이란 특정 실행을 반복하는 것.
2반복문을 사용하면 프로그래밍이 간결하고 유지 보수가 쉽다.
ex) 대량메일 또는 문자발송, 인사말반복, mp3자동재생, 구구단 출력, 팩토리얼, 기상알람 등등
3반복의 종류 - 횟수에 의한 반복(횟수만큼) - for, 조건에 의한 반복(조건에 만족할 때까지) - while
'''

# print('{} * {} = {}'.format(2,1,(2*1)))
# print('{} * {} = {}'.format(2,2,(2*2)))
# print('{} * {} = {}'.format(2,3,(2*3)))
# print('{} * {} = {}'.format(2,4,(2*4)))
# print('{} * {} = {}'.format(2,5,(2*5)))
# print('{} * {} = {}'.format(2,6,(2*6)))
# print('{} * {} = {}'.format(2,7,(2*7)))
# print('{} * {} = {}'.format(2,8,(2*8)))
# print('{} * {} = {}'.format(2,9,(2*9)))

# for i in range(1,10):
#     print('{} * {} = {}'.format(2,i,(2*i)))

# print('{}선수 에게 메일 발송!'.format('박찬호'))
# print('{}선수 에게 메일 발송!'.format('박세리'))
# print('{}선수 에게 메일 발송!'.format('박지성'))
# print('{}선수 에게 메일 발송!'.format('김연경'))
# print('{}선수 에게 메일 발송!'.format('이승엽'))

players = ['박찬호','박세리','박지성','김연경','이승엽']
for player in players:
    print('{} 선수 에게 메일 발송!'.format(player))

'''
횟수에 의한 반복이란
for문 사용방법

for 변수 in 반복횟수: #반복횟수만큼 변수에게 던져준다.
    실행문
'''
for j in range(10):
    print('{} * {} = {}'.format(7, j, (7*j)))

#pass키워드 - 나중에 코딩하겠다
for i in range(100):
    pass #비워두면 에러가 뜬다.

for j in range(5):
    print('Hi', end='')
    print(' loop statement')

'''
range()함수 - for와 붙어다닌다.

기본사용법 - range(시작,끝,단계/단위)
단계 매개변수 생략 - for i in range(1,11) - 단계가 1인 경우에
시작 매개변수 생략 - for i in range(11) - 시작이 0인 경우에
'''
#기본사용법
for i in range(0, 10, 2): #0부터 9까지(10개) 2씩 증가
    pass

#실습
start = int(input('시작숫자입력 :'))
last = int(input('마지막숫자입력 :'))

for i in range(start, last+1):
    print(i)

'''
조건에 의한 반복 - 조건에 만족할때까지 반복 불만족하면 중단.
무한루프에 빠지게 하지 않기 위해 false인 경우를 명시해주어야한다.
while이 주로 사용
for문처럼 들여쓰기 코드블럭 해주어야 한다.

while 조건식: #조건에 만족하면 실행문 실행.
    실행문
'''
end = 10
i = 0
while i <= end:
    print(i)
    i += 1 #이게 없으면 무한루프에 빠진다.

n = 1
while n <10:
    result = 7 * n
    print('{} * {} = {}'.format(7,n,(7*n)))
    n+=1

#pass키워드 - 나중에 코딩하겠다. 안쓰면 에러
while i > 10:
    pass #안쓰면 에러

#실습
j = 1
while j < 101:
    if j % 2 == 0:
        print('{}은 2의 배수이다.'.format(j))

    if j % 3 == 0:
        print('{}은 3의 배수이다.'.format(j))

    j += 1