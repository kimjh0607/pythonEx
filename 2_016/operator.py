n1 = 2
n2 = 10
res = n1 ** n2
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
sqrt() - 제곱근만 구해준다 (세제곱근 네제곱근X)
pow() - 거듭제곱 구해준다 math.pow(3,4) 3의 네제곱(=81)
'''
import math
print(math.sqrt(4))
print(math.pow(3,4))
