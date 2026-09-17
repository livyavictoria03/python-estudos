produtos = [
    {'nome': 'p1', 'preco': 25},
    {'nome': 'p2', 'preco': 15},
    {'nome': 'p3', 'preco': 40},
    {'nome': 'p4', 'preco': 10},
]

produtos_caros = [produto for produto in produtos if produto['preco'] > 20]
print(produtos_caros)
