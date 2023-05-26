'''
비교연산자
'''
cha1 = 'A' #65
cha2 = 's' #83
print('\'{}\' > \'{}\' : {}'.format(cha1, cha2, (cha1>cha2)))
print('\'{}\' >= \'{}\' : {}'.format(cha1, cha2, (cha1>=cha2)))
print('\'{}\' < \'{}\' : {}'.format(cha1, cha2, (cha1<cha2)))
print('\'{}\' <= \'{}\' : {}'.format(cha1, cha2, (cha1<=cha2)))
print('\'{}\' == \'{}\' : {}'.format(cha1, cha2, (cha1==cha2)))
print('\'{}\' != \'{}\' : {}'.format(cha1, cha2, (cha1!=cha2)))

'''
ord() 함수
chr() 함수
'''
print('\'A\' -> {}'.format(ord('A')))
print('\'s\' -> {}'.format(ord('s')))
print('65 -> {}'.format(chr(65)))
print('115 -> {}'.format(chr(115)))

s1 = 'Hello'
s2 = 'hello'

print('{} == {} : {}'.format(s1 , s2, (s1==s2)))
print('{} != {} : {}'.format(s1 , s2, (s1!=s2)))

string = input('문자입력 : ')
print(f'문자  : {string} 코드값 : {ord(string)}')

