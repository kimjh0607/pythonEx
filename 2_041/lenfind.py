'''
len() function
'''

msg = input('메세지 입력 : ')
print('메세지 문자열 길이 : {}'.format(len(msg)))

'''
find()
'''
article = '파이썬[3](영어: Python)은 1991년[4] 네덜란드계 소프트웨어 엔지니어인 ' \
          '귀도 반 로섬[5]이 발표한 고급 프로그래밍 언어로, 플랫폼에 독립적이며 ' \
          '인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. ' \
          '파이썬이라는 이름은 귀도가 좋아하는 코미디인〈Monty Python\'s Flying Circus〉에서 따온 것이다.'
string = article.find('객체지향')
print('\'객체지향\' 의 위치 : {}'.format(string))