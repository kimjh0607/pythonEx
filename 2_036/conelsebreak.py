#break 실습
sum = 0
search = 0

for i in range(100):
    sum+=i

    if sum>100:
        search = i
        break
print('searchNumber : {}'.format(search))

result = 1
num = 0
for i in range(1, 11):
    result *= i
    if result > 50:
        num = i
        break
print('num : {}, result : {}'.format(num, result))