from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog


def FileChooser():
    RuteFIle = ''
    Tk().withdraw()
    try:
        filename = filedialog.askopenfilename(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos XML', "*.{}".format('XML')),
                         ('Todos los archivos', '*.*'))
        )
        print(filename)
        with open(filename) as infile:
                RuteFIle = infile.read().strip()
                RuteFIle = RuteFIle.lower()
        print(RuteFIle)

    except:
        print('No se selecciono correctamente el archivo')
        return None

if __name__ == '__main__':

    FileChooser()
    