import datetime

dust = int(input('enter dust : '))
type = int(input('enter car type 1.comfort \t 2.business'))
cNum = int(input('enter car number : '))
curDate = datetime.datetime.now()
day = datetime.datetime.now().day

print('-' * 30)
print(curDate)
print('-' * 30)
if dust > 150 and type == 1:
    if day % 2 == cNum % 2:
        print('2부제')
        print('운행제한')
    else:
        print('운행가능')

if dust > 150 and type == 2:
    if day % 5 == cNum % 5:
        print('5부제')
        print('운행제한')
    else:
        print('운행가능')

if dust <= 150 :
    if day % 5 == cNum % 5:
        print('5부제')
        print('운행제한')
    else:
        print('운행가능')

print('-' * 30)

'''
File "C:\pythonEx\project\2_054\exif.py", line 38
    print('-' * 30)
                   ^
IndentationError: unindent does not match any outer indentation level
'''
#IndentationError : 들여쓰기 에러