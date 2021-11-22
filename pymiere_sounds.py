import pymiere
import random
import sys

cursorPos = pymiere.objects.app.project.sequences[0].getPlayerPosition()
cursorInTicks = cursorPos.ticks

# argumento del cmd



# nombre de la carpeta donde se encuentran los sonidos

findMe = sys.argv[1]

# buscar el numero index de una determinada carpeta bin
def findBinIndex (rootPath, nameToFind):
        i = 0
        # hacer un loop a traves de los diferentes items del root path del proy
        while i < rootPath.children.numItems:
            currentChild = rootPath.children[i]
            i += 1
            # print(currentChild.name)
            # si el tipo de objeto es igual a 2 (BIN) imprimir el index del objeto
            if currentChild.name == nameToFind:
                # print('se encontro la carpeta'+ nameToFind)
                # contar cuantos items hay en la carpeta encontrada y pasar a variable items
                items = int(currentChild.children.numItems)

                # print('la carpeta tiene '+ str(items) + ' elementos')

                # generar un numero random, con el rango establecido de items
                r = random.randint(0,(items-1))

                # numeros super random, que no se repitan:
                f = open('parametros.txt', 'r+')
                read = f.read()
                while str(r) == read:
                    # print('los numeros coinciden, generar otro num')
                    r = random.randint(0, (items - 1))
                    #print('Se ha seleccionado el clip: '+ str(currentChild.children[r].name))
                    # importar el clip a la secuencia, en el track de audio numero 2


                pymiere.objects.app.project.sequences[0].audioTracks[1].overwriteClip(currentChild.children[r], cursorPos)
                print( currentChild.children[r].name + ' se importó a la timeline')

                f = open('parametros.txt', 'w')
                f.write(str(r))
                f.close()
                break

        else:
            print('No se encuentra la carpeta...')


# ejecutar funcio
findBinIndex(pymiere.objects.app.project.rootItem, findMe)
