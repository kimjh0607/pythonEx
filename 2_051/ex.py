kor = int(input('enter korScore : '))
eng = int(input('enter engScore : '))
math = int(input('enter mathScore : '))
sci = int(input('enter sciScore : '))
his = int(input('enter hisScore : '))

total = kor + eng + math + sci + his
avg = total / 5
kordev = int(kor - avg)
engdev = int(eng - avg)
mathdev = int(math - avg)
scidev = int(sci - avg)
hisdev = int(his - avg)

print('total : {}, avg : {}'.format(total, avg))
print('kor :{}({}), eng :{}({}), math :{}({}), sci :{}({}), his :{}({}),'.format(kor,kordev,eng,engdev,math,mathdev,sci,scidev,his,hisdev))
print('-' * 60)
if kordev >= 0:
    print('kordev : ','+' * kordev,(kordev))
else:
    print('kordev : ','-' * abs(kordev),(kordev))

if engdev >= 0:
    print('engdev : ','+' * engdev,(engdev))
else:
    print('engdev : ','-' * engdev,(engdev))

if mathdev >= 0:
    print('mathdev : ','+' * mathdev,(mathdev))
else:
    print('mathdev : ','-' * mathdev,(mathdev))

if scidev >= 0:
    print('scidev : ','+' * scidev,(scidev))
else:
    print('scidev : ','-' * scidev,(scidev))

if hisdev >= 0:
    print('hisdev : ','+' * hisdev,(hisdev))
else:
    print('hisdev : ','-' * abs(hisdev),(hisdev))
print('-' * 60)

