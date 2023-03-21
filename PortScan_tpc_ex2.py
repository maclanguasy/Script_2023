#!/bin/python3

import socket

# Obter endereço IP a partir do teclado
ip_address = input("Digite o endereço IP a ser testado: ")

# Obter lista de portas a partir do teclado

ports = input("Digite as portas a serem testadas (separadas por vírgula): ")

ports_list = [int(port.strip()) for port in ports.split(',')]



# Loop através das portas especificadas
try:
    for port in ports_list:
        # Cria um objeto socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Tenta se conectar à porta especificada
        result = sock.connect_ex((ip_address, port))

        # Se a conexão for bem-sucedida, imprime que a porta está aberta
        if result == 0:
            print("Porta {} está aberta".format(port))
        # Caso contrário, imprime que a porta está fechada
        else:
            print("Porta {} está fechada".format(port))
            sock.close()
            
except:
    print(" o Seu endereco ou a porta nao foi bem defenido, Escolha uma opção:")
    print("1 - Ver Exemplo de como preencher'")
    print("2 - Sair:")

    opcao = int(input("Preencha 1/2: "))

    if opcao == 1:
        print("Substitua <endereço_ip> pelo endereço IP/nome que deseja testar e <80>, <443>, etc. pelas portas que deseja testar (separadas por espaços)")
    elif opcao == 2:
        print("Programa fechado")
    else:
        print("Opção inválida")
        
    
