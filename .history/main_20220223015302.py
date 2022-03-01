from msilib.schema import File
from tkinter import Tk, filedialog


def FileChooser():
    FileText = ''
    text = ''
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
                FileText = infile.read().strip()
                FileText = FileText.lower()
        print(FileText)

        return text
    except:
        print('No se selecciono correctamente el archivo')
        return None

if __name__ == '__main__':

    FileChooser()