
def babyFee(n,d):
    result1 = 18000 * n
    result2 = 18000 * d * 0.5
    return [result1, result2]

def childFee(n,d):
    result1 = 25000 * n
    result2 = 25000 * d * 0.5
    return [result1, result2]

def adultFee(n,d):
    result1 = 50000 * n
    result2 = 50000 * d * 0.5
    return [result1, result2]

inputBaby = int(input('유아 입력 : '))
disBaby = int(input('할인대상 유아 입력 : '))
inputChild = int(input('소아 입력 : '))
disChild = int(input('할인대상 소아 입력 : '))
inputAdult = int(input('성인 입력 : '))
disAdult = int(input('할인대상 성인 입력 : '))

b = babyFee(inputBaby,disBaby)
c = childFee(inputChild,disChild)
a = adultFee(inputAdult,disAdult)

sumPeo = inputBaby + disBaby + inputChild + disChild + inputAdult + disAdult
list = babyFee(inputBaby,disBaby) + childFee(inputChild,disChild) + adultFee(inputAdult,disAdult)

sumPri = 0
for index in list:
    sumPri += index

print('='*30)
print(f'유아 {inputBaby}명 요금 : {b[0]}원')
print(f'유아 할인대상 {disBaby}명 요금 : {b[1]}원')
print(f'소인 {inputChild}명 요금 : {c[0]}원')
print(f'소인 할인대상 {disChild}명 요금 : {c[1]}원')
print(f'성인 {inputAdult}명 요금 : {a[0]}원')
print(f'성인 할인대상 {disAdult}명 요금 : {a[1]}원')
print('='*30)
print(f'Total : {sumPeo}명')
print(f'TotalPrice : {sumPri}원')
print('='*30)
