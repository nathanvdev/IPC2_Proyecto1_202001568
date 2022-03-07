

# from traceback import print_tb


# cadena = 'WBWBWdfghWWB'
# Filas = 2
# Columnas = 4

# posx = 0
# posy = 1

# text = ''

# for c in cadena:
#     if posx < Columnas:
#         posx +=1
#         # print(c, "(",posx,",",posy,")")
#     else:
#         posy += 1
#         posx = 1
#         if posy > Filas:
#             print('la letra',"'",c,"'",'ya no cabe dentro del patron')
#             break
#         else:
#             # print(c, "(",posx,",",posy,")")
#             pass

# for c in Patt1.getPatt():
#     if PosX < ChosenFloor.getColumn():
#         PosX += 1
#         Cell_List1.AddCell(PosX, PosY, c)
#     else:
#         PosY += 1
#         PosX = 1
#         if PosY > ChosenFloor.getRow():
#             print('la letra',"'",c,"'",'ya no cabe dentro del patron')
#             break
#         else:
#             Cell_List1.AddCell(PosX, PosY, c)
# Cell_List1.ShowCells()




# for y in range(Filas):
#     posy += 1
#     for x in range(Columnas):
#         posx += 1
#         print('(',posx,',',posy,')', end="")
#     posx = 0
#     print('')
    

from os import startfile, system


def TxtInstructions(string):
    NewFile = open('Instrucciones.txt')
    NewFile.write('esto es una prueba')
    NewFile.close()

    system('cd ./Instrucciones.txt')
    startfile('Instrucciones.tx')

TxtInstructions()