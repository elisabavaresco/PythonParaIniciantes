# aprendendo estruturas de repetição

for i in range(10): # para executar algo X vezes
    print("Se inscreva")

lista_precos = [1500, 100, 800, 2000]
imposto = 0.1

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
