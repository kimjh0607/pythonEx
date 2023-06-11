base = 29
step = 60
stepPerDesc = 0.8

height = int(input('press height(m) : '))
curTemp = base - ((height // step) * stepPerDesc)
if height % step != 0:
    curTemp -= stepPerDesc

print('current temprature : %.2f' %(curTemp))

bread = 197
milk = 152
breadd = divmod(197, 17)
milkd = divmod(152, 17)

print('한명이 갖는 빵개수{}, 남는갯수{}'.format(breadd[0], breadd[1]))
print('한명이 갖는 우유개수{}, 남는갯수{}'.format(milkd[0], milkd[1]))