import random

# Mudar Range conforme desejado, quanto maior o Range, maior a dificuldade.
RANGE = range(1, 4)

global numPrimary
global numSecondary
numX = random.choice(RANGE)

def getNumberPrimary():
    global RANGE
    global numPrimary
    
    try:
        numPrimary = int(input('Número primário: ')) 
    except:
        print('')

    if numPrimary in RANGE:
        print('')
    else:
        print('\nNúmero inválido.\n')
        getNumberPrimary()

def getNumberSecondary():
    global RANGE
    global numSecondary
    global numPrimary

    try:
        numSecondary = int(input('Número secundário: '))
    except:
        print('')

    if numSecondary not in RANGE or numSecondary == numPrimary:
        print('\nNúmero inválido ou igual.\n')
        getNumberSecondary()
    else:
        print('')


def game():
    global numPrimary
    global numSecondary
    global numX

    if numPrimary == numX:
        print('============ RESULTADO ============')
        print('Número primário: ', numPrimary)
        print('Número secundário: ', numSecondary)
        print('\nNúmero gerado: ', numX)
        print('\nGanhou!!!')
    elif numSecondary == numX:
        print('============ RESULTADO ============')
        print('Número primário: ', numPrimary)
        print('Número secundário: ', numSecondary)
        print('\nNúmero gerado: ', numX)
        print('\nNão perdeu e nem ganhou!')
    else:
        print('============ RESULTADO ============')
        print('Número primário: ', numPrimary)
        print('Número secundário: ', numSecondary)
        print('\nNúmero gerado: ', numX)
        print('\nPerdeu...')

getNumberPrimary()

getNumberSecondary()
    
game()
