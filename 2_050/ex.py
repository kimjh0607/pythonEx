speed = int(input('enter speed : '))

if speed >= 50:
    print('안전속도 위반 - 과태료 50,000원 부과!')
else:
    print('안전속도 준수중!')



msg = input('enter message : ')

if len(msg) > 50:
    print('message : {}'.format(msg))
    print('MMS !')
    print('msg length : {}'.format(len(msg)))
    print('fee : 100won')
else:
    print('message : {}'.format(msg))
    print('SMS !')
    print('msg length : {}'.format(len(msg)))
    print('fee : 50won')