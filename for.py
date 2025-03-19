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

total_imposto = 0 # acumulado
for preco in lista_precos:
    if preco <= 1000:
        imposto = preco * 0.1
    else:
        imposto = preco * 0.15
    print(f"Preco: {preco}, Imposto: {imposto}")
    total_imposto = total_imposto + imposto
print(f"O total de imposto é: {total_imposto}")