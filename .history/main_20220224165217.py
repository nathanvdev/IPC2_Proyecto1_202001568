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
    print(root)
    
if __name__ == '__main__':

    # FilePath = FileChooser()
    ElementTree('pisos.xml')
    