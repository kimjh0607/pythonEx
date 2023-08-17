
import permutation as pt

# n = int(input('n 입력 : '))
# r = int(input('r 입력 : '))

# print(f'{n}P{r} = {pt.permu(n,r,logPrint=False)}') #개수만 출력하기

plist = [1, 2, 3, 4, 5, 6, 7, 8]
var = 3

pt.getPermutations(plist, var) #경우의 수 모두 확인하기

# print(type(list(pt.permutations(plist, var))))