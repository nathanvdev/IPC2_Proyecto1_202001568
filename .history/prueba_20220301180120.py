from matplotlib.colorbar import Colorbar



cadena = 'WBWBWWWB'
Filas = 2
Columnas = 4

posx = 0
posy = 0



for y in range(Filas):
    posy += 1
    for x in range(Columnas):
        posx += 1
        print('(',posx,',',posy,')')
    posx = 0
    print('')
    
