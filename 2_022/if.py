'''
A if 조건식 else B
조건식의 결과가 True이면 A실행, 그렇지 않으면 B실행
True 앞 False 뒤

if문 단일조건
if ~else문 양자택일
if ~elif문 다자택일

if문(단일)
if 조건식: - 콜론찍기 , 조건은 and 등을 써서 병행가능
    실행문 - 코드블럭 탭들여쓰기
false라면 실행안하고 그냥 넘어간다


'''

n1 = 10
n2 = 100

numRes = True if n1 > n2 else False
#3항 연산자 같은것임.
print('n1은 n2보다 크다.') if numRes else print('n1은 n2보다 작다.')
#풀어쓰면 아래

# if numRes:
#     print('n1은 n2보다 크다.')
# else:
#     print('n1은 n2보다 작다.') 

print('n1 > n2 : {}'.format(numRes))

print('\'n1은 n2보다 크다.\'') if numRes else print('\'n1은 n2보다 작다.\'')

kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))
math = int(input('수학점수 입력 : '))
avg = (kor+eng+math) / 3

if avg >=90:
    print('참잘했어요')

