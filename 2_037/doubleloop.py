'''
중첩반복문 - 반복문안에 또 다른 반복문을 선언한다.
세번까진 몰라도 너무많이 중첩시키면 과부하 걸려서 안좋다.
'''
#계단식 별찍기
for i in range(1, 10):
    for j in range(i):
        print('*', end='')
    print() #개행


#거꾸로 별찍기
for i in range(10,0,-1):
    for j in range(i):
        print('*',end='')
    print()

#구구단
for i in range(1,10):
    for j in range(1,10):
        res = i*j
        print('{} * {} = {}\t'.format(j,i,res),end='')
    print()