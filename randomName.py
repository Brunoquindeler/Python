import random

def main():
	nomeArquivo = input('Nome do arquivo: ')

	try:
		open("{}".format(nomeArquivo)+".txt", "x")
	except:
		print('Arquivo já existe')
		main()

	quantidadeNomes = int(input("Quantidade de nomes gerados: "))

	while quantidadeNomes > 0:
		quantidadeNomes -= 1

		nome = random.choice(['Bruno', 'Gustavo', 'Augusto', 'Felipe', 'João', 'Luciano', 'Fernando', 'Guilherme', 'Eduardo', 'Caio', 'Julio', 'Fábio', 'Jonas', 'Matheus', 'Vinicius', 'Robson', 'Jairo', 'Henrique'])
		sobrenome = random.choice(['Ferreira', 'Silva', 'José', 'Júnior', 'Gonçalves', 'Santos', 'Ribeiro', 'Carvalho', 'Fernandes', 'Couto', 'Morete', 'Videira', 'Coutinho', 'Galhardo', 'Farinha', 'Filho'])

		nomeSobrenome = nome+' '+sobrenome

		f = open("{}".format(nomeArquivo)+".txt", "a")
		f.write(nomeSobrenome + '\n')
		f.close()
			

		print(nomeSobrenome)


# ================================================================================================ #		
	print('\n')

	print ('Gerar outro arquivo?\n')
	opt = input('\nDigite "S" ou Pressione qualquer outra tecla para sair: ')

	if opt == 's' or opt == 'S':
		main()
	else:
		print('\nSaindo...')

if __name__=='__main__':
	main()

## ============================================================================================================================================================================== ##
# Gerar nomes doidos com letras aleatórias

#Lvogal  = ['a','e','i','o','u']
#Lconsoante  = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','w','y','z']

#x = [element.upper() for element in x]
#print('')
#print( random.choice([element.upper() for element in Lconsoante]), random.choice(Lvogal), random.choice(Lconsoante), random.choice(Lvogal), random.choice(Lconsoante), random.choice(Lvogal), sep='', end=' ')
#print( random.choice([element.upper() for element in Lconsoante]), random.choice(Lvogal), random.choice(Lconsoante), random.choice(Lvogal), random.choice(Lconsoante), random.choice(Lvogal), sep='')

## ============================================================================================================================================================================== ##
