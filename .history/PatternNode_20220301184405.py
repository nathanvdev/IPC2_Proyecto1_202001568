from Cell_List import Cell_List


class Pattern:
    def __init__(self, code, patt, column, row) -> None:
        self.Code = code
        self.Patt = patt
        self.Cells = Cell_List()
        self.C = column
        self.R = row
        self.Next = None

    def setCode(self, code):
        self.Code = code

    def getPatt(self):
        return self.Patt
    
    def setPatt(self, patt):
        self.Patt = patt

    def getCode(self):
        return self.Code
    
    def setNext(self, Pattern):
        self.Next = Pattern

    def CreateCells(self):
        PosX = 0
        PosY = 1
        for c in self.Patt:
            if PosX < self.C:
                PosX += 1
                self.Cells.addCell(c,PosX,PosY)
            else:
                PosY += 1
                PosX = 1
                if PosY > self.R:
                    print('el color',"'",c,"'",'ya no cabe dentro del patron')
                    break
                else:
                    self.Cells.addCell(c,PosX,PosY)
                    pass

        
    

    
    
    
        