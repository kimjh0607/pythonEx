
import mem as m

memName = input('이름 입력 : ')
memMail = input('메일 입력 : ')
memPassword = input('패스워드 입력 : ')
memAddress = input('주소 입력 : ')
memPhoneNumber = input('폰번호 입력 : ')

try:
    m.inputDataCheck(memName, memMail, memPassword, memAddress, memPhoneNumber)
    member = m.RegistMember(memName, memMail, memPassword, memAddress, memPhoneNumber)
    member.printMemberInfo()
except m.MemberEmptyException as e:
    print(e)

