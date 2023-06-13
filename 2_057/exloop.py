fNum = int(input('press int : '))

addSum = 0
for i in range(1, (fNum+1)):
    addSum += i

addSumFormated = format(addSum, ',')
print('Sum : {}'.format(addSumFormated))

oddSum = 0
for i in range(1, (fNum+1)):
    if i % 2 != 0:
        oddSum += i

oddSumFormated = format(oddSum, ',')
print('Odd Sum : {}'.format(oddSumFormated))

evenSum = 0
for i in range(1, (fNum+1)):
    if i % 2 == 0:
        evenSum += i

evenSumFormated = format(evenSum, ',')
print('even Sum : {}'.format(evenSumFormated))

factorialResult = 1
for i in range(1, (fNum+1)):
    factorialResult *= i

factorialResultFormated = format(factorialResult, ',')
print('Factorial Result : {}'.format(factorialResultFormated))
