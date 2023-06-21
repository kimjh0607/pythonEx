'''
writelines()는 리스트 또는 튜플 데이터를 파일에 쓰기 위한 함수이다.
for문을 쓸 필요 없이 내부적으로 반복실행하여 리스트 튜플등의 데이터를 파일에 써준다.
'''
languages = ['c/c++', 'java', 'c#', 'python', 'javascript']
uri = 'C:/pythonTxt/'

with open(uri + 'languages.txt', 'a') as file:
    file.writelines(item + '\n' for item in languages)

with open(uri + 'languages.txt', 'r') as file:
    print(file.read())


