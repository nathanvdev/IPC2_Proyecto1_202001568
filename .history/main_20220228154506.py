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
        
        print('nombre-', element.attrib['nombre'])
        for subelement in element:
            if subelement.tag != 'patrones':
                x = subelement.text.replace('\n','')
                x = x.replace(' ','')
                print(subelement.tag,'-',x)
            else:
                pass
        patrones = element[4]
        for p in patrones:
            y = p.text.replace('\n','')
            y = y.replace(' ','')
            print('codigo-',p.attrib['codigo'])
            print('patron-',y)
        print('--------')

if __name__ == '__main__':
    # FilePath = FileChooser()
    # ElementTree(Filepath)
    ElementTree('Docs\esto.xml')


    