# with open('arquivo.txt', 'r', encoding="utf-8") as f:
#    conteudo = f.read()
# print(conteudo)


# with open('arquivo.txt', 'r', encoding="utf-8") as f:
#    lista = [linha for linha in f]
#    print(lista)

# with open('arquivo.txt', encoding="utf-8") as f:
#    linha1 = f.readline()
#    print(linha1)
#    linha2 = f.readline()
#    print(linha2)
#    linha3 = f.readline()
#    print(linha3)

# with open('arquivo.txt', 'w', encoding="utf-8") as f:
#    f.write("Olá mundinho \n")
#    f.write("Final")

with open('arquivo.txt', 'a', encoding="utf-8") as f:
    f.write('\n')
    f.write('Estou na UFPA')
