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
                posicionActual = 18
                estadisticas["E"] += 1
            elif posicionActual == 6:
                posicionActual = 67
                estadisticas["E"] += 1
            elif posicionActual == 10:
                posicionActual = random.randint(2,99)
                estadisticas["M"] += 1
            elif posicionActual == 12:
                posicionActual = 20
                estadisticas["R"] += 1
            elif posicionActual == 17:
                posicionActual = random.randint(2,99)
                estadisticas["M"] += 1
            elif posicionActual == 25:
                posicionActual = 5
                estadisticas["CB"] += 1
            elif posicionActual == 36:
                posicionActual = 17
                estadisticas["S"] += 1
            elif posicionActual == 21:
                posicionActual = 1
                estadisticas["CB"] += 1
            elif posicionActual == 48:
                posicionActual = 12
                estadisticas["S"] += 1
            elif posicionActual == 57:
                posicionActual = 83
                estadisticas["E"] += 1
            elif posicionActual == 58:
                estadisticas["S"] += 1
                posicionActual = 37
            elif posicionActual == 63:
                posicionActual = 22
                estadisticas["S"] += 1
            elif posicionActual == 66:
                posicionActual = 46
                estadisticas["CB"] += 1
            elif posicionActual == 68:
                posicionActual = random.randint(2,99)
                estadisticas["M"] += 1
            elif posicionActual == 70:
                posicionActual = 50
                estadisticas["CB"] += 1
            elif posicionActual == 72:
                posicionActual = 89
                estadisticas["E"] += 1
            elif posicionActual == 77:
                posicionActual = 57
                estadisticas["CB"] += 1
            elif posicionActual == 85:
                posicionActual = 96
                estadisticas["E"] += 1
            elif posicionActual == 86:
                posicionActual = 45
                estadisticas["S"] += 1
            elif posicionActual == 88:
                posicionActual = 31
                estadisticas["S"] += 1
            elif posicionActual == 96:
                posicionActual = 91
                estadisticas["HL"] += 1
            elif posicionActual == 98:
                posicionActual = 79
                estadisticas["S"] += 1
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
