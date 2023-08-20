
class MemberEmptyException(Exception):

    def __init__(self, what):
        super().__init__(f'{what} is empty!!')


def inputDataCheck(n, m, p, a, ph):

    if n == '':
        raise MemberEmptyException('name')
    elif m == '':
        raise MemberEmptyException('mail')
    elif p == '':
        raise MemberEmptyException('password')
    elif a == '':
        raise MemberEmptyException('address')
    elif ph == '':
        raise MemberEmptyException('phone_number')
    

class RegistMember():

    def __init__(self, n, m, p, a, ph):
        self.name = n
        self.mail = m
        self.password = p
        self.address = a
        self.phoneNumber = ph
        print('Membership registration completed')
    
    def printMemberInfo(self):
        print(f'name : {self.name}')
        print(f'mail : {self.mail}')
        print(f'password : {self.password}')
        print(f'address : {self.address}')
        print(f'phoneNumber : {self.phoneNumber}')
