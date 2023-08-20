
g1Price = 1200
g2Price = 1000
g3Price = 800
g4Price = 2000
g5Price = 900

def formatted(price):
    return format(price, ',')

def calculator(*gcs):

    gcsDic = {}
    againCntInput = {}

    for index, gc in enumerate(gcs):
        try:
            gcsDic[f'g{index+1}'] = int(gc)
        except Exception as e:
            againCntInput[f'g{index+1}'] = gc
            print(e)

    totalPrice = 0
    for goodIndex in gcsDic.keys():
        totalPrice += globals()[f'{goodIndex}Price'] * gcsDic[goodIndex]

    print('-'*30)
    print(f'Total Price : {formatted(totalPrice)}원')
    print('-'*10 + '미결제 항목' + '-'*10)
    for goodIndex in againCntInput.keys():
        print(f'상품 : {goodIndex}, \t 구매 개수 : {againCntInput[goodIndex]}')
    print('-'*30)

