
class Member():

    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

class MemberRepository():

    def __init__(self):
        self.members = {}

    def addMember(self, mem):
        self.members[mem.id] = mem.pw

    def loginMember(self, id, pw):
        isMember = id in self.members

        if isMember and self.members[id] == pw:
            print(f'{id} : log-in success!!!')
        else:
            print(f'{id} : log-in fail!!!')

    def removeMember(self, id, pw):
        del self.members[id]

    def printMember(self):
        for mKey in self.members.keys():
            print(f'ID : {mKey}')
            print(f'PW : {self.members[mKey]}')