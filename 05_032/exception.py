'''
Exception 클래스
'''
# num1 = int(input('enter number : '))
# num2 = int(input('enter number : '))
#
# try:
#     print(f'num1 + num2 = {num1 + num2}')
# except Exception as e:
#     print('0으로 나눌 수 없습니다.')
#     print(f'exception : {e}')
#
# print(f'num1 * num2 = {num1 * num2}')
# print(f'num1 - num2 = {num1 - num2}')
# print(f'num1 / num2 = {num1 / num2}') #num2이 '0'일 떄

# def divCal(n1, n2):
#
#     if n2 != 0:
#         print(f'{n1} / {n2} = {n1 / n2}')
#     else:
#         raise Exception('0으로 나눌 수 없다!!!!')
#
# num1 = int(input('enter number1 : '))
# num2 = int(input('enter number2 : '))
#
# try:
#     divCal(num1, num2)
# except Exception as e:
#     print(f'Exception : {e}')

#실습
def sendSMS(msg):

    if len(msg) > 10:
        raise Exception('길이초과!! MMS전환 후 발송!!', 1)

    else:
        print('SMS 발송!!')

def sendMMS(msg):

    if len(msg) <= 10:
        raise Exception('길이미달!! SMS전환 후 발송!!', 2)
    else:
        print('MMS 발송!!')

msg = input('enter message : ')

try:
    sendSMS(msg)
except Exception as e:
    print(f'exception : {e.args[0]}')
    print(f'exception : {e.args[1]}')

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)