limit = 30
Amount = int(input('적설량 입력 : '))

print('적설량 : {}mm , {}'.format(Amount, '대설경보')) if Amount>=limit else \
    print('적설량 : {}mm , {}'.format(Amount, '대설경보아님'))

kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))
math = int(input('수학점수 입력 : '))
avg = (kor+eng+math) / 3

print('국어합격') if kor>=60 else print('국어불합격')
print('영어합격') if eng>=60 else print('영어불합격')
print('수학합격') if math>=60 else print('수학불합격')
print('최종합격') if avg>=70 and kor>=60 and eng>=60 and math>=60 else print('최종불합격')