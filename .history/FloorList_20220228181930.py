from FloorNode import Floor

class FloorList():
    def __init__(self):
        self.first : Floor = None
        self.last = None
        self.Size = 0

    def AddFloor(self, name, row, column, flip, slide, patrones):
        NewFloor = Floor(name, row, column, flip, slide)
        self.Size += 1
        if self.first is None:
            self.first = NewFloor
            self.last = NewFloor
        else:
            self.last.setNext(NewFloor)
            self.last = NewFloor

    def ShowFloors(self):
        tmp = self.first
        for x in range(self.Size):
            print('Nombre:', tmp.getName(), 'R-',tmp.getRow(), 'C-',tmp.getColumn(), 'F-',tmp.getFlipCost(), 'S-',tmp.getSlideCost(),'\n',tmp.Patrones)
            print('-------------')
            tmp = tmp.getNext()