
ship1 = 3
ship2 = 4
ship3 = 5
maxDay = 0

for index in range(1, (ship1+1)):
    if ship1 % index == 0 and ship2 % index == 0:
        maxDay = index

minDay = (ship1 * ship2) // maxDay

newDay = minDay
for index in range(1, (newDay+1)):
    if newDay % index == 0 and ship3 % index == 0:
        maxDay = index

minDay = (newDay * ship3) // maxDay

print(f'minDay : {minDay}')
print(f'maxDay : {maxDay}')

from datetime import datetime
from datetime import timedelta

n = 1
baseTime = datetime(2023, 1, 1, 10, 0, 0) # 2021년 1월 1일 10시 0분 0초

with open('C:/pythonTxt/arrrive.txt', 'a') as f:
    f.write(f'2023년 모든 선박 입항일\n')
    f.write(f'{baseTime}\n')

nextTime = baseTime + timedelta(days=minDay)

while True:

    with open('C:/pythonTxt/arrrive.txt', 'a') as f:
        f.write(f'{nextTime}\n')

    nextTime = nextTime + timedelta(days=minDay)
    if nextTime.year > 2023 :
        break