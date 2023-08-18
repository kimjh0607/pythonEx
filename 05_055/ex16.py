import book as bk

bookList = bk.BookRepository()

bookList.registBook(bk.Book('python', 20000, '1234567890'))
bookList.registBook(bk.Book('java', 25000, '43218765'))
bookList.registBook(bk.Book('c++', 27000, '12387698'))
print('-' * 30)

bookList.printBooksInfo()
bookList.printBookInfo('1234567890')
bookList.printBookInfo('12387698')
print('-' * 30)

bookList.removeBook('1234567890')
bookList.printBooksInfo()
print('-' * 30)

myBookList = bk.BookRepository()

myBookList.registBook(bk.Book('php', 18000, '121567890'))
myBookList.registBook(bk.Book('html', 22000, '43289765'))
myBookList.registBook(bk.Book('ruby', 33000, '1224577698'))

myBookList.printBookInfo('121567890')
myBookList.printBooksInfo()
print('-' * 30)

myBookList.removeBook('43289765')
myBookList.printBooksInfo()
