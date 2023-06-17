'''
변수는 '객체의 메모리 주소'를 저장하고 이를 이용해서 객체를 참조한다.
ex) myCar = Car() -> 변수에 직접 객체가 저장이 안됨. 메모리 주소가 변수에 저장됨
앞에서 했던 것들은.. 변수를 이용해서 객체를 조작한 것이 아니라
변수안의 메모리 주소를 찾아가서 객체의 기능을 호출, 속성을 변경한 것임. - '객체참조'
'''
class Robot:

    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight

    def Info(self):
        print(f'color : {self.color}')
        print(f'height : {self.height}')
        print(f'weight : {self.weight}')

rb1 = Robot('red', 200, 80) #뒤의 생성부만 만들면, 객체 생성만 됨. -> 변수를 만들어서 접근가능하도록..
#현재 주소값 저장됨
# rb1.Info() #주소에 가서 Info()함수를 호출하는 것임.

rb2 = Robot('blue', 300, 120)
rb3 = rb1 #얕은복사 rb1의 메모리 주소를 할당. - 하나의 객체를 공유하는 격

rb1.Info()
rb2.Info()
rb3.Info() #rb1.Info()와 값이 같다.

rb1.color = 'gray'
rb1.height = 250
rb1.weight = 100

rb1.Info()
rb2.Info()
rb3.Info() #rb1을 수정했는데, rb3도 같은 곳을 가르키고있는 메모리값이 같기 때문. 같은 곳을 참조한다.

#실습
scores = [int(input('enter kor : ')), int(input('enter eng : ')), int(input('enter math : '))]

print(scores)

copyScores = scores.copy()
for idx, score in enumerate(copyScores):
    result = score * 1.1
    copyScores[idx] = 100 if result > 100 else result

print(f'avg : {sum(scores) / len(scores)}')
print(f'copy avg : {sum(copyScores) / len(copyScores)}')