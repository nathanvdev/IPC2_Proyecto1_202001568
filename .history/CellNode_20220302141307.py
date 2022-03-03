from this import d


class Cell:
    def __init__(self, posX, posY, color):
        self.PosX = posX
        self.PosY = posY
        self.Color = color
        self.Prev = None
        self.Next = None

    def getPosX(self):
        return self.PosX
    
    def setPosX(self, posX):
        self.PosX = posX

    def getPosY(self):
        return self.PosY

    def setPosY(self, posY):
        self.PosY = posY

    def getColor(self):
        return self.Color

    def setColor(self, color):
        self.Color = color
    
    def getPrev(self):
        return self.Prev

    def getPrev(self, cell):
        self.Prev = cell

    def getNext(self):
        return self.Next
    
    def setNext(self, cell):
        self.Next = cell