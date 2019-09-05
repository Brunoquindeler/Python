import random

def main():
    print('====== ACERTE O NÚMERO ======\n')

    try:
        nEscolhido = int(input('Escolha um número de 1 a 10: '))
    except:
        print('Isto não é um número.')
        main()

    if nEscolhido > 10:
        print('Número inválido.')
        main()

    n = random.randint(1, 10)
    print('Número gerado:', n)

    if n == nEscolhido:
        print('ACERTOU!!!')
    else:
        print('ERROU...')
        main()

if __name__=='__main__':
    main()