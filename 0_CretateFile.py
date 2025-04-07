import os
import requests

aula = 101  # Número da aula que você deseja baixar

nome_arquivo = f"aula{aula}.py"
link_github = f"https://github.com/luizomf/cursopython2023/blob/main/{nome_arquivo}"

# Transforma o link visual do GitHub em um link "raw" (conteúdo puro)
link_raw = f"https://raw.githubusercontent.com/luizomf/cursopython2023/main/{nome_arquivo}"

# Faz o download do conteúdo da aula
resposta = requests.get(link_raw)
print(resposta)

# Cria o arquivo local
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(f"# {link_github}\n\n")
    if resposta.status_code == 200:
        arquivo.write(resposta.text)
        print(f"{nome_arquivo} criado com sucesso com o conteúdo da aula!")
    else:
        arquivo.write("# Erro ao baixar o conteúdo da aula.\n")
        print(f"Não foi possível baixar o conteúdo. Código de status: {resposta.status_code}")
