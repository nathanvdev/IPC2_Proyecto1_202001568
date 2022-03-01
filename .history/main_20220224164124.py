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
        print(element)

if __name__ == '__main__':

    # FilePath = FileChooser()
    ElementTree('F:/Bibliotecas/Documents/U/2022/Primer Semestre/Lab IPC2/IPC2_Proyecto1_202001568/Docs/pisos.xml')
    