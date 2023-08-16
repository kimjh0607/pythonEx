

#an = a1 + (n-1) * d
#sn = (a1+an)*n/2
def ansn(a1, d, n):

    for index in range(1,n+1):
        an = int(a1 + (index - 1) * d)
        sn = int((a1 + an) * index / 2)
        print(f'{index}번째 항의 값 {an}')
        print(f'{index}번째 항까지의 합 {sn}')


a1 = int(input('초항 입력 : '))
d = int(input('공차 입력 : '))
n = int(input('항 수 입력 : '))

print(ansn(a1, d, n))
