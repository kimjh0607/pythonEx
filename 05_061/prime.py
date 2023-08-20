
class NotPrimeException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 소수가 아닙니다.')


class PrimeException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 소수입니다.')


def isPrime(num):
    flag = True
    for index in range(2, num):
        if num % index == 0:
            flag = False
            break
    
    if flag == False:
        raise NotPrimeException(num)
    else:
        raise PrimeException(num)
        