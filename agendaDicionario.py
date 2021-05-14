# Desenvolva utilizando DICIONÁRIOS.

# Escreva um programa que permita gerenciar o banco de dados de
# clientes de uma empresa. Os clientes serão salvos em um dicionário no qual a chave de
# cada cliente será seu CPF, e o valor será outro dicionário com os dados do cliente
# (nome, endereço, telefone, email, preferencial), onde preferencial terá o valor True se
# for de um cliente especial. 
# O programa deve solicitar ao usuário uma opção no seguinte
# menu: (1) Adicionar cliente, (2) Remover cliente, (3) Mostrar cliente, (4) Listar todos
# os clientes, (5) Listar clientes preferenciais, (6) Terminar. Dependendo da opção
# escolhida, o programa deverá fazer o seguinte:

# Peça dados do cliente, crie um dicionário com os dados e adicione-o ao banco de dados.
# Peça o CPF do cliente e exclua seus dados do banco de dados.
# Peça o CPF do cliente e mostre seus dados.
# Mostrar lista de todos os clientes no banco de dados com seu CPF e nome.
# Mostre a lista de clientes preferenciais no banco de dados com seu CPF e nome.
# Termine o programa.



# Cadastro de clientes no banco de dados
banco_de_dados = {}

while True:
    print("""
(1) Adicionar cliente
(2) Remover cliente
(3) Mostrar cliente
(4) Listar todos os clientes
(5) Listar clientes preferenciais
(6) Terminar
""")

    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        # Adicionar cliente
        # Pedir os dados do cliente, criar um dicionario e adicionar ao banco de dados
        print('Inserindo os dados do novo cliente.')
        print('')
        cpf_novo = input('Informe o CPF: ')
        nome = input('Informe o nome: ')
        endereco = input(' Informe o endereço do cliente: ')
        telefone = input('Informe o telefone: ')
        email = input('Informe o email: ')

        # definindo se o cliente é preferencial
        preferencial_condicao = input("Cliente é preferencial? [S/N] ")
        if preferencial_condicao == 's' and 'S':
            preferencial = bool(True)
        else:
            preferencial = bool(False)


        dados = {cpf_novo:
                    {
                    'nome': nome,
                    'endereco': endereco, 
                    'telefone':telefone, 
                    'email':email, 
                    'preferencial':preferencial
                    }
                    }

        banco_de_dados.update(dados)
                    
        print('Cliente', nome, 'adicionado com sucesso!')

    elif opcao == 2:
        # Remover cliente
        # Pedir o CPF e excluir seus dados
        cpf_removido = input('Digite o CPF do cliente que você deseja remover:')
        print('')
        if cpf_removido in banco_de_dados:
            del banco_de_dados[cpf_removido]
            print('Cliente',cpf_removido, 'removido com sucesso!')
        else:
            print('Cliente inválido!CPF não cadastrado')

    elif opcao == 3:
        # Mostrar cliente
        # Pedir o CPF do cliente e mostrar os dados
        cpf_consultado = input('Digite o CPF que deseja consultar:')

        if cpf_consultado in banco_de_dados:
            print('Exibindo dados do cliente: ')
            print('')
            print('CPF: ', cpf_consultado)
            print('Nome: ', banco_de_dados[cpf_consultado]['nome'])
            print('Endereço: ', banco_de_dados[cpf_consultado]['endereco'])
            print('Telefone: ', banco_de_dados[cpf_consultado]['telefone'])
            print('Email: ', banco_de_dados[cpf_consultado]['email'])
            if banco_de_dados[cpf_consultado]['preferencial'] == True:
                print('Cliente preferencial: Sim')
            else:
                print('Cliente preferencial: Não')
           
        else:
            print('Este CPF não está cadastrado no sistema.')

    elif opcao == 4:
        # Listar todos os clientes
        # Mostrar lista de todos os clientes cadastrados com CPF e nome.
        print("Lista de todos os clientes:")
        for cpf in banco_de_dados:
            print('')
            print('CPF: ', cpf )
            print('Nome: ', banco_de_dados[cpf]['nome'])


    elif opcao == 5:
        # Listar clientes preferenciais
        # Mostrar lista clientes preferenciais cadastrados com CPF e nome.
        print("Clientes preferenciais:")
        for cpf in banco_de_dados:
            if banco_de_dados[cpf]['preferencial'] == True:
                print('')
                print('CPF: ', cpf)
                print('Nome: ', banco_de_dados[cpf]['nome'])
    
    elif opcao == 6:
        # Terminar
        # Terminar o programa
        print('Programa finalizado')
        break
    else:
        print('Opção inválida! Digite uma opção válida')
