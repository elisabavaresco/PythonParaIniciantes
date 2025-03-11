# aprendendo a construir a estrutura do if

# faturamento = 1000
# custo = 8100

# lucro = faturamento - custo

# if  lucro >= 0: # if + condição
#     # aqui você vai escrever tudo que quer que aconteça se a condição for VERDADEIRA
#     print(lucro)
# else: 
#     # aqui você coloca tudo que você quer que aconteça se a condição for FALSA
#     print("Prejuízo", lucro)
# != 'diferente de'
# > 'maior que'
# < 'menor que'
# >= 'maior ou igual a'
# <= 'menor ou igual a'
# == 'igual a'

# produtos = ["iphone", "ipad", "airpod"]
# novo_produto = input("Digite aqui o produto: ")
# novo_produto = novo_produto.lower() # tratamento do input do usuário

# if novo_produto in produtos:
#     print("Produto já cadastrado")
# else:
#     print("Produto cadastrado com sucesso")
#     produtos.append(novo_produto) # adicioando o novo produto à lista de produtos

# print(produtos)

# Segundo exemplo - faixas
# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus

# opção 1
vendas = 9000

if vendas > 15000:
    bonus = 500
elif vendas > 10000: # 'elif' é um "caso contrário, se..."
    bonus = 150
elif vendas > 5000:
    bonus = 50
else:
    bonus = 0

print(bonus)

# opção 2
if vendas > 5000:
    if vendas > 10000:
        if vendas > 15000:
            bonus = 500
        else:
            bonus = 150
    else: 
        bonus = 50
else:
    bonus = 0

print(bonus)

# Terceiro exemplo - duas condições
# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus
# vendas da empresa > 50000

# opção 1
vendas = 17000
vendas_empresa = 60000
meta_empresa = 50000

if vendas > 15000 and vendas_empresa > meta_empresa:
    bonus = 500
elif vendas > 10000 and vendas_empresa > meta_empresa: 
    bonus = 150
elif vendas > 5000 and vendas_empresa > meta_empresa:
    bonus = 50
else:
    bonus = 0

print(bonus)

# opção 2

if not vendas_empresa > meta_empresa:
    bonus = 0
else:
    if vendas > 15000 and vendas_empresa > meta_empresa:
        bonus = 500
    elif vendas > 10000 and vendas_empresa > meta_empresa: 
        bonus = 150
    elif vendas > 5000 and vendas_empresa > meta_empresa:
        bonus = 50
    else:
        bonus = 0

print(bonus)