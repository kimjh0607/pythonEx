import dictionary as dic

kTe = dic.KorToEng()

kTe.registWord('책', 'bok')
kTe.registWord('나비', 'butterfly')
kTe.registWord('연필', 'pencil')
kTe.registWord('학생', 'student')
kTe.registWord('선생님', 'teacher')

kTe.printWords()
print('-' * 30)
kTe.updateWord('책', 'book')
print('-' * 30)

print(f' 연필 : {kTe.searchWord("연필")}')
print(f' 나비 : {kTe.searchWord("나비")}')
print(f' 선생님 : {kTe.searchWord("선생님")}')
print('-' * 30)

kTe.removeWord('학생')
kTe.printWords()