


class Cell:
    def __init__(self, posX, posY, color, code):
        self.PosX = posX
        self.PosY = posY
        self.Color = color
        self.Prev = None
        self.Next = None
        self.Block = False
        self.Code = code

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

    def setPrev(self, cell):
        self.Prev = cell

    def getNext(self):
        return self.Next
    
    def setNext(self, cell):
        self.Next = cell

    def BlockCell(self):
        self.Block = True

    def getBlock(self):
        return self.Block
    
    def ShowCells(self):
        print(self.getColor(), "(",self.getPosX(),",",self.getPosY(),")")

    
            