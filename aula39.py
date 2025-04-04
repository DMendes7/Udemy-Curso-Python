'''https://github.com/luizomf/cursopython2023/blob/main/aula39.py'''

nome = input("Digite um nome: ")
print(nome)
novo_nome = ''
i = 0
while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1
print(novo_nome)