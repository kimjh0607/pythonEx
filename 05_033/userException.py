'''
사용자 예외클래스
Exception 클래스를 상속해서 사용자 에외 클래스를 만들 수 있다.
'''
# class NotUseZeroException(Exception): #사용자 예외클래스는 무조건 Exception 클래스를 상속
#
#     def __init__(self, n):
#         super().__init__(f'{n}은 사용할 수 없습니다.')
#
# def divCal(n1, n2):
#
#     if n2 == 0:
#         raise NotUseZeroException(n2)
#     else:
#         print(f'{n1} / {n2} = {n1 / n2}')
#
# num1 = int(input('enter Number1 : '))
# num2 = int(input('enter Number2 : '))
#
# try:
#     divCal(num1, num2)
# except NotUseZeroException as e:
#     print(e)

class PwShortException(Exception):
    def __init__(self, str):
        super().__init__(f'{str} : 길이 5 미만!!')

class PwLongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str} : 길이 10 초과!!')

class PwWrongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str} : Password 틀림!!')

adminPw = input('enter Admin Password : ')

try:
    if len(adminPw) < 5:
        raise PwShortException(adminPw)
    elif len(adminPw) > 10:
        raise PwLongException(adminPw)
    elif adminPw != 'admin1234':
        raise PwWrongException(adminPw)
    elif adminPw == 'admin1234':
        print('확인!!')

except PwShortException as e1:
    print(e1)
except PwLongException as e2:
    print(e2)
except PwWrongException as e3:
    print(e3)
