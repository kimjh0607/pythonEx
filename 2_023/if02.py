limit = 30
sAmount = int(input('적설량 입력 : '))

print('적설량 : {}mm , {}'.format(sAmount, '대설경보')) if sAmount>=limit else print('적설량 : {}mm , {}'.format(sAmount, '대설경보아님'))