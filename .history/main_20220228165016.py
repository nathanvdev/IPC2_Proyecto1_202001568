from traceback import print_tb
from xml.etree import ElementTree as ET
from tkinter import Tk, commondialog, filedialog


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
        print(name)
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
            print(p.tag, p.text)
        print(row, column, flip, slide)
        print('-----------')



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


    