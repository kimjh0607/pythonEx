
import member as mb

mems = mb.MemberRepository()

for index in range(3):
    mId = input('ID 입력 : ')
    mPw = input('PW 입력 : ')
    
    mem = mb.Member(mId, mPw)
    mems.addMember(mem)

mems.printMember()

mems.loginMember('abc@naver.com', '123')
mems.loginMember('qwe@gmail.com', '456')
mems.loginMember('zxc@daum.net', '677')

mems.removeMember('zxc@daum.net', '678')

mems.printMember()