class Car: #클래스 시작문자는 대문자
    def __init__(self, col, len):
        self.color = col #self는 Car자신 이라는 뜻
        self.length = len

    def doStop(self): #매개변수가 self라는 것은 Car클래스 안에 포함되는 기능이다
        print('Stop!')

    def doStart(self):
        print('Start!')

    def printCarInfo(self):
        print(f'self.color : {self.color}')
        print(f'self.length : {self.length}')


car1 = Car('red', 200) #객체 생성 : 객체 = 클래스명(매개, 매개) => __init__() 에 'red', 200 이 할당된다.
car2 = Car('blue', 300)
car1.printCarInfo()
car2.printCarInfo()
car1.doStop()
car2.doStart()

#실습
class Airplane:
    def __init__(self,col,no):
        self.color = col
        self.number = no

    def arrive(self):
        print('도착')

    def depart(self):
        print('출발')

    def Info(self):
        print(f'색 : {self.color}, 편명 : {self.number}')

koreanAir = Airplane('skyblue', 500)
asiana = Airplane('gold', 300)
airBusan = Airplane('navy', 200)
jinAir = Airplane('green', 600)

koreanAir.Info()
asiana.depart()
airBusan.Info()
jinAir.arrive()