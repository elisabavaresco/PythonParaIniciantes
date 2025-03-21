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

for mes in vendas_23.keys(): # estou declarando que a variável 'mes' é referente à chave do dicionário
    vari_percentual = (vendas_23[mes] - vendas_22[mes]) / vendas_22[mes]
    print(f"{mes}: {vari_percentual:.2%}")

# resolução professor
for mes_p in vendas_23:
    valor_22 = vendas_22[mes_p]
    valor_23 = vendas_23[mes_p]
    vari_percentual = valor_23 / valor_22 - 1
    print(f"Variação do {mes_p}: {vari_percentual:.1%}")

# 3.2 simule: se a empresa tivesse pelo menos empatado com 2022 nos meses que ela vendeu menos, qual teria sido o faturamento de 2023

total_vendas = 0
for mes in vendas_23.keys():
    if vendas_23[mes] < vendas_22[mes]:
        valor_venda = vendas_22[mes]
    else:
        valor_venda = vendas_23[mes]
    total_vendas = total_vendas + valor_venda

print(f"O total de vendas em 2023 foi R$ {total_vendas}")

# resolucao professor

faturamento_total_simulado = 0
for mes_p in vendas_23:
    valor_22 = vendas_22[mes_p]
    valor_23 = vendas_23[mes_p]
    vari_percentual = valor_23 / valor_22 - 1
    if vari_percentual < 0:
        faturamento_total_simulado = faturamento_total_simulado + valor_22
    else: 
        faturamento_total_simulado = faturamento_total_simulado + valor_23
print(faturamento_total_simulado)

# ou

for mes_p in vendas_23:
    valor_22 = vendas_22[mes_p]
    valor_23 = vendas_23[mes_p]
    vari_percentual = valor_23 / valor_22 - 1
    if vari_percentual < 0:
        vendas_23[mes_p] = valor_22
faturamento_total = sum(vendas_23.values())
print(faturamento_total)