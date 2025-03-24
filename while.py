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

print(produtos)