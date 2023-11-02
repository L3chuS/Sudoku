# Se crea un tablero de 9x9.
ind_tablero_comprobar = [["*" for c in range(9)] for f in range(9)]


def presentacion_juego():
    """Función que presenta el juego, lo explica y da lugar al comienzo o no."""

    print("""
            \"Bienvenidos al Sudoku\"

El juego se compone de 9 filas y 9 columnas.
En cada espacio, deberás añadir un número entre
el 1 y el 9. Cada fila y cada columna deberá
contener todos los números del 1 al 9 sin importar
el orden. A su vez, los subcuadros de 3x3 (3 filas
y 3 columnas) deberán tener también todos los
números. El juego finaliza cuando logras completar
cada fila, columna y subcuadro con los valores
entre el 1 y el 9. Puedes añadir y quitar cada
número las veces que haga falta excepto los números
iniciales.
Si deseas continuar escriba "C". En caso contrario
escriba "S".""")

    # Bucle que evalúa la elección del usuario para comenzar, finalizar o indicar una opción inválida.
    while(True):
        try:
            eleccion = input("\nOpción elegida: ")
            if eleccion == "C" or eleccion == "c":
                print("\n            Comencemos el juego!")
                break
            elif eleccion == "S" or eleccion == "s":
                print("\nTan rápido te vas? Bueno, nos vemos la proxima.")
                return None
            else:
                raise ValueError

        except ValueError:
            print("\nLa opción elegida no es correcta. Vuelva a intentarlo.")
        except KeyboardInterrupt:
            print("\n\nHasta luego")
            return None

    return ""
        

def dibujar_tablero(lista_tablero):
    """Función que dibuja un tablero en la terminal el cual será usado para ir representando los
       cambios introducidos por el jugador a partir de una lista tomada como argumento."""

    # Contador para representar las filas del tablero.
    contador = 0
    print("""
  C   C   C   C   C   C   C   C   C
  1   2   3   4   5   6   7   8   9""",)

    for filas in range(3):
        print("#-----------" * 3 + "#")
        for l in range(2):
            for columna in range(9):
                print(f"| {lista_tablero[contador][columna]} ", end="")
            print(f"| F {contador + 1}")
            contador += 1
            print("----" * 9 + "-")
        for columna in range(9):
            print(f"| {lista_tablero[contador][columna]} ", end="")
        print(f"| F {contador + 1}")
        contador += 1
    print("#-----------" * 3 + "#")

    return


def modificar_tablero(fila, columna, valor, tablero_modificar):
    """Función que modifica el tablero del juego. Toma 4 argumentos. Los primeros 3
       son los que se utilizan para modificar el último en el índice correspondiente."""
    tablero_modificar[fila-1][columna-1] = valor


def ordenar_tablero(tablero_ordenar):
    """Función que reordena las columnas y subgrupos del juego (cada grupo de 3x3) para poder
       evaluar si son válidos o no. Es decir, devuelve cada columna o cada subgrupo para verificar
       si cumple con las condiciones de victoria o no."""

    columnas_ordenadas = []
    subgrupos_ordenados = [[] for i in range (9)]

    # Se intera por cada fila del tablero.
    for filas in range(9):
        # Se crea una lista vacía para añadirle los valores de cada columna.
        comprobador_columnas = []
        # Se van agregando todos los valores de las columnas del índice de la variable "filas".
        for columnas in range(9):
            comprobador_columnas.append(tablero_ordenar[columnas][filas])
        columnas_ordenadas.append(comprobador_columnas)

    # Se itera sobre el tablero para ir armando los subgrupos de 3x3.
    for elem in range(0,9,3):
        # Por cada iteración se arman los grupos del 1 al 3, luego del 4 a 6 y finalmente del 7 al 9.
        for i in range(3):
            subgrupos_ordenados[elem] += tablero_ordenar[elem+i][:3]
            subgrupos_ordenados[elem+1] += tablero_ordenar[elem+i][3:6]
            subgrupos_ordenados[elem+2] += tablero_ordenar[elem+i][6:]

    return columnas_ordenadas, subgrupos_ordenados


def comprobador_victoria(tablero_comprobar):
    """Función que comprueba la victoria a partir de un tablero recibido como argumento.
       Devuelve True o False."""

    # Variable que se usa para comprobar la victoria. 
    comparador = [1,2,3,4,5,6,7,8,9]

    for fila in tablero_comprobar:          
        # if len(tablero_comprobar) != 9:   ######## REVISAR SI DA ERRORES. NO SE POR QUE ESTABA ESTA LINEA.########
        #     return False                  ########################################################################

        # Comprueba que no haya espacios "vacíos" representados con un "*".
        for elem in fila:
            if elem == "*":
                return False      
        if sorted(fila) != comparador:
            return False
    else:
        return True

