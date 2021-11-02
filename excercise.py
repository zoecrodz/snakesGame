import random

def openMenu(partidasJugadas, estadisticas): 
    opcion = int(input('Bienvenido al menú, ingrese una opción: \n 1) Iniciar Partida \n 2) Mostrar estadísticas \n 3) Resetear estadísticas \n 4) Salir \n'))
    if opcion == 1:
        partidasJugadas = partidasJugadas + 1
        playSnakes(partidasJugadas, estadisticas)
    elif opcion == 2:
        if partidasJugadas == 0:
            print('No jugaste todavía!')
        else: 
            print('Partidas jugadas: \n', partidasJugadas, '\n Estadisticas: \n', estadisticas)
        openMenu(partidasJugadas, estadisticas)
    elif opcion == 3:
        if partidasJugadas == 0:
            print('No jugaste todavía!')
        else:
            partidasJugadas = 0
            estadisticas = {
            'S': 0,
            'E': 0,
            'M': 0,
            'R': 0,
            'CB': 0,
            'HL': 0
            }
        openMenu(partidasJugadas, estadisticas)
    elif opcion == 4:
        return print('Nos vemos pronto!')

def playSnakes(partidasJugadas, estadisticas):
    fila1 = [1, 2, 'E', 4, 5, 'E', 7, 8, 9, 'M']
    fila2 = [11, 'R', 13, 14, 15, 16, 'M', 18, 19, 20]
    fila3 = ['CB', 22, 23, 24, 'CB', 26, 27, 28, 29, 30]
    fila4 = [31, 32, 33, 34, 35, 'S', 37, 38, 39, 40]
    fila5 = [41, 42, 43, 44, 45, 46, 47, 'S', 49, 50]
    fila6 = [51, 52, 53, 54, 55, 56, 'E', 'S', 59, 60]
    fila7 = [61, 62, 'S', 64, 65, 'CB', 67, 'M', 69, 'CB']
    fila8 = [71, 'E', 73, 74, 75, 76, 'CB', 78, 79, 80]
    fila9 = [81, 82, 83, 84, 'E', 'S', 87, 'S', 89, 90]
    fila10 = [91, 92, 93, 94, 95, 'HL', 97, 'S', 99, 100]
    diccionario = { 3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17 }
    cascara1 = random.choice([i for i in range(21,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36]])
    cascara2 = random.choice([i for i in range(21,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36, cascara1]])
    cascara3 = random.choice([i for i in range(21,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36, cascara1, cascara2]])
    cascara4 = random.choice([i for i in range(21,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36, cascara1, cascara2,cascara3]])
    cascara5 = random.choice([i for i in range(21,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36, cascara1, cascara2, cascara3, cascara4]])
    magico1 = random.choice([i for i in range(1,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36, cascara1, cascara2, cascara3, cascara4, cascara5]])
    magico2 = random.choice([i for i in range(1,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36, cascara1, cascara2, cascara3, cascara4, cascara5, magico1]])
    magico3 = random.choice([i for i in range(1,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36, cascara1, cascara2, cascara3, cascara4, cascara5, magico1, magico2]])
    rushero = random.choice([i for i in range(1,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36,10,20,30,40,50,60,70,80,90, cascara1, cascara2, cascara3, cascara4, cascara5, magico1, magico2, magico3]])
    hongos =  random.choice([i for i in range(1,99) if i not in [3,6,57,72,85,86,88,98,63,58,48,36,1,11,21,31,41,51,61,71,81,91, cascara1, cascara2, cascara3, cascara4, cascara5, magico1, magico2, magico3, rushero]])
    jugador1 = input('Ingrese el nombre del jugador 1: ')
    jugador2 = input('Ingrese el nombre del jugador 2: ')
    posicion1 = 1
    posicion2 = 1
    start = False
    jugadorActual = jugador1
    input('Ingrese la tecla enter para comenzar')
    start = True
    while start == True:
        print('\n',fila10,'\n',fila9,'\n',fila8,'\n',fila7,'\n',fila6,'\n',fila5,'\n',fila4,'\n',fila3,'\n',fila2,'\n',fila1,'\n')
        dado = 0
        print(jugadorActual, 'debe tirar el dado')
        input('Ingrese la tecla enter para tirar el dado')
        if jugadorActual == jugador1:
            posicionActual = posicion1
        else:
            posicionActual = posicion2
        print('su posición actual es', posicionActual)
        dado = random.randint(1,6)
        print('el dado sacó:', dado)
        posicionActual = posicionActual + dado
        if posicionActual >= 100: 
            print('el jugador', jugadorActual, 'ganó la partida')
            openMenu(partidasJugadas, estadisticas)
        else:
            if posicionActual == 3:
                posicionActual = diccionario[3]
                estadisticas["E"] += 1
            elif posicionActual == 6:
                posicionActual = diccionario[6]
                estadisticas["E"] += 1
            elif posicionActual == 36:
                posicionActual = diccionario[36]
                estadisticas["S"] += 1
            elif posicionActual == 57:
                posicionActual = diccionario[57]
                estadisticas["E"] += 1
            elif posicionActual == 58:
                estadisticas["S"] += 1
                posicionActual = diccionario[58]
            elif posicionActual == 63:
                posicionActual = diccionario[63]
                estadisticas["S"] += 1
            elif posicionActual == 48:
                posicionActual = diccionario[48]
                estadisticas["S"] += 1
            elif posicionActual == 72:
                posicionActual = diccionario[72]
                estadisticas["E"] += 1
            elif posicionActual == 98:
                posicionActual = diccionario[98]
                estadisticas["S"] += 1
            elif posicionActual == 85:
                posicionActual = diccionario[85]
                estadisticas["E"] += 1
            elif posicionActual == 86:
                posicionActual = diccionario[86]
                estadisticas["S"] += 1
            elif posicionActual == 88:
                posicionActual = diccionario[88]
                estadisticas["S"] += 1
            elif posicionActual == magico1:
                posicionActual = random.randint(2,99)
                estadisticas["M"] += 1
            elif posicionActual == magico2:
                posicionActual = random.randint(2,99)
                estadisticas["M"] += 1
            elif posicionActual == magico3:
                posicionActual = random.randint(2,99)
                estadisticas["M"] += 1
            elif posicionActual == rushero:
                posicionActual = ((math.floor(posicionActual / 10)) * 10) + 10
                estadisticas["R"] += 1
            elif posicionActual == cascara1:
                posicionActual -= 10
                estadisticas["CB"] += 1
            elif posicionActual == cascara2:
                posicionActual -= 10
                estadisticas["CB"] += 1
            elif posicionActual == cascara3:
                posicionActual -= 10
                estadisticas["CB"] += 1
            elif posicionActual == cascara4:
                posicionActual -= 10
                estadisticas["CB"] += 1
            elif posicionActual == cascara5:
                posicionActual -= 10
                estadisticas["CB"] += 1
            elif posicionActual == hongos:
                posicionActual = (math.floor(posicionActual / 10)) * 10
                estadisticas["HL"] += 1
        print(jugadorActual, 'ahora está en la posición', posicionActual)
        if jugadorActual == jugador1:
            posicion1 = posicionActual
            jugadorActual = jugador2
        else:
            posicion2 = posicionActual 
            jugadorActual = jugador1
    
openMenu(0, {
        'S': 0,
        'E': 0,
        'M': 0,
        'R': 0,
        'CB': 0,
        'HL': 0
    })
