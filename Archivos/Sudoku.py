def presentacion_juego():
    """Función que presenta el juego, lo explica y da lugar al comienzo o no."""

    # Se explica por pantalla las reglas generales del juego.
    print("""
            \"Bienvenidos al Sudoku\"

El juego se compone de 9 filas y 9 columnas.
En cada espacio, deberás añadir un número entre
el 1 y el 9. Cada fila y cada columna deberá
contener todos los números del 1 al 9 sin importar
el orden. A su vez, los subcuadros de 3x3 (3 filas
y 3 columnas) deberán tener también todos los
números. El juego finaliza cuando logres completar
cada fila, columna y subcuadro con los valores
entre el 1 y el 9. Puedes añadir y quitar cada
número las veces que haga falta excepto los números
iniciales.
Si deseas continuar escribe "C". En caso contrario
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
            print("\nLa opción elegida no es correcta. Vuelve a intentarlo.")
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
       evaluar si son válidos o no. Es decir, devuelve cada columna o cada subgrupo por separado
       para verificar si cumplen con las condiciones de victoria o no.  """

    columnas_ordenadas = []
    subgrupos_ordenados = [[] for i in range (9)]

    # Se itera por cada fila del tablero.
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
        # Comprueba que no haya espacios "vacíos" representados con un "*".
        for elem in fila:
            if elem == "*":
                return False
        if sorted(fila) != comparador:
            return False
    else:
        return True


def random_tableros(tablero_comprobar):
    """Función para generar tableros nuevos con valores aleatorios. Se utiliza un for que va agregando cada subgrupo
    del juego."""

    # Varible que determina sobre qué fila se van a añadir los valores.
    contador_filas = 0
    # Varible que determina sobre qué columnas se van a añadir los valores.
    contador_columnas = 0

    for subgrupo in range(9):
        # Varible que determina sobre qué fila se van a añadir los valores y será mutable según el subgrupo que se esté evaluando.
        indice_filas = 0
        # Varible que determina sobre qué columna se van a añadir los valores y será mutable según el subgrupo que se esté evaluando.
        indice_columnas = 0
        if subgrupo == 0:
            # Se llama a la función que comprueba que los valores cumplan con las condiciones del juego.
            comprobar_lineas_random_tablero(tablero_comprobar, contador_filas, contador_columnas)
        else:
            if subgrupo == 1:
                indice_columnas = 3
            elif subgrupo == 2:
                indice_columnas = 6
            elif subgrupo == 3:
                indice_filas = 3
            elif subgrupo == 4:
                indice_filas = 3
                indice_columnas = 3
            elif subgrupo == 5:
                indice_filas = 3
                indice_columnas = 6
            elif subgrupo == 6:
                indice_filas = 6
            elif subgrupo == 7:
                indice_filas = 6
                indice_columnas = 3
            elif subgrupo == 8:
                indice_filas = 6
                indice_columnas = 6

            # Se llama a la función que intenta agregar nuevos subgrupos al tablero para luego comprobarlos.
            lanzar_tablero(tablero_comprobar, contador_filas, indice_filas,contador_columnas,indice_columnas,subgrupo)


def lanzar_tablero(tablero,contador_filas, indice_filas, contador_columnas, indice_columnas, subgrupo):
    """Función que llama a la función que comprueba que los valores cumplan con las condiciones del juego y evalúa
    su resultado. Si el resultado no cumple con las condiciones restablece a cero las lineas de 3 a 6 o de 6 a 9."""

    comprobar_lineas_random_tablero(tablero, contador_filas+indice_filas, contador_columnas+indice_columnas)
    
    # Se ordena el tablero para evaluar si el subgrupo a analizar tiene espacios vacios (representados con "*").
    for valor in ordenar_tablero(tablero)[1][subgrupo]:
        if valor == "*":
            for linea in range(3):
                # Restablece a cero las líneas de 3 a 6.
                if 2 < subgrupo < 6:
                    tablero[linea+3] = ["*" for x in range (9)]
                # Restablece a cero las líneas de 6 a 9.
                elif 5 < subgrupo < 9:
                    tablero[linea+6] = ["*" for x in range (9)]


def comprobar_lineas_random_tablero(tablero_comprobar, contador_filas, contador_columnas):
    """Función que intenta agregar un valor por cada espacio del tablero y comprueba que cumpla con las condiciones
    del juego."""

    from random import shuffle

    valores_disponibles = [1+valor for valor in range(9)]
    # Desordena la lista creada para generar subgrupos aleatorios.
    shuffle(valores_disponibles)
    # Se establece un bucle que intenta agregar un valor dependiendo de las filas y columnas pasadas.
    # Como resultado se obtiene un subgrupo que luego será evaluado si es un subgrupo válido.
    for numero in range(3):
        # Variable vinculada a los índices de las columnas. Si se agrega un valor la variable muta para pasar a la columna siguiente.
        valor = 0
        contador_iter = 0
        while True:
            # Evalúa si el valor está en la fila indicada.
            if valores_disponibles[0] not in tablero_comprobar[contador_filas+numero]:
                # Evalúa si el valor está en la columna indicada.
                if valores_disponibles[0] not in ordenar_tablero(tablero_comprobar)[0][contador_columnas+valor]:
                    # Se añade el valor en el índice que corresponda.
                    tablero_comprobar[contador_filas+numero][valor+contador_columnas] = valores_disponibles[0]
                    # Se elimina el valor añadido para evitar duplicidad.
                    valores_disponibles.remove(valores_disponibles[0])
                    valor += 1
                else:
                    # Se desordena la lista para intentar agregar otro valor.
                    shuffle(valores_disponibles)
                    contador_iter += 1
            else:
                shuffle(valores_disponibles)
                contador_iter += 1

            # Finaliza el bucle cuando se añaden 3 elementos a una fila para luego pasar a la fila siguiente.
            if valor == 3:
                break
            # Finaliza el bucle cuando se alcanza el máximo de intentos de "desordenar la lista" para evitar un bucle infinito.
            elif contador_iter == 20:
                break


def comprobador_tablero_random(tablero_comprobar):
    """Función que evalúa si un tablero es correcto. Lo retorna si es "True" o llama a la función de generar uno
    nuevo en caso de que sea "False"."""

    while comprobador_victoria(tablero_comprobar) == False:
        # Restablece el tablero a cero para enviar a la función un tablero vacío.
        tablero_comprobar = [["*" for c in range(9)] for f in range(9)]
        random_tableros(tablero_comprobar)
    return tablero_comprobar


def generar_tableros_aleatorios(dificultad):
    """Función que toma un tablero correcto y oculta aleatoriamente sus valores reemplazándolos por "*"."""

    from random import randrange

    # Se genera un tablero vacío de 9x9.
    tablero_random = [["*" for c in range(9)] for f in range(9)]
    # Tablero final que se va a retornar.
    tablero_reordenado = [[], [], [], [], [], [], [], [], [],]

    # Se genera un tablero válido nuevo.
    tablero_a_generar = comprobador_tablero_random(tablero_random)
    # Se reordena el tablero según sus subgrupos.
    valores_aleatorios = ordenar_tablero(tablero_a_generar)[1]

    # Bucle que agregará 1,2 o 3 valores por cada subgrupo.
    for i in range(9):
        # Se generan índices aleatorios para determinar en qué parte del subgrupo se van a agregar los valores.
        indices_aleatorio1, indices_aleatorio2, indices_aleatorio3 = randrange(0,9), randrange(0,9), randrange(0,9)
        while True:
            # Se verifica que los indices generados no se repitan.
            if indices_aleatorio1 == indices_aleatorio2:
                indices_aleatorio2 = randrange(0,9)
            elif indices_aleatorio3 == indices_aleatorio2 or indices_aleatorio3 == indices_aleatorio1:
                indices_aleatorio3 = randrange(0,9)
            else:
                break
        # Se agregan 3 valores por subgrupo en caso de que la dificultad elegida sea "Fácil".
        if dificultad == "F" or dificultad == "f":
            tablero_random[i][indices_aleatorio1] = valores_aleatorios[i][indices_aleatorio1]
            tablero_random[i][indices_aleatorio2] = valores_aleatorios[i][indices_aleatorio2]
            tablero_random[i][indices_aleatorio3] = valores_aleatorios[i][indices_aleatorio3]
        # Se agregan 2 valores por subgrupo en caso de que la dificultad elegida sea "Medio".
        if dificultad == "M" or dificultad == "m":
            tablero_random[i][indices_aleatorio1] = valores_aleatorios[i][indices_aleatorio1]
            tablero_random[i][indices_aleatorio2] = valores_aleatorios[i][indices_aleatorio2]
        # Se agregan 1 valor por subgrupo en caso de que la dificultad elegida sea "Difícil".
        if dificultad == "D" or dificultad == "d":
            tablero_random[i][indices_aleatorio1] = valores_aleatorios[i][indices_aleatorio1]

    # El tablero ordenado por subgrupos se reordena y se vuelca en el tablero final que utilizará el jugador.
    for elem in range(0,9,3):
        for i in range(3):
            tablero_reordenado[elem] += tablero_random[elem+i][:3]
            tablero_reordenado[elem+1] += tablero_random[elem+i][3:6]
            tablero_reordenado[elem+2] += tablero_random[elem+i][6:]

    return tablero_reordenado


# #####################################################
# #########       PRESENTACIÓN DEL JUEGO      #########
# #####################################################

try:
    
    while(True):
        # Se llama a la función inicial y se comienza o finaliza el juego según lo que se responda.
        if presentacion_juego() == None:
            break
        else:
            print("""\nVamos a lo primero. Qué nivel de dificultad quieres?
Si quieres un juego fácil escribe "F". Si quieres que
sea un nivel medio escribe "M". Si eres valiente
escribe "D".\n""")
            # Se elije la dificultad del juego para luego crear un tablero en consecuencia.
            dificultad = input("Opción elegida: ")
            opciones_correctas = ["F", "f", "M", "m", "D", "d"]

            while dificultad not in opciones_correctas:
                print(f"\nLa opcion elegida \"{dificultad}\" no es válida. Debe escribir \"F\", \"M\" o \"D\".\n")
                dificultad = input("Opción elegida: ")
            if dificultad in opciones_correctas[0:2]:
                valor = 3
            elif dificultad in opciones_correctas[2:4]:
                valor = 2
            else:
                valor = 1

            # Se explica por pantalla las reglas puntuales del juego.
            print(f"""\nAlgunas aclaraciones antes de empezar. Teniendo en
cuenta la dificultad que has elegido, se ha generado
un tablero con {valor} valor/es cargado/s aleatoriamente
por cada subgrupo. Tu objetivo es completar todos los
campos. Para ello se te pedirá una fila, una columna y
el valor a introducir de manera que vayas completando
todo el tablero. No puedes modificar los números ya
cargados previamente pero sí puedes deshacer todos los
cambios realizados. También, puedes reemplazar un valor
que hayas agregado por un "*" si deseas restablecerlo a
cero. Cuando creas que has terminado tienes 3 intentos
para comprobar tu victoria.

        Estás listo para comenzar?

Escribe "C" para continuar o "S" para salir.\n""")

            # Bucle que evalúa si el juego comienza o no.
            while(True):
                inicio = input("Opción elegida: ")
                if inicio == "S" or inicio == "s":
                    print("\nTan rápido te vas? Bueno, nos vemos la proxima.")
                    break
                elif inicio == "C" or inicio == "c":
                    print("")
                    print("#####" * 12)
                    print("\nGenerando un tablero.\n")
                    break
                else:
                    print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n")

            if inicio == "S" or inicio == "s":
                break

#####################################################
#########       AQUÍ COMIENZA EL JUEGO      #########
#####################################################

            else:
                # Tablero generado a partir de la dificultad elegida con el que el usuario jugará.
                tablero_usuario = generar_tableros_aleatorios(dificultad)
                print("#####" * 12)
                print("\nComencemos el juego!")
                dibujar_tablero(tablero_usuario)
                movimientos_restringidos = []
                contador = 0

                # Bucle que recupera el tablero generado, comprueba donde hay números y los añade a la variable
                # "movimientos_restringidos" que serán los únicos valores que el usuario no podrá modificar.
                for ind_fila, fila in enumerate(tablero_usuario):
                    for ind_col, elem in enumerate(fila):
                        if elem == "*":
                            pass
                        else:
                            movimientos_restringidos.append([])
                            movimientos_restringidos[contador].append(ind_fila)
                            movimientos_restringidos[contador].append(ind_col)
                            contador +=1

                # Se generan 3 listas cuyos índices se usarán como backup para "deshacer movimientos". Permitirán al usuario
                # volver al punto anterior.
                lista_filas = []
                lista_columnas = []
                lista_valores = ["*"]
                intentos_victoria = 3

                while(True):

                    continuar = True
                    valores_correctos = ["1","2","3","4","5","6","7","8","9"]

                    print("\nElija una fila, una columna y el valor que desea modificar o presione \"Enter\" para las opciones:\n\
- Deshacer Movimiento\n\
- Comprobar Victoria\n\
- Salir\n")

                    while True:
                        # Se pregunta la fila a modificar.
                        fila = input("Fila: ")
                        if fila in valores_correctos:
                            fila = int(fila)
                            lista_filas.append(fila)
                            break

                        # Se ingresa al menú de opciones.
                        while fila == "":
                            movimiento = input("\nPara deshacer el último movimiento escribe \"0\".\
\nSi quieres comprobar tu victoria escribe \"9\".\
\nPara salir \"8\".\
\nSi no escribe \"C\":  ")
                            # Condición que se utiliza para deshacer movimientos y volver al punto anterior.
                            if movimiento == "0":
                                if len(lista_filas) > 0:
                                    modificar_tablero(lista_filas[-1], lista_columnas[-1], lista_valores[-1], tablero_usuario)
                                    lista_filas.pop()
                                    lista_columnas.pop()
                                    lista_valores.pop()
                                    dibujar_tablero(tablero_usuario)
                                    print("")
                                    break
                                else:
                                    print("\nNo se pueden deshacer mas movimientos.\n")
                                    break
                            # Condición que se utiliza para comprobar la victoria.
                            elif movimiento == "9":
                                comprobador_victoria(tablero_usuario)
                                if comprobador_victoria(tablero_usuario) == True:
                                    tablero_usuario = True
                                    break
                                else:
                                    if intentos_victoria > 1:
                                        intentos_victoria -= 1
                                        print("\n","#####" * 12, sep="")
                                        print("Mmm, algo no está bien. Revisa tu tablero.")
                                        print("Intentos restantes:", intentos_victoria)
                                        print("#####" * 12)
                                        dibujar_tablero(tablero_usuario)
                                        print("")
                                    else:
                                        intentos_victoria -= 1
                                        break
                            # Condición que se utiliza para finalizar el juego.
                            elif movimiento == "8":
                                continuar = False
                                break

                            elif movimiento == "C" or movimiento == "c":
                                print("\nElija una fila, una columna y el valor que desea modificar o presione \"Enter\" para las opciones:\n\
- Deshacer Movimiento\n\
- Comprobar Victoria\n\
- Salir\n")
                                break
                            else:
                                print("\nLa opción elegida no es correcta. Vuelva a intentarlo.")

                        else:
                            print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n")

                        # Condicionales que comprueban si hay una derrota, si se decide salir del juego o si hay victoria. 
                        if intentos_victoria == 0:
                            intentos_victoria = False
                            break
                        elif continuar == False:
                            break
                        elif tablero_usuario == True:
                            break
                    
                    # Mensajes por pantalla si hay una derrota, si se decide salir del juego o si hay victoria.
                    if intentos_victoria == False:
                        print("\nMmm, lo siento, tu tablero no es correcto y se te han acabado las posibilidades de comprobar tu victoria. Deberás comenzar nuevamente.")
                        break
                    if continuar == False:
                        print("\nHa sido un placer jugar contigo. Nos vemos la proxima!")
                        break
                    if tablero_usuario == True:
                        print("\nFelicidades, has ganado!!")
                        break

                    # Se pregunta la columna a modificar.
                    while True:
                        columna = input("columna: ")
                        if columna in valores_correctos:
                            columna = int(columna)
                            lista_columnas.append(columna)
                            break
                        else:
                            print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n")
                    
                    # Se pregunta el valor a introducir.
                    while True:
                        valor = input("valor: ")
                        if valor in valores_correctos:
                            valor = int(valor)
                            lista_valores.append(tablero_usuario[fila-1][columna-1])
                            break
                        elif valor == "*":
                            break
                        else:
                            print("\nLa opción elegida no es correcta. Vuelva a intentarlo.\n")

                    # Variable en donde se añade la fila y la columna del valor elegido por el usuario para comprobarlo con la
                    # variable "movimientos_restringidos" y determinar si es un campo modificable o no.
                    compr_mov_restringidos = []
                    compr_mov_restringidos.append(fila-1)
                    compr_mov_restringidos.append(columna-1)
                    validador_mov_restringidos = False

                    # Bucle que itera sobre los "movimientos_restringidos" y los compara con lo introducido por el usuario.
                    for f in movimientos_restringidos:
                        if compr_mov_restringidos == f:
                            validador_mov_restringidos = True
                            break

                    if validador_mov_restringidos == False:
                        modificar_tablero(fila, columna, valor, tablero_usuario)
                        dibujar_tablero(tablero_usuario)
                    else:
                        dibujar_tablero(tablero_usuario)
                        print("\n","#####" * 12, sep="")
                        print("Este valor no puede ser modificado. Intente otro.")
                        print("#####" * 12)

        # Condición que finaliza el juego.
        if continuar == False:
            break

        # Bucle para reiniciar el juego o no.
        while (True):
            reiniciar = input("\nQuieres volver a jugar? Escribe \"S\" para intentarlo nuevamente o \"N\" para salir: ")

            if reiniciar == "S" or reiniciar == "s":
                reiniciar = True
                break
            elif reiniciar == "N" or reiniciar == "n":
                reiniciar = False
                break
            else:
                print("\nLa opción elegida no es correcta. Vuelva a intentarlo.")

        if reiniciar == True:
            print("\n\n","#####" * 10, sep="")
            print("             Comencemos nuevamente!")
            print("#####" * 10)
            pass
        else:
            print("\nHa sido un placer jugar contigo. Nos vemos la proxima!")
            break

except KeyboardInterrupt:
        print("\n\nHasta luego.")

