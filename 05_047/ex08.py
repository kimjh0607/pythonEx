


disRate = 0
buyCnt = 0
costSum = 0

while True:
    buyExit = int(input('상품을 구매하시겠어요? 1.구매 2.종료 : '))
    if buyExit == 2:
        break

    if buyExit == 1:
        cost = int(input('상품 가격 입력 : '))
        costSum += cost
        buyCnt += 1

if buyCnt == 1:
    disRate = 5
    costSum *= 0.95
elif buyCnt == 2:
    disRate = 10
    costSum *= 0.9
elif buyCnt == 3:
    disRate = 15
    costSum *= 0.85
elif buyCnt == 4:
    disRate = 20
    costSum *= 0.8
else:
    disRate = 25
    costSum *= 0.75

print(f'할인율 : {disRate}%')
print(f'합계 : {int(costSum)}원')



