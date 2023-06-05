#input() data입력
#input데이터의 default는 string형이어서 이용시 맞는 타입변환을 해주어야함
#print() data출력
#print('keyboard input data')

# userInputData = input('press input data')
# print(userInputData)
#
data1 = input('문자형 데이터를 입력 ')
print(data1)
print(type(data1))

data2 = input('실수형 데이터를 입력 ')
print(data2)
print(type(data2))

data3 = input('정수형 데이터를 입력 ')
print(data3)
print(type(data3))

data4 = input('논리형 데이터를 입력 ')
print(data4)
print(type(data4))
#
# userInputData = int(input('자료입력'))
# print(userInputData)
# print(type(userInputData))
#
# todayWeather = input('오늘 날씨 입력')
# print(todayWeather)
# print(type(todayWeather))
# print('데이터를 입력해주세요')
garo = int(input('밑변 입력'))
saero = int(input('높이 입력'))
print('사각형넓이 :' , (garo * saero))
print('삼각형넓이 :' , (garo * saero)/2)

