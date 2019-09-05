#!/usr/bin/python
import requests
import json

def main():
	api_input = input('CEP: ')

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(api_input))
	
	#print(request.status_code)
		
	if request.status_code == 200:
		dados = request.json()

		cep = dados['cep']
		logradouro = dados['logradouro']
		complemento = dados['complemento']
		bairro = dados['bairro']
		localidade = dados['localidade']
		uf = dados['uf']
		unidade = dados['unidade']
		ibge = dados['ibge']
		gia = dados['gia']


		print('\n')
		print('CEP:', cep)
		#print(logradouro)
		#print(complemento)
		#print(bairro)
		print(localidade, '-', uf)
		#print(uf)
		#print(unidade)
		print('IBGE:', ibge)
		#print(gia)
	else:
		print('\n\n === CEP não existe ===')

# ================================================================================================ #		
	print('\n')

	print('Deseja pesquisar outro CEP?\n')
	opt = input('\nDigite "S" ou Pressione qualquer outra tecla para sair: ')

	if (opt == 's' or opt == 'S'):
		main()
	else:
		print('Saindo...')

if __name__=='__main__':
	main()