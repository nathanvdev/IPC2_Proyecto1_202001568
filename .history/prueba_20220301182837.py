from matplotlib.colorbar import Colorbar



cadena = 'WBWBWWesfgWB'
Filas = 2
Columnas = 4

posx = 0
posy = 1


for c in cadena:
    
    if posx < Columnas:
        posx +=1
        print(c, "(",posx,",",posy,")")
    else:
        posy += 1
        posx = 1
        if posy > Filas:
            print('somtax error')
            break
        else:
            print(c, "(",posx,",",posy,")")
    


# for y in range(Filas):
#     posy += 1
#     for x in range(Columnas):
#         posx += 1
#         print('(',posx,',',posy,')', end="")
#     posx = 0
#     print('')
    
