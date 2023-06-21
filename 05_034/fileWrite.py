'''
open(디렉토리, 쓰기('w') / 읽기) - 파일 열기
read() - 파일 읽기
write() - 파일 쓰기
close() - 파일 닫기
를 이용한 텍스트 파일 다루기
'''
#reference variable 'file'
file = open('C:/pythonTxt/text.txt', 'w') #파일이 없으면 생성 있으면 열기

file.write('Hello Python!!!!')
#print(f'글자수 : {strCnt}')

file.close()

import time

lt = time.localtime()
dateStr = '[ ' + str(lt.tm_year) + '년 ' + \
          str(lt.tm_mon) + '월 ' + str(lt.tm_mday) + '일 ] '

todaySchedule = input('enter Schedule : ')

file = open('C:/pythonTxt/test.txt', 'w')
file.write(dateStr + todaySchedule)
file.close()
