userName = 'hong'
userAge = 20
print(userName)
print(userAge)

print('User name :', userName)
print('User age :', userAge)

print('3 * 5 = ', end='')  #자동개행(\n)을 강제로 빈문자('')로 설정해서 자동개행을 하지않도록하겠다
print(3 * 5)

print(f'Username : {userName}')  #f는 포맷의 약자
print(f'Userage : {userAge}') #변수는 중괄호로 묶는다 뼈대 - f'{}'
print(f'Username : {userName}, Userage : {userAge}')

print(f'Username :\t{userName}, \nUserage : {userAge}')

print('-'*40)

width = int(input('밑변길이 : '))
height = int(input('높이길이 : '))
triangle = width * height / 2

#1
print(f'밑변 : {width}, 높이 : {height}, 넓이(삼각) : {triangle}')

#2
print('밑변 :',width, end='')
print(', 높이 :',height, end='')
print(', 넓이(삼각) :',triangle)

