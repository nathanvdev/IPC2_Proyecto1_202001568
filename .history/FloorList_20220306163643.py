from FloorNode import Floor



class FloorList():
    def __init__(self):
        self.first : Floor = None
        self.last = None
        self.Size = 0

    def AddFloor(self, name, row, column, flip, slide, patrones):
        NewFloor = Floor(name, row, column, flip, slide)
        patrones = str(patrones)
        patrones.replace()
        
        for p in patrones:
                code = p.attrib['codigo']
                patt = str(p.text)
                patt= patt.upper()
                NewFloor.setPattern(code, patt)
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
            print('Nombre:', tmp.getName(), 'R-',tmp.getRow(), 'C-',tmp.getColumn(), 'F-',tmp.getFlipCost(), 'S-',tmp.getSlideCost())
            print('con los patrones:')
            tmp.Patrones.showPatterns()
            print('-------------')
            tmp = tmp.getNext()

    def FindFloor(self, name):
        tmp = self.first
        for d in range(self.Size):
            if tmp.getName() == name:
                print('piso', tmp.getName(), 'seleccionado')
                print('con los siguientes patrones:')
                tmp.Patrones.showPatterns()
                return tmp
            else:
                tmp = tmp.getNext()
        print('No se encontro el Piso ingresado')
        return None
        

