'''
str[0] - str에 저장된 문자열에서 인덱스값에 따른 문자반환
'''

name = input('이름입력 : ')
mail = input('메일입력 : ')
id = input('아디입력 : ')
pw = input('비번입력 : ')
privateNum1 = input('주민앞입력 : ')
privateNum2 = input('주민뒤입력 : ')
address = input('주소입력 : ')

print('-'*30)
print(f'{name}')
print(f'{mail}')
print(f'{id}')
pwstr = '*'*len(pw)
print(f'{pwstr}')
privatestr = privateNum2[0] + '*' * 6
print(f'{privateNum1} - {privatestr}')
print(f'{address}')
print('-' * 30)
