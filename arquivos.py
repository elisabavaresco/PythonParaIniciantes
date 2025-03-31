# como ler arquivos num geral (txt, csv, etc)

arquivo = open("vendas.txt", "r") # isso no caso quando o arquivo já está no 'código', se ele estiver em outro local do computador, é preciso colocar o endereço/caminho completo.
# ao abrir um arquivo, você tem duas opção: modo de leitura ou no modo de escrita
# quando adicionamos o "w" ali encima, dizemos que queremos abri-lo no modo de escrita, onde podemos editar o arquivo
# quando adicionamos o "r" ali encima, dizemos que queremos abri-lo no modo leitura

# depois de abrir o arquivo, podemos fazer oque quisermos com ele, porém no final é obrigatório fechá-lo, se não ele fica eternamente aberto:
arquivo.close()

# outra forma de abrir e fechar um arquivo é utilizar a estrutura de 'with':

with open("vendas.txt", "r") as arquivo: # criei a variável 'arquivo'
    # e vai fazer aqui dentro o que quiser com o arquivo, depois ele automaticamente vai fechar esse arquivo
    # infos = arquivo.read() # isso aqui é uma string, o .read() vai te retornar como um texto tudo junto
    infos = arquivo.readlines() # vai te retornar uma lista, em que cada item da lista é uma linha

# para calcular o total de vendas das infos trazidas pelo arquivo:

vendas_totais = 0 
for item in infos:
    item = item.replace("\n", "")
    item = item.replace(" ", "")
    resultado = item.split(",") # vai separar o 'texto' pela virgula e vai entregar uma lista dos itens separados
    valor = resultado[1] # esse cara aqui ainda está em formato de texto
    valor = float(valor) # transformando o texto em número
    vendas_totais = vendas_totais + valor
print (vendas_totais)