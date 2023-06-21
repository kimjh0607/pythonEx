'''
finally - 예외 발생과 상관없이 항상 실행한다.
try ~ except ~ else ~ finally
'''
# try:
#     inputData = input('enter num : ')
#     numInt = int(inputData)
# except:
#     print('exception raise!!!')
#     print('not number')
# else:
#     if numInt % 2 == 0:
#         print('even number!!')
#     else:
#         print('odd number!!')
# finally:
#     print(f'Data = {inputData}')

#실습
evenList = []; oddList = []; floatList = []; dataList = []

n = 1
while n < 6:

    try:
        data = input('enter number : ')
        floatNum = float(data)
    except:
        print('exception raise!!!')
        print('not number')
        #continue

    else:
        if floatNum - int(floatNum) != 0:
            print('float Num!!')
            floatList.append(floatNum)
        else:
            if floatNum % 2 == 0:
                print('even number!!')
                evenList.append(floatNum)
            else:
                print('odd Number!!')
                oddList.append(floatNum)
    finally:
        dataList.append(data)

    n += 1

print(f'floatList = {floatList}')
print(f'evenList = {evenList}')
print(f'oddList = {oddList}')
print(f'dataList = {dataList}')