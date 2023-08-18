
class NormalTv():

    def __init__(self, i=32, c='black', r='full-HD'):
        self.inch = i
        self.color = c
        self.resolution = r
        self.smartTv = 'off'
        self.aiTv = 'off'

    def turnOn(self):
        print('Tv power on~!')

    def turnOff(self):
        print('Tv power off~!')

    def printTvInfo(self):
        print(f'inch : {self.inch}inch')
        print(f'color : {self.color}')
        print(f'resolution : {self.resolution}')
        print(f'smartTv : {self.smartTv}')
        print(f'aiTv : {self.aiTv}')


class Tv4k(NormalTv):

    def __init__(self, i, c, r='4k'):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTv = s


class Tv8k(NormalTv):

    def __init__(self, i, c, r='8k'):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTv = s

    def setAiTv(self, a):
        self.aiTv = a