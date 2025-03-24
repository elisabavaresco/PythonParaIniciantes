vendedores = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

# Calcule o Bônus de cada um dos vendedores:
# a cada venda o vendedor ganha R$2 e 1% do valor de venda
# calcular o valor total de bonus pago e o bonus de cada vendedor

comissao_total = 0
for vendedor in vendedores:
    comissao_vendedor = (len(vendedores[vendedor]) * 2) + (sum(vendedores[vendedor]) * 0.01)
    print(f"O bônus recebido pelo(a) {vendedor} foi de R${comissao_vendedor}")
    comissao_total = comissao_total + comissao_vendedor
print(f"O bonus total pago foi R${comissao_total}")