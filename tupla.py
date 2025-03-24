def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss 
# quando uma função retorna mais de um valor como resposta, ela por padrão, retorna uma tupla python como resposta:
# (275.0, 35.0, 50.0)
# uma tupla nada mais é do que uma lista de informações, só que ela vem entre parenteses 
# uma tupla é imutável

resposta = calcular_imposto2(1000)
print(resposta)
print(resposta[0])