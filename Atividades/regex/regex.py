import re

arquivo_leitura = 'Atividades/regex/arquivo.txt'

# arquivo_armazenamento = 'Atividades/regex/palavras.txt'
# def salvar_palavras(arquivo_leitura, arquivo_armazenamento):
#     with open(arquivo_leitura, 'r', encoding="utf-8") as f:
#         palavras_selecionadas = re.findall(
#             r'\b[aeiouAEIOU][a-zA-Z]*[aeiouAEIOU]\b', f.read())
#         with open(arquivo_armazenamento, 'w', encoding="utf-8") as f2:
#             for palavras in palavras_selecionadas:
#                 f2.write(f"{palavras}\n")
#         print(
#             f"Palavras salvas no arquivo '{arquivo_armazenamento}': {palavras_selecionadas}")
# salvar_palavras(arquivo_leitura, arquivo_armazenamento)

# novo_arquivo = 'Atividades/regex/novo_arquivo.txt'
# def remover_acentos(arquivo_leitura, novo_arquivo):
#     with open(arquivo_leitura, 'r', encoding="utf-8") as f:
#         texto_original = f.read()
#         palavras_com_acentos = re.findall(
#             r'\b\w*[áàâãéèêíìîóòôõúùûç´`^~]\w*\b', texto_original)
#         with open(novo_arquivo, 'w', encoding="utf-8") as f2:
#             f2.write(f"{palavras_com_acentos}\n")
#         with open(novo_arquivo, 'r', encoding="utf-8") as f:
#             texto_sem_acentos = re.sub(
#                 r'[áàâãéèêíìîóòôõúùûç´`^~]', ' ', f.read())
#         print(f"Palavras com acentos e 'ç': {palavras_com_acentos}")
#         print(f"Palavra final (sem acentos): {texto_sem_acentos}")
# remover_acentos(arquivo_leitura, novo_arquivo)
