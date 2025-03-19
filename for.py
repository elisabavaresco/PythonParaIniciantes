# aprendendo estruturas de repetição

for i in range(10): # para executar algo X vezes
    print("Se inscreva")

lista_precos = [1500, 1000, 800, 2000]

for preco in lista_precos: #vai permitir percorrer uma lista e executar algo para cada item até ela acabar
    imposto = preco * 0.1
    print(f"Preco: {preco}, Imposto: {imposto}")

# exercicio 1
# regra do imposto:
# preco até 1000 -> imposto é de 10%%

for preco in lista_precos:
    if preco <= 1000:
        imposto = preco * 0.1
    else:
        imposto = preco * 0.15
    print(f"Preco: {preco}, Imposto: {imposto}")

# exercio 2
# calcular o total de imposto 

# criando acumulados

total_imposto = 0 # acumulado
for preco in lista_precos:
    if preco <= 1000:
        imposto = preco * 0.1
    else:
        imposto = preco * 0.15
    print(f"Preco: {preco}, Imposto: {imposto}")
    total_imposto = total_imposto + imposto
print(f"O total de imposto é: {total_imposto}")


# exercio 3 - desafio

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

# 3.1 saber quanto variou percentualmente cada mes de 2023 em comparacao com 2022

vari_percentual = ((vendas_23["jan"] - vendas_22["jan"])/vendas_22["jan"]) * 100
print(vari_percentual)

venda_22 = vendas_22.values()

# for venda_23 in vendas_23:

# 3.2 simule: se a empresa tivesse pelo menos empatado com 2022 nos meses que ela vendeu menos, qual teria sido o faturamento de 2023
