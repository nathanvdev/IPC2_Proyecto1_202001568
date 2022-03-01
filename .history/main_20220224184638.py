from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog


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
        print(element.attrib['nombre'])
        for subelement in element:
            x = subelement.text.replace('\n','')
            x = x.replace(' ','')
            print(x)
        patrones = element[4]
        for p in patrones:
            y = p.text.replace('\n','')
            y = y.replace(' ','')
            print(p.attrib['codigo'], '-', y)

if __name__ == '__main__':
    # FilePath = FileChooser()
    ElementTree('Docs\esto.xml')
    