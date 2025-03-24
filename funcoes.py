lista_precos = [1500, 1000, 800, 2000]

total_imposto = 0

def calcular_imposto(preco): # entre parênteses está o parâmetro da função
    if preco > 1000:
        imposto = preco * 0.15 # as variáveis criadas dentro da função, só existe dentro da função
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