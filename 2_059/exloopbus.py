busA = 15
busB = 13
busC = 8

total = 60 * 17
for i in range(total+1):
    if i < 20 or i > (total-60):
        if i % busA == 0 and i % busB == 0:
            print('busA and busB, stop!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}시:{}분'.format(hour, min))
    else:
        if i % busA == 0 and i % busB == 0:
            print('busA and busB, stop!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}시:{}분'.format(hour, min))
        elif i % busA == 0 and i % busC == 0:
            print('busA and busC, stop!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}시:{}분'.format(hour, min))
        elif i % busB == 0 and i % busC == 0:
            print('busB and busC, stop!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}시:{}분'.format(hour, min))