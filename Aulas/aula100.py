import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.0},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos) 

for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.10, 2)  #
    print(produto['nome'], produto['preco'])  

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'])
print(*produtos_ordenados_por_nome, sep='\n')

print('-' * 20)

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])
print(*produtos_ordenados_por_preco, sep='\n')