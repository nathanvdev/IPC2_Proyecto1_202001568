from PatternList import PatternList

class Floor:
    def __init__(self, name, row, column, flip, slide):
        self.Name = name
        self.Row = row
        self.Column = column
        self.FlipCost = flip
        self.SlideCost = slide
        self.Patrones = PatternList()
        self.Next = None


    def getName(self):
        return self.Name

    def getRow(self):
        return self.Row
    
    def getColumn(self):
        return self.Column
    
    def getFlipCost(self):
        return self.FlipCost
    
    def getSlideCost(self):
        return self.SlideCost
    
    def getPatrones(self):
        return self.Patrones
    
    def getNext(self):
        return self.Next

    def setName(self, name):
        self.Name = name

    def setRow(self, row):
        self.Row = row

    def setColumn(self, column):
        self.Column = column

    def setFlipCost(self, flipcost):
        self.FlipCost = flipcost

    def setSlideCost (self, slidecost):
        self.SlideCost = slidecost
    
    def setNext(self, floor):
        self.Next = floor
    
    def setPattern(self, code, patt):
        self.Patrones.addPattern(code, patt)

    def ShowFloor(self):
        print('Nombre del piso:', self.getName(), 'Costo por intercambiar', self.getSlideCost(), 'costo por Voltear un piso', self.getFlipCost())