def random_tableros():
    """Función para generar tableros con valores aleatorios. Primero intenta agregar el valor 1 una vez por fila
       y sin que se repita en la misma columna. Si se consigue agregarlo 9 veces (límite máximo del juego por cada
       valor) pasa al número 2 y así sucesivamente hasta llegar al 9 o al máximo de iteraciones posibles. Finalmente
       lo retorna para que sea evaluado si es un tablero válido para jugar."""
    
    from random import shuffle

    valores = [1,2,3,4,5,6,7,8,9]
    tablero_comprobar = []
    repetido = False
    
    for indice in range(9):
        if indice == 0:
            shuffle(valores)
            tablero_comprobar.append(valores[:])
        else:
            
            shuffle(valores)
            while True:
                repetido = False
                for valor in range(9):
                    # print(valores[valor])
                    indice_fila = indice
                    while indice_fila != 0:
                        if valores[valor] == tablero_comprobar[indice_fila-1][valor]:
                            repetido = True
                            break
                        
                        else:
                            indice_fila -= 1

                    if repetido == True:
                        shuffle(valores)
                        break
                if repetido == False:
                    tablero_comprobar.append(valores[:])
                    # print(tablero_comprobar)
                    shuffle(valores)
                    break
        
    for linea in tablero_comprobar:
        print(linea)


print(random_tableros())

# def comprobador_tablero_random(ind_tablero_comprobar):

#     while comprobador_victoria(ind_tablero_comprobar) == False:

#         random_tableros()
            
#     return ind_tablero_comprobar


# x = [[5, 9, 3, 7, 6, 8, 2, 4, 1],[8, 7, 6, 1, 4, 2, 9, 5, 3],[1, 2, 4, 5, 9, 3, 7, 8, 6],[7, 6, 8, 9, 2, 5, 1, 3, 4],[4, 3, 2, 8, 1, 7, 6, 9, 5],[9, 1, 5, 6, 3, 4, 8, 7, 2],[6, 8, 1, 4, 5, 9, 3, 2, 7],[3, 4, 7, 2, 8, 1, 5, 6, 9],[2, 5, 9, 3, 7, 6, 4, 1, 8]]

# print(comprobador_tablero_random(x))

# def exportar_tableros():
#     import csv

#     numero_tableros_exportados = 0

#     while numero_tableros_exportados < 50:
#         with open("Tableros Exportados.csv", "a", newline="\n") as fichero:
#             writer = csv.writer(fichero, delimiter=",")
#             for linea in range(1):
#                 writer.writerow(comprobador_tablero_random(ind_tablero_comprobar))
#         numero_tableros_exportados += 1
#     return ""

# def leer_tableros_exportados():
#     import csv
#     from random import randrange

#     with open("Tableros Exportados.csv", "r", newline="") as fichero:
#         reader = csv.reader(fichero, delimiter=",")
#         ref = ["1","2","3","4","5","6","7","8","9"]
#         valor = []
#         contador = 0
#         tab_convertido = list(reader)[randrange(50)]

#         for f in tab_convertido:
#             valor.append([])
#             for e in f:
#                 if e in ref:
#                     e = int(e)
#                     valor[contador].append(e)
#             contador += 1        

#     return valor

# def generar_tableros_aleatorios(dificultad):

#     from random import randrange

#     tablero_reordenado = [[], [], [], [], [], [], [], [], [],]
#     tablero_random = [["*" for c in range(9)] for f in range(9)]

#     tablero_a_generar = leer_tableros_exportados()
#     valores_aleatorios = ordenar_tablero(tablero_a_generar)[1]

#     for i in range(9):
#         indices_aleatorio1, indices_aleatorio2, indices_aleatorio3 = randrange(0,9), randrange(0,9), randrange(0,9)
#         while True:
#             if indices_aleatorio1 == indices_aleatorio2:
#                 indices_aleatorio2 = randrange(0,9)
#             if indices_aleatorio3 == indices_aleatorio2 or indices_aleatorio3 == indices_aleatorio1:
#                 indices_aleatorio3 = randrange(0,9)
#             else:
#                 break
#         if dificultad == "F" or dificultad == "f":
#             tablero_random[i][indices_aleatorio1] = valores_aleatorios[i][indices_aleatorio1]
#             tablero_random[i][indices_aleatorio2] = valores_aleatorios[i][indices_aleatorio2]
#             tablero_random[i][indices_aleatorio3] = valores_aleatorios[i][indices_aleatorio3]
#         if dificultad == "M" or dificultad == "m":
#             tablero_random[i][indices_aleatorio1] = valores_aleatorios[i][indices_aleatorio1]
#             tablero_random[i][indices_aleatorio2] = valores_aleatorios[i][indices_aleatorio2]
#         if dificultad == "D" or dificultad == "d":
#             tablero_random[i][indices_aleatorio1] = valores_aleatorios[i][indices_aleatorio1]

