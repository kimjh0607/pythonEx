
#실행파일

import utilityBill as ub

inputIncome = int(input('수입입력 : '))
ub.setIncome(inputIncome)

inputWaterPrice = int(input('수도입력 : '))
ub.setWaterPrice(inputWaterPrice)

inputEletricPrice = int(input('전기입력 : '))
ub.setEletricPrice(inputEletricPrice)

inputGasPrice = int(input('가스입력 : '))
ub.setGasPrice(inputGasPrice)

print(f'공과금 Total : {ub.getUtilityBill()}원')
print(f'수입대비 공과금률 : {ub.getUtilityBillRate()}%')
