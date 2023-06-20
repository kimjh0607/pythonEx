'''
하위 클래스에서 상위 클래스의 메서드를 재정의한다.
'''

class Robot:

    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w

    def fire(self):
        print('fire!!')


class NewRobot(Robot):

    def __init__(self, c, h, w):
        super().__init__(c, h, w)

    def fire(self):
        print('lazer!!') #오버라이딩.

myRobot = NewRobot('red', 200, 300)
myRobot.fire()

#실습
class TriangleArea:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printInfo(self):
        print(f'self.width : {self.width}')
        print(f'self.height : {self.height}')

    def getArea(self):
        return self.width * self.height / 2

class NewTriangleArea(TriangleArea):

    def __init__(self, w, h):
        super().__init__(w, h)

    def getArea(self):
        return str(super().getArea()) + ' (cm X cm)'

tri1 = NewTriangleArea(10, 10)
triArea = tri1.getArea()
print(f'Area = {triArea}')