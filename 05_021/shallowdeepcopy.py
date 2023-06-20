'''
얕은 복사란, '객체 주소를 복사'하는 것으로 객체 자체가 복사되지 않는다.
깊은 복사란, '객체 자체'를 복사하는 것으로 하나의 객체가 만들어진다.
'''
class TemCls:

    def __init__(self, n, s):
        self.number = n
        self.str = s

    def Info(self):
        print(f'number : {self.number}')
        print(f'str : {self.str}')

#얕은복사
tc1 = TemCls(10, 'Hello')
tc2 = tc1

tc1.Info()
tc2.Info()

tc2.number = 3.14
tc2.str = 'Bye'

tc1.Info()
tc2.Info()

#깊은 복사
import copy

tc1 = TemCls(10, 'Hello')
tc2 = copy.copy(tc1) #객체 자체를 복사

tc1.Info()
tc2.Info()

tc2.number = 3.14
tc2.str = 'Bye'

tc1.Info()
tc2.Info()

scores = [9, 8, 5, 7, 6, 10]
scoresCopy = []

# scoresCopy = scores
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

#깊은복사 4가지 - for문 사용, extend(), copy모듈사용, 슬라이스사용
# for s in scores:
#     scoresCopy.append(s)
#
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

# scoresCopy.extend(scores)
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

# scoresCopy = scores.copy()
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

scoresCopy = scores[:]
print(f'id(scores) : {id(scores)}')
print(f'id(scoresCopy) : {id(scoresCopy)}')

#실습 남아있음.
plaOriSco = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
plaCopSco = plaOriSco.copy()

plaOriSco.sort()

plaCopSco.sort()
plaCopSco.pop(0)
plaCopSco.pop() #절사평균의 개념 - 데이터분석에 유용할지도..

print(f'plaOriSco : {plaOriSco}')
print(f'plaCopSco : {plaCopSco}')

oriTot = round(sum(plaOriSco), 2)
oriAvg = round(oriTot / len(plaOriSco), 2)
print(f'Original Total : {oriTot}')
print(f'Original Average : {oriAvg}')

copTot = round(sum(plaCopSco), 2)
copAvg = round(copTot / len(plaCopSco), 2)
print(f'Copy Total : {copTot}')
print(f'Copy Average : {copAvg}')

print(f'oriAvg - copAvg : {oriAvg - copAvg}')
