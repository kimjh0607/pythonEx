'''
format() 함수
'''

userName = 'jay lee'
userAge = 23
print('User name : {}'.format(userName)) #중괄호{}안에 userName변수를 넣어주겠다. 라는 느낌
print('User age : {}'.format(userAge))

print('User name : {}, User age : {}'.format(userName, userAge)) #변수가 {}안에 순차적으로 들어감
print('User name : {1}, User age : {0}'.format(userName, userAge)) #인덱스 0,1(이경우엔)을 통해서 변수넣는 순서도 정할수있음

print('이름은 {}, 나이는 {}, {}라는 이름은 아버지가 지으심'.format(userName,userAge,userName))
print('이름은 {0}, 나이는 {1}, {0}라는 이름은 아버지가 지으심'.format(userName,userAge))#인덱스 사용

'''
형식문자열
%s 문자열 
%d 정수
%f 실수
'''

print('User name : %s' %userName)
print('User age : %d' %userAge)
print('User name : %s, User age : %d' %(userName,userAge))
print('Pi : %f' %3.14)
print('Pi : %d' %3.14)
print('Pi : %.1f' %3.14) #자릿수 정하기
print('Pi : %.3f' %3.14)

#실습
radius = float(input('반지름 입력 : ')) #입력받는 값을 담아두는 방식 기억하기.
pi = float(input('원주율 입력 : '))
cwidth = radius * radius * pi

print('radius : %f' %radius)
print('pi : %f' %pi)
print('width : %f' %cwidth)
print('='*40)
print('radius : %.0f, pi : %f' %(radius, pi))
print('radius : %.2f, pi : %.4f' %(radius, pi))
print('radius : %.2f, pi : %.2f' %(radius, pi))



