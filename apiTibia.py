#!/usr/bin/python
import requests
import json

def main():
	api_input = input('Nome do personagem: ')

	request = requests.get('https://api.tibiadata.com/v2/characters/{}.json'.format(api_input))
	dados = request.json()
		
	try:
		('{}'.format(dados['characters']['error']))
		print('\n\n === Personagem não existe ===')
	except:
		requestrank = requests.get('https://api.tibiadata.com/v2/highscores/{}.json'.format(dados['characters']['data']['world']))
		rank = requestrank.json()
		nome = dados['characters']['data']['name']
		vocacao = dados['characters']['data']['vocation']
		cidade = dados['characters']['data']['residence']
		mundo = dados['characters']['data']['world']
		level = dados['characters']['data']['level']
		top = rank['highscores']['data'][0]['name']

		print('\n')
		print(nome, 'é um', vocacao, 'que vive em', cidade, end='.')
		print('\n')
		print('Durante anos,', nome, 'tem travado guerras em busca do dominio de', mundo, end='.')
		print('\n')
		print('Seu nível de poder atualmente é', level, end='.')
		print('\n')

		if nome != top:
			print('Constantemente,', nome, 'vem aperfeiçoando suas técnicas de luta e aumentando seu nível de poder, para ser o guerreiro mais poderoso de', mundo, end='.')
			print('\n')
			print('O guerreiro mais forte de', mundo, 'é o', top, end='.')
			print('\n')
			print(nome, 'luta bravamente para alcançá-lo a todo custo!\n')
		else:
			print(nome, 'é o Guerreiro mais forte de', mundo, end='.')
			print('\n')

# ================================================================================================ #		
	print('\n')

	print('Deseja pesquisar outro personagem?\n')
	opt = input('\nDigite "S" ou Pressione qualquer outra tecla para sair: ')

	if (opt == 's' or opt == 'S'):
		main()
	else:
		print('Saindo...')

if __name__=='__main__':
	main()