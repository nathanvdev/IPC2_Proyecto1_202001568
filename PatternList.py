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
            print('codigo=',tmp.Code, 'patron-',tmp.Patt)
            tmp = tmp.getNext()

    def FindPatt(self, code):
        tmp = self.first
        for d in range(self.Size):
            if tmp.getCode() == code:
                print('codigo', tmp.getCode(), 'seleccionado')
                print('Patron:', tmp.getPatt())
                return tmp
            else:
                tmp = tmp.getNext()
        print('No se encontro el patron {}'.format(code))
        return None
        