class Book:

    def __init__(self, n, p, i):
        self.bName = n
        self.bPrice = p
        self.bIsbn = i

class BookRepository():

    def __init__(self):
        self.bDic = {} #담을 자료구조 딕셔너리로 생성

    def registBook(self, b):
        self.bDic[b.bIsbn] = b

    def removeBook(self, i):
        del self.bDic[i]

    def printBooksInfo(self):
        for isbnIndex in self.bDic.keys():
            b = self.bDic[isbnIndex]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')

    def printBookInfo(self, i):
        if i in self.bDic:
            b = self.bDic[i]
            print(f'{b.bName}, {b.bPrice}, {b.bIsbn}')
        else:
            print('Lookup result does not exist')
