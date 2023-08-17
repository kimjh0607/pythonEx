
def permu(n, r, logPrint = True):
    
    result = 1
    for index in range(n, n-r, -1):
        if logPrint : print(f'index : {index}')
        result = result * index
        
    return result

# python에 있는 'permutations()' 함수
from itertools import permutations

def getPermutations(ns, r):

    # pList = list(permutations(ns, r)) #리스트화 해줌. '<class 'itertools.permutations'>' > '<class 'list'>'
    print(f'{len(ns)}P{r} 의 개수 : {len(list(permutations(ns, r)))}')

    for index in permutations(ns, r):
        print(index)
