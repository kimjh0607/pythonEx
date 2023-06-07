'''
중첩조건문
조건문안에 또 다른 조건문이 있을 수 있다.
'''

Score = int(input('시험 성적 입력 : '))

if Score < 60:
    print('재시험대상')
else:
    if Score >= 90:
        print('A')
    elif Score >= 80:
        print('B')
    elif Score >= 70:
        print('C')
    elif Score >= 60:
        print('D')

#실습
selectNum = int(input('출퇴근 대상자 인가요? 1. Yes \t 2. No'))

if selectNum == 1:
    print('교통수단을 선택하세요.')
    trans = int(input('1.도보 자전거 \t 2.버스,지하철 \t 3.자가용'))

    if trans == 1:
        print('세금 감면 5%')
    elif trans == 2:
        print('세금 감면 3%')
    elif trans == 3:
        print('세금 감면 1%')
elif selectNum == 2:
    print('세금 변동 없습니다.')
else:
    print('잘못 입력했습니다.')