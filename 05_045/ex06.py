
#an = a1 * r**(n-1)
#sn = a1(1-r**n)/(1-r)
def ansn(a1, r, n):

    for index in range(1,n+1):
        an = int(a1 * r ** (index-1))
        sn = int(a1 * (1-r**index)/(1-r))
        print(f'{index}번째 항의 값 {an}')
        print(f'{index}번째 항까지의 합 {sn}')


a1 = int(input('초항 입력 : '))
r = int(input('공비 입력 : '))
n = int(input('항 수 입력 : '))

ansn(a1, r, n)