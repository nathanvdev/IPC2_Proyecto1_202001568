from importlib.abc import PathEntryFinder
from traceback import print_tb
from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog

from FloorList import FloorList
from FloorNode import Floor
from PatternNode import Pattern
from List_Cell import Cell_List



FloorList1 = FloorList()

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
            FloorList1.AddFloor(name, row, column, flip, slide, patrones)
    except:
        print('No se cargaron los datos correctamente')


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
        print(tmp1.getColor(), tmp2.getColor())
        if tmp1.getColor() == tmp2.getColor():
            tmp1.BlockCell()
            print('manzana')
        tmp1 = tmp1.getNext()
        tmp2 = tmp2.getNext()

def SlidePatt(L1:Cell_List, L2:Cell_List):
    tmp1 = L1.First
    tmp2 = L2.First
    print(tmp1.getColor(),tmp2.getColor())
    if str(tmp1.getColor()) != str(tmp2.getColor()) and tmp1.getBlock == False:
        print('desgracia', tmp1.getBlock)
            

        
        
if __name__ == '__main__':

    while True:
        Menu = input ('''
==============================
||1. Cargar Archivo XML     ||
||2. Mostrar Pisos Cargados ||
||3. Analizar               ||
||4. Reportes               ||
||5. Salir                  ||
==============================
Elige una opción:  ------->  ''')

        if Menu == '1':
            FloorList1 = FloorList()
            # FilePath = FileChooser()
            # ElementTree(FilePath)
            ElementTree('Docs\esto.xml')
            print('Elementos Cargados Exitosamente')
        elif Menu == '2':
            FloorList1.ShowFloors()
            while True:
                MenuPisos = input('''
===================================================
||1. Ingresa el nombre del piso para seleccionar ||
||2. Regresar al Menu Principal                  ||
===================================================
Elige una opción:  ------->  ''')
                
                if MenuPisos == '2':
                    break
                else:
                    ChosenFloor = FloorList1.FindFloor(MenuPisos)
                    if ChosenFloor is not None:
                        while True:
                            MenuPatt = input('''
=======================================================
||1. Ingresa el codigo del patron para seleccionar   ||
||2. Atras                                           ||
=======================================================
Elige una opción:  ------->  ''')
                            if MenuPatt == '2':
                                break
                            else:
                                Patt1 = ChosenFloor.Patrones.FindPatt(MenuPatt)
                                
                                while True:
                                    if Patt1 is not None:
                                        MenuPatt2 = input('''
=======================================================
||1. Ingresa el codigo del patron con el que         ||
||   Desea Intercambiar                              ||
||2. Atras                                           ||
=======================================================
Elige una opción:  ------->  ''')
                                        if MenuPatt2 == '2':
                                            break
                                        else:
                                            Cell_List1 = Cell_List()
                                            Cell_List2 = Cell_List()
                                            PosX = 0
                                            PosY = 1    

                                            Patt2 = ChosenFloor.Patrones.FindPatt(MenuPatt2)

                                            Cell_List1 = InserttPattToList(ChosenFloor, Patt1)
                                            Cell_List2 = InserttPattToList(ChosenFloor, Patt2)

                                            SlidePatt(Cell_List1, Cell_List2)

        elif Menu == '5':
            break                                  
                                            
                                            
                                            
                                                

                                            




                    



    