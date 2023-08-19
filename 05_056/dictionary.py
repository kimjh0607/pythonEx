
from abc import ABCMeta
from abc import abstractmethod

class AbsDictionary(metaclass=ABCMeta):

    def __init__(self):
        self.wordDic = {}

    @abstractmethod
    def registWord(self, w1, w2):
        pass

    @abstractmethod
    def updateWord(self, w1, w2):
        pass
    
    @abstractmethod
    def removeWord(self, w1):
        pass
    
    @abstractmethod
    def searchWord(self, w1):
        pass


class KorToEng(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KorToEng] registWord(): {w1} to {w2}')
        self.wordDic[w1] = w2

    def updateWord(self, w1, w2):
        print(f'[KorToEng] updateWord(): {w1} to {w2}')
        self.wordDic[w1] = w2
    
    def removeWord(self, w1):
        print(f'[KorToEng] removeWord(): {w1}')
        del self.wordDic[w1]
    
    def searchWord(self, w1):
        print(f'[KorToEng] searchWord(): {w1}')
        return self.wordDic[w1]
    
    def printWords(self):
        for wordKey in self.wordDic.keys():
            print(f'{wordKey} : {self.wordDic[wordKey]}')


class KorToJpn(AbsDictionary):

    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KorToJpn] registWord(): {w1} to {w2}')
        self.wordDic[w1] = w2

    def updadteWord(self, w1, w2):
        print(f'[KorToJpn] updateWord(): {w1} to {w2}')
        self.wordDic[w1] = w2
    
    def updateWord(self, w1):
        print(f'[KorToJpn] removeWord(): {w1}')
        del self.wordDic[w1]
    
    def searchWord(self, w1):
        print(f'[KorToJpn] searchWord(): {w1}')
        return self.wordDic[w1]
    
    def printWords(self):
        for wordKey in self.wordDic.keys():
            print(f'{wordKey} : {self.wordDic[wordKey]}')
