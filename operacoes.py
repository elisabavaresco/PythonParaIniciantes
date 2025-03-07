# é possível colocar '_' para facilitar a visualização de números muito grandes, é uma edição visual
faturamento = 53_429_462_523
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas # somar
imposto = faturamento * 0.1 # multiplicar
lucro = faturamento - custo - imposto # subtrair

print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento # dividir
print(margem_lucro)

restituicao = imposto * 0.1
print (restituicao)

# Mod(%) resto da divisão
print (10 % 3)
tempo_em_meses = 160

# para razer somente a parte inteira do número usar 'int', como no exemplo a baixo
tempo_em_anos = int(tempo_em_meses / 12)
print (tempo_em_anos, "anos e", (tempo_em_meses % 12), "meses")

# arredondamento de números
numero = 123.57
print(round(numero))