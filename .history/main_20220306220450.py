from os import startfile, system
from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog

from CellNode import Cell
from FloorList import FloorList
from FloorNode import Floor
from PatternNode import Pattern
from List_Cell import Cell_List



FloorList1 = FloorList()
Instructions = ''
SlideCount = 0
FlipCount = 0
MovCount = 0



def FileChooser():
    RuteFIle = ''
    Tk().withdraw()
    try:
        filename = filedialog.askopenfile(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos xml', "*.{}".format('xml')),
                         ('Todos los archivos', '*.*'))
        )
        return filename
    except:
        print('No se selecciono correctamente el archivo')
        return None


def ElementTree(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            name = element.attrib['nombre']
            row = ''
            column = ''
            flip = ''
            slide = ''
            for subelement in element:
                tag = str(subelement.tag).lower()
                if tag == 'r':
                    row = int(subelement.text)
                elif tag == 'c':
                    column = int(subelement.text)
                elif tag == 'f':
                    flip = int(subelement.text)
                elif tag == 's':
                    slide = int(subelement.text)
                elif tag == 'patrones':
                    patrones = subelement
                else:
                    print('Atributo no registrable', subelement.tag)
            if row >= 1 and column >= 1 and flip >= 0 and slide >= 0:
                FloorList1.AddFloor(name, row, column, flip, slide, patrones)
                print('piso "{}" cargado correctamente'.format(element.attrib['nombre']))
            else:
                print('!!!ERROR!!! Datos del piso "{}" incorrectos'.format(element.attrib['nombre']))
    except:
        print('No se cargaron los datos correctamente del piso "{}"'.format(element.attrib['nombre']))


def InserttPattToList(Floor : Floor, Patt : Pattern):
    tmpList = Cell_List()
    PosX = 0
    PosY = 1  
    for c in Patt.getPatt():
        if PosX < Floor.getColumn():
            PosX += 1
            tmpList.AddCell(PosX, PosY, c)
        else:
            PosY += 1
            PosX = 1
            if PosY > Floor.getRow():
                print('la letra',"'",c,"'",'ya no cabe dentro del patron')
                break
            else:
                tmpList.AddCell(PosX, PosY, c)
    return tmpList


def RefreshPatt(L1:Cell_List, L2:Cell_List):
    tmp1 = L1.First
    tmp2 = L2.First
    
    while tmp1 is not None:
        if tmp1.getColor() == tmp2.getColor():
            tmp1.BlockCell()
        tmp1 = tmp1.getNext()
        tmp2 = tmp2.getNext()

def SlidePatt(L1: Cell_List, L2: Cell_List, Floor: Floor):
    tmp1 = L1.First
    tmp2 = L2.First
    tmp1Next: Cell = tmp1.getNext()

    while tmp1Next is not None:
        if tmp1.getColor() != tmp2.getColor() and tmp1.getColor() != tmp1Next.getColor() :
            if tmp1.getBlock() == False and tmp1.getPosY() == tmp1Next.getPosY() and tmp1Next.getBlock() == False:
                global Instructions
                global MovCount
                global SlideCount
                SlideCount += 1
                MovCount += 1
                Instructions += '{}. Se Deslizo -->({}) de {},{} para {},{} -->({})  ||Costo: {}\n'.format(
                    MovCount, tmp1.getColor(), tmp1.getPosX(), tmp1.getPosY(), tmp1Next.getPosX(), tmp1Next.getPosY(), tmp1Next.getColor(), Floor.getSlideCost())

                tmp = tmp1.getColor()
                tmp1.setColor(tmp1Next.getColor())
                tmp1Next.setColor(tmp)
                tmp1.BlockCell()
                RefreshPatt(L1, L2)
        tmp1 = tmp1.getNext()
        tmp2 = tmp2.getNext()
        tmp1Next: Cell = tmp1.getNext()
    
def SlideDown(L1: Cell_List, L2: Cell_List, Floor: Floor):
    tmp1 = L1.First
    tmp2 = L2.First

    while tmp1 is not None:
        if tmp1.getBlock() == False:
            tmp1Down: Cell = tmp1.getNext()
            while tmp1Down is not None:
                if tmp1Down.getPosX() == tmp1.getPosX() and tmp1Down.getPosY() == tmp1.getPosY()+1:
                    if tmp1.getBlock() == False and tmp1.getColor() != tmp1Down.getColor() and tmp1Down.getBlock() == False:
                        global Instructions
                        global MovCount
                        global SlideCount
                        SlideCount += 1
                        MovCount += 1
                        Instructions += '{}. Se Deslizo -->({}) de {},{} para {},{} -->({})  ||Costo: {}\n'.format(
                            MovCount, tmp1.getColor(), tmp1.getPosX(), tmp1.getPosY(), tmp1Down.getPosX(), tmp1Down.getPosY(), tmp1Down.getColor(), Floor.getSlideCost())

                        tmp = tmp1.getColor()
                        tmp1.setColor(tmp1Down.getColor())
                        tmp1Down.setColor(tmp)
                        tmp1.BlockCell()
                        RefreshPatt(L1, L2)
                        print('----------------')
                tmp1Down = tmp1Down.getNext()
        tmp1 = tmp1.getNext()
        tmp2 = tmp2.getNext()

def InvertCell(L1: Cell_List, L2: Cell_List, Floor: Floor):
    tmp1 = L1.First
    tmp2 = L2.First
    while tmp1 is not None:
        if tmp1.getBlock() == False and tmp1.getColor() != tmp2.getColor():
            global Instructions
            global MovCount
            global FlipCount
            FlipCount += 1
            MovCount += 1
            Instructions += '{}. Se cambio de cara ({}) ({},{}) para obtener {}  ||Costo: {}\n'.format(
                MovCount, tmp1.getColor(), tmp1.getPosX(), tmp1.getPosY(), tmp2.getColor(), Floor.getFlipCost())
 
            tmp1.setColor(tmp2.getColor())
            tmp1.BlockCell
        tmp1 = tmp1.getNext()
        tmp2 = tmp2.getNext()


                    
    
            

def PrintGraphv(L1: Cell_List, Floor: Floor):
    GraphCode = ''' 
digraph Grafica{
    node[shape = box fillcolor = "FFEDBB" style = filled]
    label = "Nathan Valdez - 202001568"
    
    subgraph cluster_p{'''

    GraphCode += 'label = "{}"'.format(Floor.getName())
    GraphCode += '''bgcolor = "#E2A914"
        edge[dir = "none" style= invisible]\n'''

    tmp = L1.First
    RankCode = ''
    while tmp is not None:
        if tmp.getColor() == 'W':
            color = 'white'
        elif tmp.getColor() == 'B':
            color = 'black'
        GraphCode += 'Node{}_{}[label= " ", group={}, fillcolor= {}];\n'.format(
            tmp.getPosX(), tmp.getPosY(), tmp.getPosX(), color)
        
        if tmp.getNext() is not None and tmp.getPosX() < Floor.getColumn():
            # Node1_1 -> Node2_1
            GraphCode += 'Node{}_{} -> Node{}_{};\n'.format(
                tmp.getPosX(), tmp.getPosY(), tmp.getNext().getPosX(), tmp.getNext().getPosY())

            RankCode += '{rank=same; '
            RankCode += 'Node{}_{}; Node{}_{};'.format(
                tmp.getPosX(), tmp.getPosY(), tmp.getNext().getPosX(), tmp.getNext().getPosY())

            RankCode += '};\n'
            

        tmpDown: Cell = tmp.getNext()
        while tmpDown is not None:
            # Node1_1 -> Node1_2;
            if tmpDown.getPosX() == tmp.getPosX() and tmpDown.getPosY() == tmp.getPosY()+1:
                GraphCode+= 'Node{}_{} -> Node{}_{};\n'.format(
                    tmp.getPosX(), tmp.getPosY(), tmpDown.getPosX(), tmpDown.getPosY())
            tmpDown = tmpDown.getNext() 

        tmp = tmp.getNext()
    GraphCode += RankCode
    GraphCode += '''
    }
}    
'''
    NewFile= open('./TempFiles/{}.dot'.format(Floor.getName()),'w')
    NewFile.write(GraphCode)
    NewFile.close()

    system('dot -Tpng ./TempFiles/{}.dot -o {}.png'.format(Floor.getName(),Floor.getName()))
    startfile('{}.png'.format(Floor.getName()))
        
        
        
def TxtInstructions(str, Floor: Floor):
    TotalCost = SlideCount*Floor.getSlideCost()
    TotalCost += FlipCount*Floor.getFlipCost()
    
    str += '\n---->Costo Total: {}'.format(TotalCost)
    NewFile = open('Instrucciones.txt','w')
    NewFile.write(str)
    NewFile.close()

    startfile('Instrucciones.txt')
    

        
        
if __name__ == '__main__':
    Patt2: Pattern = None
    while True:
        Menu = input ('''
==============================
||1. Cargar Archivo XML     ||
||2. Mostrar Pisos Cargados ||
||9. Salir                  ||
==============================
Elige una opción:  ------->  ''')

        if Menu == '1':
            FloorList1 = FloorList()
            Cell_List1 = Cell_List()
            FilePath = FileChooser()
            ElementTree(FilePath)
            # ElementTree('Docs\esto.xml')
            # print('Elementos Cargados Exitosamente')

        elif Menu == '9':
            break 
            
        elif Menu == '2':
            FloorList1.ShowFloors()
            while True:
                MenuPisos = input('''
===================================================
||-> Ingresa el nombre del piso para seleccionar ||
||9. Regresar al Menu Principal                  ||
===================================================
Elige una opción:  ------->  ''')
                MenuPisos =  MenuPisos.lower()
                
                if MenuPisos == '9':
                    break
                else:
                    ChoosenFloor = FloorList1.FindFloor(MenuPisos)
                    if ChoosenFloor is not None:
                        
                        while True:
                            MenuPatt = input('''
==========================================================
||1. Mostrar Graficamente el Piso                       ||
||-> Para cambiar el patron por favor ingrese el codigo ||
||   del patron que desea cambiar                       ||
||9. Atras                                              ||
==========================================================
Elige una opción:  ------->  ''')
                            MenuPatt = MenuPatt.lower()
                            if MenuPatt == '9':
                                break
                            elif MenuPatt == '1':
                                Cell_List1 = InserttPattToList(ChoosenFloor, ChoosenFloor.getPatrones().first)
                                PrintGraphv(Cell_List1, ChoosenFloor)
                                pass
                            else:
                                Patt1 = ChoosenFloor.Patrones.FindPatt(MenuPatt)
                                if Patt1 is None:
                                    pass
                                else:

                                    while True:
                                        if Patt1 is not None:
                                            Cell_List1 = InserttPattToList(ChoosenFloor, Patt1)

                                            MenuPatt2 = input('''
=======================================================
||1. Mostrar Graficamente el Piso                    ||
||->.Para cambiar de patron seleccione               ||
||   otro codigo de patron con el cual intercambiar  ||
||3. Mostrar Instrucciones                           ||
||9. Atras                                           ||
=======================================================
Elige una opción:  ------->  ''')

                                            MenuPatt2 = MenuPatt2.lower()
                                            

                                            if MenuPatt2 == '9':
                                                break
                                            elif MenuPatt2 == '1':
                                                PrintGraphv(Cell_List1, ChoosenFloor)

                                            elif MenuPatt2 == '3':
                                                while True:
                                                    if Patt2 is not None:

                                                        TotalCost = SlideCount*ChoosenFloor.getSlideCost()
                                                        TotalCost += FlipCount*ChoosenFloor.getFlipCost()
                                        
                                                        Instructions += '\n---->Costo Total: {}'.format(TotalCost)



                                                        MenuInstructions = input('''
==============================
||1. Mostrar en Consola       ||
||2. Mostrar Instrucciones en ||
||   un archivo txt           ||
||9. Salir                    ||
==============================                   
Elige una opción:  ------->  ''')
                                                
                                                        if MenuInstructions == '1':
                                                            print(Instructions)
                                                            break
                                                        elif MenuInstructions == '2':
                                                            TxtInstructions(Instructions, ChoosenFloor)
                                                            break
                                                        elif MenuInstructions == '9':
                                                            break
                                                        else:
                                                            print('Ingrese una opcion valida')
                                                    else:
                                                        print('No se ha intercambiado ningun patron')
                                                        break


                                            else:
                                                Cell_List2 = Cell_List()
                                                PosX = 0
                                                PosY = 1
                                                SlideCount = 0
                                                FlipCount = 0 

                                                Instructions = '''Pasos que realizo el algoritmo para llegar al patron solicitado
Evuluado el costo minimo calculado:

'''

                                                Patt2 = ChoosenFloor.Patrones.FindPatt(MenuPatt2)
                                                if Patt2 is not None:
                                                    Cell_List2 = InserttPattToList(ChoosenFloor, Patt2)

                                                    RefreshPatt(Cell_List1, Cell_List2)

                                                    if ChoosenFloor.getSlideCost() <= ChoosenFloor.getFlipCost():
                                                        SlidePatt(Cell_List1, Cell_List2, ChoosenFloor)
                                                        SlideDown(Cell_List1, Cell_List2, ChoosenFloor)
                                                        InvertCell(Cell_List1, Cell_List2, ChoosenFloor)
                                                    elif ChoosenFloor.getSlideCost() > ChoosenFloor.getFlipCost():
                                                        InvertCell(Cell_List1, Cell_List2, ChoosenFloor)
                                                        SlidePatt(Cell_List1, Cell_List2, ChoosenFloor)
                                                        SlideDown(Cell_List1, Cell_List2, ChoosenFloor)

                                                    tmp = Cell_List1.First
                                                    tmpString = ''
                                                    while tmp is not None:
                                                        tmpString += tmp.getColor()
                                                        tmp = tmp.getNext()
                                                    
                                                    Patt1.setPatt(tmpString)
                                                    print('Intercambio de patrones exitoso')
                                                else:
                                                    pass
                                            
                                            
                                            
                                            
                                                

                                            




                    



    