
from asyncio.proactor_events import _ProactorBasePipeTransport
from os import startfile, system
import sys
from tempfile import TemporaryDirectory
from traceback import print_tb
from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog

from jinja2 import ChoiceLoader
from CellNode import Cell

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
        tmp1 = tmp1.getNext()
        tmp2 = tmp2.getNext()

def SlidePatt(L1: Cell_List, L2: Cell_List):
    tmp1 = L1.First
    tmp2 = L2.First
    tmp1Next: Cell = tmp1.getNext()

    while tmp1Next is not None:
        if tmp1.getColor() != tmp2.getColor() and tmp1.getColor() != tmp1Next.getColor() :
            if tmp1.getBlock() == False and tmp1.getPosY() == tmp1Next.getPosY():
                tmp = tmp1.getColor()
                tmp1.setColor(tmp1Next.getColor())
                tmp1Next.setColor(tmp)
                tmp1.BlockCell()
                RefreshPatt(L1, L2)
                print('----------------')
        tmp1 = tmp1.getNext()
        tmp2 = tmp2.getNext()
        tmp1Next: Cell = tmp1.getNext()
    
def SlideDown(L1: Cell_List, L2: Cell_List, Floor: Floor):
    tmp1 = L1.First
    tmp2 = L2.First
    tmp1Down = tmp1
    while tmp1Down is not None:
        if tmp1Down.getBlock() == False:


            pass
            

def PrintGraphv(L1: Cell_List, Floor: Floor):
    GraphCode = ''' 
digraph Grafica{
    node[shape = box fillcolor = "FFEDBB" style = filled]
    label = "Nathan Valdez - 202001568"
    
    subgraph cluster_p{'''

    GraphCode += 'label = "{}"'.format(Floor.getName())
    GraphCode += '''bgcolor = "#E2A914"
        edge[dir = "both" ]'''

    tmp = L1.First

    while tmp is not None:
        if tmp.getColor() == 'W':
            color = 'white'
        elif tmp.getColor() == 'B':
            color = 'black'
        GraphCode += 'Node{}_{}[label= "{},{}", group={}, fillcolor= {}];'.format(tmp.getPosX(),tmp.getPosY(),
                                                                                tmp.getPosX(),tmp.getPosY(),
                                                                                tmp.getPosX(),
                                                                                color)
        if tmp.getNext() is not None and tmp.getPosX() < Floor.getColumn():
            # Node1_1 -> Node2_1
            GraphCode += 'Node{}_{} -> Node{}_{};'.format(tmp.getPosX(),tmp.getPosY(),
                                                            tmp.getNext().getPosX(),tmp.getNext().getPosY())
            RankCode = ''
            

        tmpDown: Cell = tmp.getNext()
        while tmpDown is not None:
            # Node1_1 -> Node1_2;
            if tmpDown.getPosX() == tmp.getPosX() and tmpDown.getPosY() == tmp.getPosY()+1:
                GraphCode+= 'Node{}_{} -> Node{}_{};'.format(tmp.getPosX(), tmp.getPosY(),
                                                            tmpDown.getPosX(), tmpDown.getPosY())
            tmpDown = tmpDown.getNext()




        tmp = tmp.getNext()
    
    GraphCode += '''
    }
}    
'''
    NewFile= open('{}.dot'.format(Floor.getName()),'w')
    NewFile.write(GraphCode)
    NewFile.close()

    system('dot -Tpng {}.dot -o {}.png'.format(Floor.getName(),Floor.getName()))
    system('cd ./{},png'.format(Floor.getName()))
    startfile('{}.png'.format(Floor.getName()))
        
        
        

        
            

        
        
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
||1. Mostrar Graficamente el Piso                    ||
||2. Ingresa el codigo del patron para seleccionar   ||
||3. Atras                                           ||
=======================================================
Elige una opción:  ------->  ''')
                            if MenuPatt == '3':
                                break
                            elif MenuPatt == '1':
                                Cell_List1 = Cell_List()
                                Cell_List1 = InserttPattToList(ChosenFloor, ChosenFloor.getPatrones().first)

                                PrintGraphv(Cell_List1, ChosenFloor)


                                pass
                            else:
                                Patt1 = ChosenFloor.Patrones.FindPatt(MenuPatt)
                                PrintGraphv(Patt1)
                                
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
                                            
                                            Cell_List2 = Cell_List()
                                            PosX = 0
                                            PosY = 1    

                                            Patt2 = ChosenFloor.Patrones.FindPatt(MenuPatt2)

                                            Cell_List1 = InserttPattToList(ChosenFloor, Patt1)
                                            Cell_List2 = InserttPattToList(ChosenFloor, Patt2)

                                            RefreshPatt(Cell_List1, Cell_List2)
                                            print('***********************')
                                            SlidePatt(Cell_List1, Cell_List2)

                                            

        elif Menu == '5':
            break                                  
                                            
                                            
                                            
                                                

                                            




                    



    