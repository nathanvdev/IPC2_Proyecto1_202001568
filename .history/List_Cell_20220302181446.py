from CellNode import Cell

class Cell_List():
    def __init__(self):
        self.First = None
        self.Last = None
        self.Size = 0

    def AddCell(self, PosX, PosY, Color):
        NewCell = Cell(PosX, PosY, Color)
        self.Size += 1
        if self.First is None:
            self.First = NewCell
            self.Last = NewCell
        else:
            self.Last.setNext(NewCell)
            NewCell.setPrev(self.Last)
            self.Last = NewCell

    def ShowCells(self):
        tmp = self.First
        while tmp is not None:
            print(tmp.Color, "(",tmp.getPosX(),",",tmp.getPosY(),")")
            tmp = tmp.getNext()


    def ChangePatt(self, Lista : Cell):
        pass