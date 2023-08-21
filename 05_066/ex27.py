import time

def getTime():
    lt = time.localtime()
    st= time.strftime('%Y-%m-%d %H:%M:%S')
    return st

while True:

    selectNum = int(input('1.입금\t2.출금\t3.종료'))

    if selectNum == 1:
        money = int(input('입금액 입력 : '))
        with open('C:/pythonTxt/bank/money.txt', 'r') as f:
            m = f.read()

        with open('C:/pythonTxt/bank/money.txt', 'w') as f: #갱신이기때문에 a가 아니라 w
            f.write(str(int(m) + money))

        memo = input('입금 내역 입력 : ')
        with open('C:/pythonTxt/bank/pocketMoneyRegister.txt', 'a') as f:
            f.write('-------------------------------------------\n')
            f.write(f'{getTime()} \n')
            f.write(f'[입금] {memo} : {str(money)}원 \n')
            f.write(f'[잔액] : {str(int(m) + money)}원 \n')
            
        print('입금 완료!!')
        print(f'기존 잔액 : {m}')
        print(f'입금 후 잔액 : {int(m)+money}')

    elif selectNum == 2:
        money = int(input('출금액 입력 : '))
        with open('C:/pythonTxt/bank/money.txt', 'r') as f:
            m = f.read()

        with open('C:/pythonTxt/bank/money.txt', 'w') as f: #갱신이기때문에 a가 아니라 w
            f.write(str(int(m) - money))

        memo = input('출금 내역 입력 : ')
        with open('C:/pythonTxt/bank/pocketMoneyRegister.txt', 'a') as f:
            f.write('-------------------------------------------\n')
            f.write(f'{getTime()} \n')
            f.write(f'[출금] {memo} : {str(money)}원 \n')
            f.write(f'[잔액] : {str(int(m) - money)}원 \n')
            
        print('출금 완료!!')
        print(f'기존 잔액 : {m}')
        print(f'출금 후 잔액 : {int(m) - money}')
    elif selectNum == 3:
        print('Bye~~~')
        break
    else:
        print('다시 입력하세요~!')