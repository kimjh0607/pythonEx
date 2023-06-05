n1 = 2
n2 = 10
res = n1 ** n2 #거듭제곱 연산자
print(res)

'''
제곱근구하기 
n의 m제곱근 공식
n ** (1/m)
'''
#2의 제곱근
res1 = 2**(1/2)
print(res1)

#9의 제곱근
res2 = 9**(1/2)
print(res2)

#5의 세제곱근
res3 = 5**(1/3)
print(res3)

'''
math모듈의 sqrt()와 pow()함수
import math
sqrt() - 제곱근만 구해준다 (세제곱근X 네제곱근X)
pow() - 거듭제곱 구해준다 math.pow(3,4) 3의 네제곱(=81)
'''
import math #math모듈 가져오기
print(math.sqrt(4)) #모듈.함수() 형태
print(math.pow(3,4))

#실습
#엄마에게 첫달 용돈을 200원 받고 매월 2배씩 12개월간 받는다고 했을때 최종으로 받는 돈은?
seed = 200
result = seed * (2**(12-1))
print('최종 :',result)
print(type(result))

strResult = format(result, ',') #천단위로 끊어주기
print(strResult,'원')
print(type(strResult))
