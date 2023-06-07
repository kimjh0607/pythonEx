'''
반복문제어

continue 키워드 - 반복 실행 중 continue를 만나면 실행을 생략, 다음 반복 실행문으로 넘어감.
else 키워드 - else의 실행문은 for반복문이 종료된 후에 실행된다.
break 키워드 - 실행을 중단하고 반복문을 빠져나와라
'''
#continue
for i in range(100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수'.format(i))

#else
cnt = 0
for i in range(100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수'.format(i))
    cnt += 1 #반복을 실행한 횟수가 저장됨.
else:
    print('7의 배수는 {}개'.format(cnt))

#break
num = 0
while True:
    print('Hi~')

    num+=1
    if(num>=5):
        print('bye~')
        break