'''
if else 양자택일
'''
passScore = 80
myScore = int(input('점수 입력 : '))

#1
# if myScore >= passScore:
#     print('PASS')
# if myScore < passScore:
#     print('FAIL')

#2
if myScore >= passScore:
    print('PASS')
else:
    print('FAIL')

'''
pass 키워드
'''
if myScore >= passScore:
    pass #나중에 코딩하겠다 - 없으면 에러
else:
    pass #없으면 에러

#실습
floatNum = 3.14

if floatNum - int(floatNum) >=0.5:
    print('올림 ',int(floatNum)+1)
else:
    print('버림 ',int(floatNum))
