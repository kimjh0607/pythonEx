
def getCombinationCnt(n, r, logPrint = True):
    resP = 1
    resR = 1
    resC = 1

    for index in range(n, (n-r), -1):
        resP *= index
    if logPrint : print(f'result P : {resP}')

    for index in range(r, 0, -1):
        resR *= index
    if logPrint : print(f'result R : {resR}')
    
    resC = int(resP / resR)
    if logPrint : print(f'result C : {resC}') #logPrint의 T/F로 중간 값들을 확인해 볼 수도 있다.
    
    return resC

# itertools 모듈 사용
from itertools import combinations

def getCombinations(ns, r):
    cList = list(combinations(ns, r))
    print(f'{len(ns)}C{r}의 값 : {len(cList)}') # nCr 값만 확인
    
    for index in cList:
        print(f'{index}')