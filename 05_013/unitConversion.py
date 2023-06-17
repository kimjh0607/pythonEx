def cmToMm(n):
    return round(n * 10, 3)

def cmToInch(n):
    return round(n * 0.393, 3)

def cmToM(n):
    return round(n * 0.01, 3)

def cmToFt(n):
    return round(n * 0.032, 3)

if __name__ == '__main__': #느낌이, 다른 파일에서 모듈로 쓰일 때 부분적으로 제공할 수 있다는 느낌?
    print(f'10cm : {cmToMm(10)}mm')
    print(f'10cm : {cmToInch(10)}inch')
    print(f'10cm : {cmToM(10)}M')
    print(f'10cm : {cmToFt(10)}ft')
