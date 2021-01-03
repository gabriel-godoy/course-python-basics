#!python3

# for i in range(10):
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(0, 100, 10):  # De 1 a cem, pulando de 10 em 10
#     print(i)

# nums = [2, 4, 6, 8]

# for n in nums:
#     print(n, end=' ')


produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

# for chave in produto:
#     print(chave, '==>', produto[chave])

# for chave, valor in produto.items():
#     print(chave, '==>', valor)

for valor in produto.values():
    print(valor, end=' | ')
