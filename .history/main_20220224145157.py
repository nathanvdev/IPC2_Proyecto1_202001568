from msilib.schema import File
from xml.etree import ElementTree as ET
from tkinter import Tk, filedialog


def FileChooser():
    RuteFIle = ''
    Tk().withdraw()
    try:
        file = filedialog.askopenfile(
            initialdir = './',
            title = 'Selecciona un archivo',
            filetypes = (('Archivos XML', "*.{}".format('XML')),
                         ('Todos los archivos', '*.*'))
        )
        return file

    except:
        print('No se selecciono correctamente el archivo')
        return None

if __name__ == '__main__':

    FilePath = FileChooser()
    print(FilePath)
    