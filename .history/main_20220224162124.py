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
        print(filename)
        with open(filename) as infile:
                FileText = infile.read().strip()
                FileText = FileText.lower()
        return RuteFIle

    except:
        print('No se selecciono correctamente el archivo')
        return None

if __name__ == '__main__':

    FilePath = FileChooser()
    print(FilePath)
    