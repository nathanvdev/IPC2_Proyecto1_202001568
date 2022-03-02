from matplotlib.colorbar import Colorbar



cadena = 'WBWBWWWB'
Filas = 2
Columnas = 4

posx = 0
posy = 0


for i in cadena:
    for y in Filas:
        posy += 1
        for x in Columnas:
            posx += 1
            print(posx, ',',posy)

    
