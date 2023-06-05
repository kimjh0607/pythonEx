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
ord() - 함수 문자를 정수로
chr() - 함수 십진수를 문자로
'''
print('\'A\' -> {}'.format(ord('A')))
print('\'S\' -> {}'.format(ord('S')))
print('65 -> {}'.format(chr(65)))
print('115 -> {}'.format(chr(115)))

#문자열 비교는 '같다, 같지않다'만 판별가능
s1 = 'Hello'
s2 = 'hello'

print('{} == {} : {}'.format(s1 , s2, (s1==s2)))
print('{} != {} : {}'.format(s1 , s2, (s1!=s2)))

#실습
#문자입력후 아스키코드로 출력하기
#아스키코드입력후 문자로 출력하기
string = input('문자입력 : ')
print(f'문자  : {string}, 아스키코드값 : {ord(string)}')

int = int(input('아스키코드입력 : '))
print(f'아스키코드값  : {int}, 문자 : {chr(int)}')
