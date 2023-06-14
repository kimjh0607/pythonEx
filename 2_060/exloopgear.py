gearACnt = int(input('enter gearA num : '))
gearBCnt = int(input('enter gearB num : '))

gearA = 0
gearB = 0
leastNum = 0

flag = True
while flag:

    if gearA != 0:
        if gearA != leastNum:
            gearA += gearACnt
        else:
            flag = False

    else:
        gearA += gearACnt

    if gearB != 0 and gearB % gearACnt == 0:
        leastNum = gearB
    else:
        gearB += gearBCnt


print('최초 만나는 톱니수(최소공배수) : {}'.format(leastNum))
print('gearA 회전 수 : {}'.format(int(leastNum/gearACnt)))
print('gearB 회전 수 : {}'.format(int(leastNum/gearBCnt)))