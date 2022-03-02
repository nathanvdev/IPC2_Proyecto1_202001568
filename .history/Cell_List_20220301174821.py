from CellNode import Cell



class Cell_List():
    def __init__(self):
        self.First = None
        self.Last = None
        self.Size = 0

    def addCell(self, color, posX, posY):
        NewColor = Cell(posX, posY, color)
        self.Size += 1

        if self.First is None:
            self.First = NewColor
            self.Last = NewColor
        else:
            self.Last.setNext(NewColor)
            NewColor.setPrev(self.Last)
            self.Last = NewColor
            