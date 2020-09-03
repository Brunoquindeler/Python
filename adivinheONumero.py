import random

def main():
    print('====== ACERTE O NÚMERO ======\n')

    try:
        nEscolhido = int(input('Escolha um número de 1 a 10: '))
    except:
        print('Isto não é um número.\n')
        main()

    if nEscolhido > 10:
        print('Número inválido.\n')
        main()

    n = random.randint(1, 10)
    print('\nNúmero gerado:', n)

    if n == nEscolhido:
        print('ACERTOU!!!\n')
    else:
        print('ERROU...\n')
        main()

if __name__=='__main__':
    main()
