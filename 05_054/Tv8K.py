
class Tv8k(NormalTv):

    def __init__(self, i, c, r='8k'):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTv = s

    def setAiTv(self, a):
        self.aiTv = a