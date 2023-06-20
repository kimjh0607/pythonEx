class MidExam:
    def __init__(self, s1, s2, s3):
        print('[MidExam] __init__()')

        self.mid_kor_score = s1
        self.mid_eng_score = s2
        self.mid_math_score = s3

    def printScore(self):
        print(f'[korScore] : {self.mid_kor_score}')
        print(f'[engScore] : {self.mid_eng_score}')
        print(f'[mathScore] : {self.mid_math_score}')

class EndExam(MidExam):

    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[EndExam] __init__()')

        super().__init__(s1, s2, s3)

        self.end_kor_score = s4
        self.end_eng_score = s5
        self.end_math_score = s6

    def printScore(self):
        super().printScore()
        print(f'[korScore] : {self.end_kor_score}')
        print(f'[engScore] : {self.end_eng_score}')
        print(f'[mathScore] : {self.end_math_score}')

    def getTotal(self):
        total = self.mid_kor_score + self.mid_eng_score + self.mid_math_score
        total += self.end_kor_score + self.end_eng_score + self.end_math_score

        return total

    def getAverage(self):
        return self.getTotal() / 6

exam = EndExam(85, 90, 88, 75, 85, 95)
exam.printScore()

print(f'Total : {exam.getTotal()}')
print(f'Average : {round(exam.getAverage(), 2)}')