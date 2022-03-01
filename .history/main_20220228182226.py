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
                row = subelement.text
            elif tag == 'c':
                column = subelement.text
            elif tag == 'f':
                flip = subelement.text
            elif tag == 's':
                slide = subelement.text
            elif tag == 'patrones':
                patrones = subelement
            else:
                print('Atributo no registrable', subelement.tag)

        for p in patrones:
            print(p.attrib['codigo'])
        

        FloorList1.AddFloor(name, row, column, flip, slide)
        
        



        # patrones = element[4]
        # for p in patrones:
        #     y = p.text.replace('\n','')
        #     y = y.replace(' ','')
        #     print('codigo-',p.attrib['codigo'])
        #     print('patron-',y)
        # print('--------')

if __name__ == '__main__':
    # FilePath = FileChooser()
    # ElementTree(Filepath)
    ElementTree('Docs\esto.xml')
    # FloorList1.ShowFloors()


    