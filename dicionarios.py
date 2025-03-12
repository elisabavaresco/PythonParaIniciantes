precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# o que é um dicionário: é um conjunto de elementos, em que cada item é um conjunto de chave e valor
# o valor da chave pode ser número, lista, textos...
# para criar um dicionário, é preciso cololar "{}":
dic_precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 20000}

# para pegar um item do dicionário, ao invés de passar o índice você vai passar a chave do dicionário:
preco_celular = dic_precos["celular"]
print(preco_celular)

dic_precos["celular"] = 2000 # para editar/modificar um intem dentro do dicionario
dic_precos["iphone"] = 4500 # para adicionar um intem ao dicionario (se ele não existir, será adicionado, se existir, será editado)
dic_precos.pop("camera") # para deletar um item do dicionario
len(dic_precos) # para saber quantos itens tem dentro do dicionário
"televisão" in dic_precos # para verificar se um item existe dentro do dicionário, OBS: ele sempre vai buscar o item nas chaves do dicionário, não nos valores
1500 in dic_precos.values() # para verificar/ buscar pelo valor de uma chave dentro do dicionário
dic_precos.keys() # para pegar a lista de chaves do dicionário
dic_precos.values() # para pegar a lista de valores do dicionário

# Exercicio de consulta de preço

produto_buscado = input("Digite aqui o produto que gostaria de consultar: ")
produto_buscado = produto_buscado.lower()

if produto_buscado in dic_precos:
        preco_buscado = dic_precos[produto_buscado]
        print(f"O preço do produto buscado é R$ {preco_buscado}")
else:
        print("Produto não cadastrado")
print ("Fim")