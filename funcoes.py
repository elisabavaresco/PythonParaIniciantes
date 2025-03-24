lista_precos = [1500, 1000, 800, 3000]

total_imposto = 0

def calcular_imposto(preco): # entre parênteses está o parâmetro da função
    if preco > 2000:
        imposto = preco * 0.2 # as variáveis criadas dentro da função, só existe dentro da função
    elif preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f"Preco: {preco}, Imposto: {imposto}")
    return imposto # para uma variável existir fora de uma função, é preciso "retornar" a variável

for preco in lista_precos:
    imposto = calcular_imposto(preco)
    total_imposto = total_imposto + imposto

print(total_imposto)

def se_inscrever(): # definindo/ criando funções
    print("Se inscreve no canal")

# adicionando parâmetros

lista_precos = [1500, 1000, 800, 3000]

total_imposto = 0

def calcular_imposto(preco, aliquota1, aliquota2, aliquota3): # é possível solicitar mais de um parâmetro
    if preco > 2000:
        imposto = preco * aliquota1 
    elif preco > 1000:
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
    print(f"Preco: {preco}, Imposto: {imposto}")
    return imposto 

for preco in lista_precos:
    imposto = calcular_imposto(preco, 0.2, 0.15, 0.1)
    total_imposto = total_imposto + imposto

print(total_imposto)

# definindo valores padrões para os parâmetros 

lista_precos = [1500, 1000, 800, 3000]

total_imposto = 0

def calcular_imposto(preco, aliquota1=0.2, aliquota2=0.15, aliquota3=0.1): # é possível definir valores padrões para os parâmetros de uma função
    if preco > 2000:
        imposto = preco * aliquota1 
    elif preco > 1000:
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
    print(f"Preco: {preco}, Imposto: {imposto}")
    return imposto 

for preco in lista_precos:
    imposto = calcular_imposto(preco) # se for usar só o padrão dos parâmetros, não é preciso informar o valor deles ao chamar a função, ou, se quiser alterar, basta seguir o exemplo a baixo:
#   imposto = calcular_imposto(preco, aliquita1=0.25)
    total_imposto = total_imposto + imposto

print(total_imposto)