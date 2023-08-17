


from random import randint

myList = []
for index in range(6):
    num = int(input('번호(1~45) 입력 : '))
    myList.append(num)

ranList = []
for index in range(6):
    rNum = randint(1,45)
    ranList.append(rNum)

matchList = []
for index1 in myList:
    for index2 in ranList:
        if index1 == index2:
            matchList.append(index2)

if len(matchList) == 6:
    print('당첨')
    print(f'맞춘 번호 : {matchList}')
else:
    print('다음 기회에')
    print(f'맞춘 번호 : {matchList}')