#     for elem in range(0,9,3):
#         for i in range(3):
#             tablero_reordenado[elem] += tablero_random[elem+i][:3]
#             tablero_reordenado[elem+1] += tablero_random[elem+i][3:6]
#             tablero_reordenado[elem+2] += tablero_random[elem+i][6:]

#     return tablero_reordenado


# #####################################################
# #########       PRESENTACIÓN DEL JUEGO      #########
# #####################################################

# try:

#     while(True):

#         if presentacion_juego() == None:
#             break
#         else:
#             print("""\nVamos a lo primero. Qué nivel de dificultad quieres?
# Si quieres un juego fácil escribe "F". Si quieres que
# sea un nivel medio escribe "M". Si eres valiente
# escribe "D".\n""")
#             dificultad = input("Opción elegida: ")
#             opciones_correctas = ["F", "f", "M", "m", "D", "d"]

#             while dificultad not in opciones_correctas:
#                 print(f"\nLa opcion elegida \"{dificultad}\" no es válida. Debe escribir \"F\", \"M\" o \"D\".\n")
#                 dificultad = input("Opción elegida: ")
#             if dificultad in opciones_correctas[0:2]:
#                 valor = 3
#             elif dificultad in opciones_correctas[2:4]:
#                 valor = 2
#             else:
#                 valor = 1
        
#             print(f"""\nAlgunas aclaraciones antes de empezar. Teniendo en
# cuenta la dificultad que has elegido, se ha generado
# un tablero con {valor} valor/es cargado/s aleatoriamente
# por cada subgrupo. Tu objetivo es completar todos los
# campos. Para ello se te pedirá una fila, una columna y
# el valor a introducir de manera que vayas completando
# todo el tablero. No puedes modificar los números ya
# cargados previamente pero sí puedes deshacer todos los
# cambios realizados. También, puedes reemplazar un valor
# que hayas agregado por un "*" si deseas restablecerlo a
# cero. Cuando creas que has terminado tienes 3 intentos
# para comprobar tu victoria. 

#         Estás listo para comenzar?
                                    
# Escribe "C" para continuar o "S" para salir.\n""")

#             while(True):
#                 inicio = input("Opción elegida: ")
#                 if inicio == "S" or inicio == "s":
#                     print("\nTan rápido te vas? Bueno, nos vemos la proxima.")
#                     break
#                 elif inicio == "C" or inicio == "c":
#                     print("")
#                     print("#####" * 12)
#                     print("\nComencemos el juego!\n")                  
#                     break
#                 else:
#                     print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n") 

#             if inicio == "S" or inicio == "s":
#                 break

# #####################################################
# #########       AQUÍ COMIENZA EL JUEGO      #########
# #####################################################
            
#             else:
#                 # tablero_usuario = leer_tableros_exportados()
#                 tablero_usuario = generar_tableros_aleatorios(dificultad)
#                 dibujar_tablero(tablero_usuario)
#                 movimientos_restringidos = []
#                 contador = 0

#                 for ind_fila, fila in enumerate(tablero_usuario):
#                     for ind_col, elem in enumerate(fila):
#                         if elem == "*":
#                             pass
#                         else:
#                             movimientos_restringidos.append([])
#                             movimientos_restringidos[contador].append(ind_fila)
#                             movimientos_restringidos[contador].append(ind_col)
#                             contador +=1

#                 lista_filas = []
#                 lista_columnas = []
#                 lista_valores = ["*"]
#                 intentos_victoria = 3

#                 while(True):

#                     continuar = True
#                     valores_correctos = ["1","2","3","4","5","6","7","8","9"]
                    
                    
#                     print("\nElija una fila, una columna y el valor que desea modificar o presione \"Enter\" para las opciones:\n\
# - Deshacer Movimiento\n\
# - Comprobar Victoria\n\
# - Salir\n")          
          
#                     while True:
#                         fila = input("Fila: ")
#                         if fila in valores_correctos:
#                             fila = int(fila)
#                             lista_filas.append(fila)
#                             break

#                         while fila == "":
#                             movimiento = input("\nPara deshacer el último movimiento escribe \"0\".\
# \nSi quieres comprobar tu victoria escribe \"9\".\
# \nPara salir \"8\".\
# \nSi no escribe \"C\":  ")
#                             if movimiento == "0":
#                                 if len(lista_filas) > 0:
#                                     modificar_tablero(lista_filas[-1], lista_columnas[-1], lista_valores[-1], tablero_usuario)
#                                     lista_filas.pop()
#                                     lista_columnas.pop()
#                                     lista_valores.pop()
#                                     dibujar_tablero(tablero_usuario) 
#                                     print("")
#                                     break 
#                                 else:
#                                     print("\nNo se pueden deshacer mas movimientos.\n")
#                                     break 
                   
