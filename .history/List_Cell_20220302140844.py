
class Cell_List():
    def __init__(self):
        self.First = None
        self.Last = None
        self.size = 0

    def AddCell(self, Cell):
        NewCell = Cell()
        if self.First is None:
