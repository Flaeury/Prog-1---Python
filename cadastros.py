import re


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


def email():
    while True:
        try:
            print('\n')
            email = input('Digite seu email (email@email.com):\n')
            if len(re.findall("[@.]", email)) < 2:
                raise Exception(
                    "COLOQUE SEU EMAIL CORRETAMENTE (EX: email@email.com)")
        except Exception as e:
            print(e)
        else:
            return email


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
    campo_email = email()
    campo_telefone = telefone()

    with open('BD_CADASTRO.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(f"Nome:, {campo_nome}")
        f.write('\n')
        f.write(f"Email:, {campo_email}")
        f.write('\n')
        f.write(f"Telefone:, {campo_telefone}")
        f.write('\n')
        f.write('------------------------')
        f.write('\n')


def listar_cadastros():
    with open('BD_CADASTRO.txt', 'r', encoding="utf-8") as f:
        conteudo = f.read()
    print(conteudo)


def menu():
    print("--------------------")
    print('Escolha um opção')
    print('1- Listar cadastros')
    print('2- Cadastrar')
    print('3- Buscar por nome')
    print('Qualquer Tecla para Sair')
    print("--------------------")
    return input()


def buscar_por_nome():
    while True:
        inicial = input("Busque por uma inicial: ")
        with open('BD_CADASTRO.txt', 'r', encoding="utf-8") as f:
            conteudo_nomes = [line.split(
                ", ")[1][:-1] for line in f.readlines() if line.startswith(f"Nome:, {inicial}")]
            print('\n'.join(conteudo_nomes))
        return inicial


def programa():
    opcao = menu()

    while opcao != '4':
        if opcao == '1':
            listar_cadastros()
        elif opcao == '2':
            cadastrar()
        elif opcao == '3':
            buscar_por_nome()
        else:
            break
        opcao = menu()


programa()
