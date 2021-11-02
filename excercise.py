import random

def openMenu(): 
    opcion = input('Bienvenido al menú, ingrese una opción: /n 1) Iniciar Partida /n 2) Mostrar estadísticas 3) Resetear estadísticas 4) Salir')
    if opcion == 1:
        playSnakes()
    elif opcion == 2:
        mostrarEstadisticas()
    elif opcion == 3;
        reseterEstadisticas()
    elif opcion == 4;
        print('Nos vemos pronto!')
        break

def mostrarEstadisticas: 
    print('estadisticas')
    
def resetearEstadisticas:
    print('reset')

def playSnakes():
    jugador1 = input('Ingrese el nombre del jugador 1: ')
    jugador2 = input('Ingrese el nombre del jugador 2: ')
    posicion1 = 1
    posicion2 = 1
    start = False
    jugadorActual = jugador1
    input('Ingrese cualquier letra para comenzar')
    start = True
    while start == True:
        dado = 0
        print(jugadorActual, 'debe tirar el dado')
        input('Ingrese cualquier letra para tirar el dado')
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
            start = False
        else:
            if posicionActual == 3:
                posicionActual = 18
            elif posicionActual == 6:
                posicionActual = 67
            elif posicionActual == 10:
                posicionActual = random.randint(2,99)
            elif posicionActual == 12:
                posicionActual = 20
            elif posicionActual == 17:
                posicionActual = random.randint(2,99)
            elif posicionActual == 25:
                posicionActual = 5
            elif posicionActual == 36:
                posicionActual = 17
            elif posicionActual == 21:
                posicionActual = 1
            elif posicionActual == 48:
                posicionActual = 12
            elif posicionActual == 57:
                posicionActual = 83
            elif posicionActual == 58:
                posicionActual = 37
            elif posicionActual == 63:
                posicionActual = 22
            elif posicionActual == 66:
                posicionActual = 46
            elif posicionActual == 68:
                posicionActual = random.randint(2,99)
            elif posicionActual == 70:
                posicionActual = 50
            elif posicionActual == 72:
                posicionActual = 89
            elif posicionActual == 77:
                posicionActual = 57
            elif posicionActual == 85:
                posicionActual = 96
            elif posicionActual == 86:
                posicionActual = 45
            elif posicionActual == 88:
                posicionActual = 31
            elif posicionActual == 96:
                posicionActual = 91
            elif posicionActual == 98:
                posicionActual = 79
            print(jugadorActual, 'ahora está en la posición', posicionActual)
            if jugadorActual == jugador1:
                posicion1 = posicionActual
                jugadorActual = jugador2
            else:
                posicion2 = posicionActual 
                jugadorActual = jugador1
    
playSnakes()
