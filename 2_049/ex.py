import datetime
born = int(input('press when were you born : '))
age = datetime.datetime.now().year - born
if age <= 19  or age >= 65:
    if age % 5 == 0:
        print('Friday possible')
    if age % 5 == 1:
        print('Monday possible')
    if age % 5 == 2:
        print('Tuesday possible')
    if age % 5 == 3:
        print('Wednesday possible')
    if age % 5 == 4:
        print('Thursday possible')
else:
    print('check next schedule')
