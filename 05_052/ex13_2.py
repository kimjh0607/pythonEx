
from shape import triangle_square_area
from shape import circle_area

width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))
radius = float(input('반지름 입력 : '))

print(f'삼각형 넓이 : {triangle_square_area.triArea(width, height)}')
print(f'사각형 넓이 : {triangle_square_area.squArea(width, height)}')

print(f'원 넓이 : {circle_area.cirArea(radius):.2f}')