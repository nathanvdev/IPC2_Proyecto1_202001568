

from traceback import print_tb


cadena = 'WBWBWdfghWWB'
Filas = 2
Columnas = 4

posx = 0
posy = 1

text = ''

for c in cadena:
    if posx < Columnas:
        posx +=1
        # print(c, "(",posx,",",posy,")")
    else:
        posy += 1
        posx = 1
        if posy > Filas:
            print('la letra',"'",c,"'",'ya no cabe dentro del patron')
            break
        else:
            # print(c, "(",posx,",",posy,")")
            pass

    text += c
    text += '('
    text += str(posx)
    text += ','
    text += str(posy)
    text += ')'
    print(text,end='\n')







# for y in range(Filas):
#     posy += 1
#     for x in range(Columnas):
#         posx += 1
#         print('(',posx,',',posy,')', end="")
#     posx = 0
#     print('')
    
