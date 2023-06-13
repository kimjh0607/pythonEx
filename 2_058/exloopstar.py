#1
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()

#1+5
for i in range(1,6):
    for j in range(6-i,1,-1):
        print('*', end='')
    print()
print('-'*10)

#5
for i in range(1,10):
    if i < 6 :
        for j in range(i):
            print('*', end="")
    else:
        for j in range(10-i):
            print('*', end="")
    print()
print('-'*10)

#3
for i in range(1,6):
    for j in range(7-i,1,-1):
        print('*', end='')
    print()
print('-'*10)

#2
for i in range(1,6):
    for j in range(5-i,0,-1):
        print(' ', end='')
    print('*'*i)
print('-'*10)

#6
for i in range(1,6):
    for j in range(i):
        print(' ', end='')
    print('*')
print('-'*10)

#7
for i in range(1,6):
    for j in range(5-i,0,-1):
        print(' ', end='')
    print('*')
print('-'*10)

#4
for i in range(1,6):
    for j in range(0,i-1):
        print(' ', end='')
    print('*' * (6-i))
print('-'*10)

#8
for i in range(1,6):
    print(' ' * (5-i) + '*' * (1+(2*(i-1))))