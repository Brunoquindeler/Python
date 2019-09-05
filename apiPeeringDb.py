import requests

def main():
	request = requests.get('https://www.peeringdb.com/api/net/7169')
	dados = request.json()

	nome = dados['data'][0]['org']['name']
	website = dados['data'][0]['org']['website']
	endereco = dados['data'][0]['org']['address1']
	cidade = dados['data'][0]['org']['city']
	zipcode = dados['data'][0]['org']['zipcode']
	estado = dados['data'][0]['org']['state']
	pais = dados['data'][0]['org']['country']
	status = dados['data'][0]['org']['status']
	nota = dados['data'][0]['notes']
	noc = dados['data'][0]['poc_set'][0]['name']
	phone = dados['data'][0]['poc_set'][0]['phone']
	mail = dados['data'][0]['poc_set'][0]['email']

	print('=================================\n')
	print('Nome:', nome)
	print('Website:', website)
	print('Endereço:', endereco)
	print('Cidade:', cidade)
	print('Código Postal:', zipcode)
	print('Estado:', estado)
	print('País:', pais)
	print('Status:', status)
	print('\n')
	print('---------------------------------\n')
	print(noc)
	print('Telefone:', phone)
	print('E-mail:', mail)

	print('\n')
	print(nota)
	print('\n=================================')

if __name__=='__main__':
	main()