'''
read() 함수
read(디렉토리, 읽기)
'''
# file = open('C:/pythonTxt/test.txt', 'r')
#
# str = file.read()
# print(f'내용 : {str}')
#
# file.close()

# import time
#
# lt = time.localtime()
# # dateStr = '[ ' + str(lt.tm_year) + '년 ' + \
# #           str(lt.tm_mon) + '월 ' + str(lt.tm_mday) + '일 ] '
#
# dateStr = '[' + time.strftime('%Y-%m-%d %H:%M:%S %p') + ']'
#
# todaySchedule = input('enter Today\'s Schedule : ')
#
# file = open('C:/pythonTxt/test.txt', 'w')
# file.write(dateStr + todaySchedule)
# file.close()

file = open('C:/pythonTxt/about_python.txt', 'r', encoding='UTF8') #엔코딩에러

str = file.read()
print(f'내용 : {str}')

file.close()

str = str.replace('Python', '파이썬', 2) #두번째까지만
print(f'내용 : {str}')

file = open('C:/pythonTxt/about_python.txt', 'w')
file.write(str)
file.close()