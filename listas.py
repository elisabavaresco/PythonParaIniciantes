# listas sempre ficam entre '[]' e os itens separados por ','
vendas = [100, 50, 130, 80, 120, 200] # lista de números
produtos = ["iphone", "ipad", "airpod"] # lista de strings

print(vendas[0]) # para pegar um item da lista de uma posição específica
print(vendas[-1]) # para pegar o último item da lista, independente do tamanho dela
print(vendas[-2]) # para pegar o penúltimo item da lista, independente do tamanho dela
print(vendas[-3]) # para pegar o antipenúltimo item da lista, independente do tamanho dela
print(vendas[:2]) # para pegar até o índice X, sem contar o índice X
print(vendas[2:]) # para pegar o índice X até o final da lista, contando o índice X

total_vendas = sum(vendas) # para somar todos os valores de uma lista de núemros
quantidade = len(vendas) # para saber quantos itens tem dentro de uma lista
valor_max =  max(vendas) # para saber qual o valor mais alto dentro da lista de números
valor_min = min(vendas) # para saber qual o valor mais baixo dentro da lista de números
posicao = vendas.index(130) # para descobrir a posição de um elemento dentro da lista

print("iphone" in produtos) # 'in' para verificar ser determinado valor faz parte de uma lista, boleano (true or false)

# exemplo de uso do 'in' com input do usuário
# produto_usuario = input("Digite o nome de um produto: ")
# print(produto_usuario in produtos)

precos_produtos = [4000, 8000, 2000]
precos_produtos[0] = 4500 # para editar um iten dentro de uma lista
precos_produtos[0] = precos_produtos[0] * 1.1 # para aumentar um valor em X% ou qualquer outra conta matemática

# para adicionar novos itens à lista
produtos.append("macbook")
precos_produtos.append(10000)

# para remover itens da lista
produtos.remove("iphone") # para remover de acordo com o valor do item
precos_produtos.pop(0) # para remover um item de acordo com a posição dele na lista

# para inserir um valor em uma posição/índice específica dentro da lista
produtos.insert(1, "airpod")

# para contar valores
print(produtos.count("airpod"))
