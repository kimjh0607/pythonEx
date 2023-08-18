
class Tv4K(NormalTv):

    def __init__(self, i, c, r='4k'):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTv = s