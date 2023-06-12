import random

rNum = random.randint(1,1000)
tryCount = 0
gameFlag = True

while gameFlag:
    tryCount += 1
    pNum = int(input('enter 1~1000 Number : '))

    if rNum == pNum:
        print('correct!')
        gameFlag = False #
    else:
        if rNum > pNum:
            print('Num is bigger')
        else:
            print('Num is smaller')

print('randomNumber : {}, tryCount : {}'.format(rNum, tryCount))

#airconditioner
temp = int(input('enter temp : '))

if temp <= 18:
    print('off')
elif temp > 18 and temp <= 22:
    print('very weak')
elif temp > 22 and temp <= 24:
    print('weak')
elif temp > 24 and temp <= 26:
    print('mid')
elif temp > 26 and temp <= 28:
    print('strong')
elif temp > 28:
    print('very strong')