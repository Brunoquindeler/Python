import random

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
        numSecondary = int(input('\nNúmero secondário: '))
    except:
        print('')

    if numSecondary not in RANGE or numSecondary == numPrimary:
        print('\nNúmero inválido ou igual.')
        getNumberSecondary()
    else:
        print('')


def game():
    global numPrimary
    global numSecondary
    global numX

    if numPrimary == numX:
        print('Número primário: ', numPrimary)
        print('Número secondário: ', numSecondary)
        print('Número gerado: ', numX)
        print('Ganhou!!!')
    elif numSecondary == numX:
        print('Número primário: ', numPrimary)
        print('Número secondário: ', numSecondary)
        print('Número gerado: ', numX)
        print('Não perdeu e nem ganhou!')
    else:
        print('Número primário: ', numPrimary)
        print('Número secondário: ', numSecondary)
        print('Número gerado: ', numX)
        print('Perdeu...')

getNumberPrimary()

getNumberSecondary()
    
game()