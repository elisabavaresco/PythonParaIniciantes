lista_precos = [1500, 1000, 800, 2000]

total_imposto = 0

for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f"Preco: {preco}, Imposto: {imposto}")
    total_imposto = total_imposto + imposto

print(total_imposto)

def se_inscrever(): # definindo/ criando funções
    print("Se inscreve no canal")