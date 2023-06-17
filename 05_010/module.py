#모듈 써보기
#calculator 모듈
# import calculator
#
# calculator.add(10, 20)
# calculator.sub(10, 20)
# calculator.mul(10, 20)
# calculator.div(10, 20)

#로또머신모듈 lottoMachine
import lottoMachine
num = lottoMachine.getLottoNum()
print(f'lotto numbers : {num}')

#문자거꾸로출력 모듈 reverseStr
import reverseStr

inputString = input('enter User\'s String : ')
direct = reverseStr.reverseStr('apple')
var = reverseStr.reverseStr(inputString)
print(f'direct print : {direct}')
print(f'User\'s input print : {var}')