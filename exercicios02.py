# Exercíco desafio
# Criar um sistema de consulta de preço

precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# quero que o usuário me dê um input e o meu sistema diga qual o preço do produto
# se o produto não existir, o programa precisa dizer pro usuário que esse produto não existe

produto_buscado = input("Digite aqui o produto que gostaria de consultar: ")
produto_buscado = produto_buscado.lower()

if produto_buscado in produtos:
        encontrar_preco = produtos.index(produto_buscado)
        print(f"O preço do produto buscado é R$ {precos[encontrar_preco]}")
else:
        print("Produto não cadastrado")
        print(f"Escolha um dos produtos cadastrados: {produtos}")
print ("Fim")