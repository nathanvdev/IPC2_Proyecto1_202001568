from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog

from FloorList import FloorList



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
        
        
if __name__ == '__main__':

    while True:
        Menu = input ('''=============================
||1. Cargar Data           ||
||2. Cargar Instrucciones  ||
||3. Analizar              ||
||4. Reportes              ||
||5. Salir                 ||
=============================
Elige una opción:  ------->  ''')

    if Menu 




    # FilePath = FileChooser()
    # ElementTree(Filepath)
    ElementTree('Docs\esto.xml')
    FloorList1.ShowFloors()


    