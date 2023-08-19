
import random as ran

class Dice:
    
    def __init__(self):
        self.cNum = 0
        self.uNum = 0

    def setCnum(self):
        print(f'[Dice] setCnum~~')
        self.cNum = ran.randint(1,6)

    def setUnum(self):
        print(f'[Dice] setUnum~~')
        self.uNum = ran.randint(1,6)

    def startGame(self):
        print(f'[Dice] Game Start!!')
        self.setCnum()
        self.setUnum()

    # def printResult(self):
    #     print(f'게임 결과는?')
    #     if self.cNum == 0 or self.uNum == 0 :
    #         print('숫자 설정 전 입니다.')
    #     elif self.cNum > self.uNum:
    #         print(f'com({self.cNum} VS user({self.uNum})) >>> com Win!!')
    #     elif self.cNum < self.uNum:
    #         print(f'com({self.cNum} VS user({self.uNum})) >>> user Win!!')
    #     elif self.cNum == self.uNum:
    #         print(f'com({self.cNum} VS user({self.uNum})) >>> Draw!!')


    def printResult(self):
        print(f'게임 결과는?')

        if self.cNum == 0 or self.uNum == 0 :
            print('숫자 설정 전 입니다.')
        else:
            if self.cNum > self.uNum:
                print(f'com({self.cNum} VS user({self.uNum})) >>> com Win!!')
            elif self.cNum < self.uNum:
                print(f'com({self.cNum} VS user({self.uNum})) >>> user Win!!')
            elif self.cNum == self.uNum:
                print(f'com({self.cNum} VS user({self.uNum})) >>> Draw!!')