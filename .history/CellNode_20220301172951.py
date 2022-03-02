class Cell:
    def __init__(self,posX, posY, color):
        self.PosX = posX
        self.PosY = posY
        self.Color = color
        self.Next = None
        self.Prev = None

    def getPosX(self):
        return self.PosX
    
    def getPosY(self):
        return self.PosY

    def getColor(self):
        return self.Color

    def getNext(self):
        return self.Next

    def getPrev(self):
        return self.Prev
    
    def setPosX(self, posX):
        self.PosX = posX
    
    def setPosY(self, posY):
        self.PosY = posY

    def setColor(self, color):
        self.Color = color

    def setNext(self, cell):
       self.Next = cell

    def setPrev(self, cell):
        self.Prev = cell
