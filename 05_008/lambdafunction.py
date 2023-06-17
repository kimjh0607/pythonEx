'''
lambda 키워드를 이용하면 함수 선언을 보다 간다하게 할 수 있다.
'''

def cal(a, b):
    return a + b

returnValue = cal(10, 20)
print(f'returnValue : {returnValue}')

#lambda 형식으로 바꾸면?
cal = lambda a, b: a + b
returnValue = cal(10, 20)
print(f'returnValue : {returnValue}')

getTriangle = lambda a, b: a * b / 2
getSquare = lambda a, b: a * b
getCircle = lambda r : r * r * 3.14

width = int(input('enter width : '))
height = int(input('enter height : '))
radius = int(input('enter radius : '))

triangleArea = getTriangle(width, height)
squareArea = getSquare(width, height)
circleArea = getCircle(radius)

print(f'triangle Area : {triangleArea}')
print(f'square Area : {squareArea}')
print(f'circle Area : {circleArea}')

# print(getTriangle(width, height))
# print(getSquare(width, height))
# print(getCircle(radius))
