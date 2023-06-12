#홀짝게임
import random

cNum = random.randint(1,2)
pNum = int(input('choose 1.홀 \t 2.짝'))

if cNum ==1 and pNum ==1:
    print('빙고 홀수')
elif cNum ==2 and pNum ==2:
    print('빙고 짝수')
elif cNum == 1 and pNum == 2:
    print('실패 홀수')
elif cNum == 2 and pNum == 1:
    print('실패 짝수')


#가위바위보 게임
cNum = random.randint(1,3)
pNum = int(input('선택 - 1.가위 \t 2.바위 \t 3.보'))

if (cNum ==1 and pNum ==2) or (cNum==2 and pNum==3) or (cNum ==3 and pNum ==1):
    print('com defeat, player win')
elif cNum == pNum:
    print('draw')
else:
    print('com win, player defeat')

print('com : {}, player : {}'.format(cNum,pNum))