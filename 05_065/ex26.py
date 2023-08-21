import diary

members = {}
uri = 'C:/pythonTxt/'

def printMembers():
    for memIndex in members.keys():
        print(f' ID : {memIndex} \t PW : {members[memIndex]}')


while True:
    selectNum = int(input('1.회원가입 2.한줄일기쓰기 3.일기보기 4.종료'))

    if selectNum == 1:
        mId = input('enter ID : ')
        mPw = input('enter password : ')
        members[mId] = mPw
        printMembers()

    elif selectNum == 2:
        mId = input('enter ID : ')
        mPw = input('enter password : ')

        if mId in members and members[mId] == mPw:
            print(f'Log in Success!!')
            fileName = 'myDiary_' + mId + '.txt'
            data = input('오늘의 일기를 기록하세요.')
            diary.writeDiary(uri, fileName, data)

        else:
            print('Log in Fail!!')
            printMembers()

    elif selectNum == 3:
        mId = input('enter ID : ')
        mPw = input('enter PW : ')

        if mId in members and members[mId] == mPw : 
            print('Log in Success!!')
            fileName = 'myDiary_' + mId + '.txt'
            datas = diary.readDiary(uri, fileName)
            for data in datas:
                print(data, end='')


        else:
            print('Log in Fail!!')
            printMembers()

    elif selectNum == 4:
        print('Bye~~~~')
        break
