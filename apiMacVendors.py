import requests

def main():
	inputmac = input('MAC: ')

	requestmac = requests.get('https://api.macvendors.com/{}'.format(inputmac))

	try:
		('{}'.format(requestmac.json()['errors'])) 
		print('\n\n === MAC não existe ===\n\n')
	except:
		print('\n')
		print('=======================================')
		print(requestmac.text)
		print('=======================================')

# ================================================================================================ #		
	print('\n')
	print('Deseja pesquisar outro MAC?\n')
	opt = input('\nDigite "S" ou Pressione qualquer outra tecla para sair: ')

	if (opt == 's' or opt == 'S'):
		main()
	else:
		print('Saindo...')

if __name__=='__main__':
	main()