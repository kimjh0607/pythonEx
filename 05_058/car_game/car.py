
import random as ran

class Car:

    def __init__(self, n= 'fire car', c= 'red', s= 200):
        self.name = n
        self.color = c
        self.maxSpeed = s
        self.distance = 0

    def printCarInfo(self):
        print(f'{self.name}, {self.color}, {self.maxSpeed}')

    def controlSpeed(self):
        return ran.randint(0, self.maxSpeed)

    def getDistanceForHour(self):
        return self.controlSpeed() * 1