#                             elif movimiento == "9":
#                                 comprobador_victoria(tablero_usuario)
#                                 if comprobador_victoria(tablero_usuario) == True:
#                                     tablero_usuario = True
#                                     break
#                                 else:
#                                     if intentos_victoria > 1:
#                                         intentos_victoria -= 1
#                                         print("\n","#####" * 12, sep="")
#                                         print("Mmm, algo no está bien. Revisa tu tablero.")
#                                         print("Intentos restantes:", intentos_victoria)
#                                         print("#####" * 12)
#                                         dibujar_tablero(tablero_usuario)
#                                         print("")
#                                     else:
#                                         intentos_victoria -= 1
#                                         break
    
#                             elif movimiento == "8":
#                                 continuar = False
#                                 break 

#                             elif movimiento == "C" or movimiento == "c":
#                                 print("\nElija una fila, una columna y el valor que desea modificar o presione \"Enter\" para las opciones:\n\
# - Deshacer Movimiento\n\
# - Comprobar Victoria\n\
# - Salir\n")   
#                                 break
#                             else:
#                                 print("\nLa opción elegida no es correcta. Vuelva a intentarlo.")
                        

#                         else:
#                             print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n")

                        
#                         if intentos_victoria == 0:
#                             intentos_victoria = False
#                             break
#                         elif continuar == False:
#                             break
#                         elif tablero_usuario == True:
#                             break
                    

#                     if intentos_victoria == False:
#                         print("\nMmm, lo siento, tu tablero no es correcto y se te han acabado las posibilidades de comprobar tu victoria. Deberás comenzar nuevamente.")
#                         break
                            
#                     if continuar == False:
#                         print("\nHa sido un placer jugar contigo. Nos vemos la proxima!")
#                         break
                    
#                     if tablero_usuario == True:
#                         print("\nFelicidades, has ganado!!")
#                         break

#                     while True:
#                         columna = input("columna: ")
#                         if columna in valores_correctos:
#                             columna = int(columna)
#                             lista_columnas.append(columna)
#                             break
#                         else:
#                             print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n")
                            
#                     while True:
#                         valor = input("valor: ")
#                         if valor in valores_correctos:
#                             valor = int(valor)
#                             lista_valores.append(tablero_usuario[fila-1][columna-1])
#                             break
#                         elif valor == "*":
#                             break
#                         else:
#                             print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n")

#                     compr_mov_restringidos = []
#                     compr_mov_restringidos.append(fila-1)
#                     compr_mov_restringidos.append(columna-1)
#                     validador_mov_restringidos = False

#                     for f in movimientos_restringidos:
#                         if compr_mov_restringidos == f:
#                             validador_mov_restringidos = True
#                             break

#                     if validador_mov_restringidos == False:
#                         modificar_tablero(fila, columna, valor, tablero_usuario)
#                         dibujar_tablero(tablero_usuario)
#                     else:
#                         dibujar_tablero(tablero_usuario)
#                         print("\n","#####" * 12, sep="")   
#                         print("Este valor no puede ser modificado. Intente otro.")
#                         print("#####" * 12)

#         if continuar == False:
#             break

#         while (True):
#             reiniciar = input("\nQuieres volver a jugar? Escribe \"S\" para intentarlo nuevamente o \"N\" para salir: ")

#             if reiniciar == "S" or reiniciar == "s":
#                 reiniciar = True
#                 break
#             elif reiniciar == "N" or reiniciar == "n":
#                 reiniciar = False
#                 break
#             else:
#                 print("\nLa opción elegida no es correcta. Vuelva a intentarlo.")

#         if reiniciar == True:
#             print("\n\n","#####" * 10, sep="")   
#             print("             Comencemos nuevamente!")
#             print("#####" * 10)
#             pass
#         else:
#             print("\nHa sido un placer jugar contigo. Nos vemos la proxima!")
#             break

# except KeyboardInterrupt:
#         print("\n\nHasta luego.")

       


#####################################################
#####################################################

# base  = 3
# side  = base*base

# # pattern for a baseline valid solution
# def pattern(r,c): return (base*(r%base)+r//base+c)%side


# # randomize rows, columns and numbers (of valid base pattern)
# from random import sample
# def shuffle(s): return sample(s,len(s)) 
# rBase = range(base) 
# rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
# cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
# nums  = shuffle(range(1,base*base+1))

# # produce board using randomized baseline pattern
# board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

# for line in board: print(line)


