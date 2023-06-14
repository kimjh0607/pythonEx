year = int(input('enter year : '))

# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print('{} : Yoon'.format(year))
# else:
#     print('{} : Common'.format(year))

for year in range(2021, (2021+101)):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print('{} : Yoon'.format(year))
    else:
        print('{} : Common'.format(year))