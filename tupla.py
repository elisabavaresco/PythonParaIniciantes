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
print(resposta[0]) # você consegue dessa forma 'pegar' um único valor dentro de uma tupla, assim como nas listas

# unpacking uma tupla

resposta = calcular_imposto2(1000) # (275.0, 35.0, 50.0
ir, csll, iss = resposta # ao fazer isso, como a resposta é uma tupla, 
# ele automaticamente vai atribuir o primeiro valor da tupla (275) pra primeira variável (ir), 
# assim por diante, criando 3 variáveis de uma vez só
print(ir, csll, iss, sep="\n") # o sep="\n" é para separar os valores com um enter

# refatorando
ir, csll, iss = calcular_imposto2(1000)
print(ir, csll, iss, sep="\n")

# também podemos criar tuplas para variáveis nas quais os valores são fixos, exemplo:
tamanho_tela = (1920, 1080)