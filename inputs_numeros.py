# 1 exemplo

vendas = input("Digite suas vendas do dia: ")
vendas = float(vendas)

# ou
# vendas = float(input("Digite suas vendas do dia: "))

bonus = vendas * 0.01
print(bonus)

# 2 exemplo
vendas_dia1 = float(input("Vendas Dia 1: "))
vendas_dia2 = float(input("Vendas Dia 2: "))

print(f"Total de Vendas: {vendas_dia1 + vendas_dia2}")

# ou, colocar o float/int no print e nao da declaração da variável
# print(f"Total de Vendas: {float(vendas_dia1) + float(vendas_dia2)}")