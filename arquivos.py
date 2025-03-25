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
    