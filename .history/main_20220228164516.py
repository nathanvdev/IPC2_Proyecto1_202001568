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
                for x in subelement:
                    y = str(x.tag).lower()
                    if y == 'codigo':
                        codigo = x.attrib['codigo']
                        patron = x.text
                    elif y == 'codigo':
                        codigo = x.attrib['código']
                        patron = x.text

            else:
                print('Atributo no registrable', subelement.tag)

            print(row, column, flip, slide, codigo, patron)
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


    