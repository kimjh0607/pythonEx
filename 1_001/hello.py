str = 'Hello python'
print(str)
print('Hello')
print(1+1)

num = 10*10
print(num)

name = 'jake'
age = 30

print(f'My name is {name}, age is {age}')
print('My name is {}, age is {}'.format(name, age))
print('My name is %s, age is %d' %(name, age))

def add(a,b):
    return print(a+b)

add(10,12)

'''
함수정의
프린트 방법
'''
def greet(name):
    message = 'Hi~ ' + name + ' sir'
    return message

#1
print(greet('jake'))
#2
result = greet('jake')
print(result)

def greet2(name):
    return 'Hi~ ' + name + ' sir'

#1
print(greet2('jake'))
#2
result2 = greet2('jake')
print(result2)

print(f'name is {name}, age is {age}')
print('name is {}, age is {}'.format(name, age))
print('name is %s, age is %d' %(name, age))

def multi(a,b):
    print(a*b)

print(multi(4,4))

def greet():
    print("Hello, World!")

print(greet())
