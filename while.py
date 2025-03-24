# while -> loops infinitos

contador = 0
while contador < 3:
    print("Se inscreva no canal")
    contador = contador + 1 # é preciso explicitar quando o contador aumenta, se nao irá fazer um loop infinito


produtos = ["iphone", "ipad", "airpod"]

while True: # para que o loop aconteça enquanto X for verdade
    novo_produto = input("Digite aqui o produto: ")
    novo_produto = novo_produto.lower() 

    if "sair" == novo_produto: # condição para que o loop infinito pare
        break

    if novo_produto in produtos:
        print("Produto já cadastrado")
    else:
        print(f"Produto {novo_produto} cadastrado com sucesso")
        produtos.append(novo_produto) 

print(produtos) # esse só vai acontecer depois que todo o loop do while terminar


# Criando um sistema de consulta de preço com While

precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

while True:
    produto_buscado = input("Digite aqui o produto que gostaria de consultar: ")
    produto_buscado = produto_buscado.lower()

    if produto_buscado in produtos:
            encontrar_preco = produtos.index(produto_buscado)
            print(f"O preço do produto buscado é R$ {precos[encontrar_preco]}")
            break
    elif "sair" == produto_buscado:
         break       
    else:
            print("Produto não cadastrado")
            print(f"Escolha um dos produtos cadastrados: {produtos}")

print("Fim")