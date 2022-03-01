from PatternNode import Pattern


from PatternNode import Pattern

class PatternList():
    def __init__(self):
        self.first : Pattern = None
        self.last = None
        self.Size = 0

    def addPattern(self, code, patt):
        NewPatt = Pattern(code, patt)
        self.Size += 1
        if self.first is None:
            self.first = NewPatt
            self.last = NewPatt
        else:
            self.last.setNext(NewPatt)
            self.last = NewPatt
    
    def showPatterns(self):
        tmp = self.first
        for x in range(self.Size):
            print('codigo-',tmp.Code, 'patron-',tmp.Patt)