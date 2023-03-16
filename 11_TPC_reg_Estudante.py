#!/bin/python3

idade = int(input("Qual é a sua idade? "))

pagamento = (input("Tem Primeira mensalidade regularizada? Rep: (SIM/NAO) "))

if idade >= 18 and pagamento.upper() == "NAO" :
    print(" - "," Tem que pagar Primeira Mensalidade, Inscricao Pendente!")

elif idade <= 18 and pagamento.upper() == "NAO" :
    print(" - "," Você ainda é menor de idade. & Nao pode pagar")

elif idade >= 18 and pagamento.upper() == "SIM" :
	print("Parabéns, pode se escrever!")
	#Cria uma lista com os cursos e seus preços
	cursos_precos = {'network Penetration testing': 11100.0, 'Network Defender': 11200, 'Network Pen testing Advanced': 11300.0, 'web App Defender': 10300.0, 'Delivery Method':10500}               
	curso_escolhido = input('Digite o nome do curso: ') # Recebe o nome do curso escolhido pelo utilizador atravez do teclado  




# Verifica se o curso escolhido está na lista de cursos disponíveis
	if curso_escolhido in cursos_precos:
	
		#adicionou dia 15
		preco = cursos_precos[curso_escolhido]
		print(f"O preço do curso {curso_escolhido} é {preco:.2f}MT")
		# Cria um dicionário vazio para armazenar as informações do estudante
		estudante = {}
		
		# Recebe as informações do estudante
		estudante['nome'] = input('Digite seu nome: ')
		# Adiciona o curso escolhido à lista de cursos do estudante
		estudante['cursos'] = [curso_escolhido]
		
		# Imprime as informações do estudante e o curso escolhido
		print('Estudante registrado com sucesso!')
		print('Nome: ', estudante['nome'])
		print('Curso: ', estudante['cursos'])
    

else:
	print(" - ", " Você ainda é menor de idade. Mesmo pagando nao pode frequentar o curso")



