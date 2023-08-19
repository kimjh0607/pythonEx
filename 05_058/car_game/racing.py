
from time import sleep

class CarRacing:

    def __init__(self):
        self.cars = []
        self.ranking = []

    def startRacing(self):
        print('Racing Start!!')
        for index in range(10):
            print(f'Racing : {index+1}바퀴')
            for carIndex in self.cars:
                carIndex.distance += carIndex.getDistanceForHour()

            sleep(1)
            self.printCurrentCarDistance()

    def printCurrentCarDistance(self):
        for carIndex in self.cars:
            print(f'{carIndex.name} : {carIndex.distance}\t\t', end='')
        print()

    def addCar(self, c):
        self.cars.append(c)