money = int(input('금액?'))
rate = float(input('이율?'))
term = int(input('기간?'))

target = money

for i in range(term):
    target += (target * rate * 0.01) #이율땜시 기간에 100나눔

result = format(int(target) , ',')
print('-' * 30)
print('원금 : {}'.format(money))
print('이율 : {}'.format(rate))
print('기간 : {}'.format(term))
print('{}년 후 받을금액 : {}원'.format(term,result))
print('-' * 30)