
first = int(input('1과목 점수 입력 : '))
second = int(input('2과목 점수 입력 : '))
third = int(input('3과목 점수 입력 : '))
fourth = int(input('4과목 점수 입력 : '))
fifth = int(input('5과목 점수 입력 : '))

total = first + second + third + fourth + fifth
avg = total / 5

if first >= 40 and second >= 40 and third >= 40 and fourth >= 40 and fifth >= 40 and total >= 60 :
    print(f'{first} : Pass')
    print(f'{second} : Pass')
    print(f'{third} : Pass')
    print(f'{fourth} : Pass')
    print(f'{fifth} : Pass')
    print(f'총점 : {total}')
    print(f'평균 : {avg}')
    print('Final Pass!!')
else:
    if first >= 40:
        print(f'{first} : Pass')
    else:
        print(f'{first} : Fail')

    if second >= 40:
        print(f'{second} : Pass')
    else:
        print(f'{second} : Fail')

    if third >= 40:
        print(f'{third} : Pass')
    else:
        print(f'{third} : Fail')

    if fourth >= 40:
        print(f'{fourth} : Pass')
    else:
        print(f'{fourth} : Fail')

    if fifth >= 40:
        print(f'{fifth} : Pass')
    else:
        print(f'{fifth} : Fail')

    print(f'총점 : {total}')
    print(f'평균 : {avg}')
    print('Final Fail!!')

