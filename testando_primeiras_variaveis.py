# numero inteiro -> int
# numero decimal -> float
# texto -> string
# boolean -> true or false

faturamento = 1200 
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1 
imposto = taxa_imposto * faturamento

print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)