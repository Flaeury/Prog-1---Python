cadastros = []


def nome():
    while True:
        try:
            print('\n')
            nome = input('Digite o nome:\n')
            if nome.isnumeric():
                raise Exception("USE SOMENTE LETRAS")
        except Exception as e:
            print(e)
        else:
            return nome


def nascimento():
    while True:
        try:
            print('\n')
            nascimento = input('Digite sua data de nascimento (ddMMyyyy):\n')
            if not nascimento.isdigit():
                raise Exception("USE SOMENTE NÚMEROS")
            elif len(nascimento) != 8:
                raise Exception("VOCÊ INSERIU MAIS OU MENOS NÚMEROS")
        except Exception as e:
            print(e)
        else:
            return nascimento


def sexo():
    while True:
        try:
            print('\n')
            sexo = input('Digite seu sexo (F ou M):\n').upper()
            if sexo.isnumeric():
                raise Exception("USE SOMENTE LETRAS")
            if sexo != "F" and sexo != "M":
                raise Exception("UTILIZE F OU M")
        except Exception as e:
            print(e)
        else:
            return sexo


def cpf():
    while True:
        try:
            print('\n')
            cpf = input('Digite seu cpf (00011122233):\n')
            if not cpf.isdigit():
                raise Exception("USE SOMENTE NÚMEROS")
            elif len(cpf) != 11:
                raise Exception("VOCÊ INSERIU MAIS OU MENOS NÚMEROS")
        except Exception as e:
            print(e)
        else:
            return cpf


def rg():
    while True:
        try:
            print('\n')
            rg = input('Digite seu rg (0123456):\n')
            if not rg.isdigit():
                raise Exception("USE SOMENTE NÚMEROS")
            elif len(rg) != 7:
                raise Exception("VOCÊ INSERIU MAIS OU MENOS NÚMEROS")
        except Exception as e:
            print(e)
        else:
            return rg


def telefone():
    while True:
        try:
            print('\n')
            telefone = input('Digite seu telefone (91940028922):\n')
            if not telefone.isdigit():
                raise Exception("USE SOMENTE NÚMEROS")
            elif len(telefone) != 11:
                raise Exception("VOCÊ INSERIU MAIS OU MENOS NÚMEROS")
            elif telefone[:2] != '91':
                raise Exception(
                    "COLOQUE O DDD DO ESTADO DO PARÁ (INICIE COM 91)")
            elif telefone[2] != '9':
                raise Exception(
                    "NÃO ESQUEÇA DO 9 OBRIGATÓRIO EM TERRITÓRIO BRASILEIRO (EX: 009000-0000)")
        except Exception as e:
            print(e)
        else:
            return telefone


def cadastrar():
    campo_nome = nome()
    campo_nascimento = nascimento()
    campo_sexo = sexo()
    campo_cpf = cpf()
    campo_rg = rg()
    campo_telefone = telefone()

    cadastros.append({'nome': campo_nome,
                      'nascimento': campo_nascimento,
                      'sexo': campo_sexo,
                      'cpf': campo_cpf,
                      'rg': campo_rg,
                      'telefone': campo_telefone
                      })


def listar_cadastros():
    for item in cadastros:
        print("----------------------------")
        print('Nome:', item['nome'])
        print('Nascimento:', item['nascimento'])
        print('Sexo:', item['sexo'])
        print('CPF:', item['cpf'])
        print('RG:', item['rg'])
        print('Telefone:', item['telefone'])
        print("----------------------------")
        print()


def menu():
    print("--------------------")
    print('Escolha um opção')
    print('1- Listar cadastros')
    print('2- Cadastrar')
    print('3- Sair')
    print("--------------------")
    return input()


def programa():
    opcao = menu()

    while opcao != '3':
        if opcao == '1':
            listar_cadastros()
        elif opcao == '2':
            cadastrar()
        else:
            print('Opção inválida!')
        opcao = menu()


programa()
