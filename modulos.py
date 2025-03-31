# o python tem varias bibliotecas que permitem que você execute tarefas de forma eficiente

# vamos aprender sobre as bibliotecas os e requests

import os # essa biblioteca permite que a gente acesse as coisas do nosso computador

arquivos = os.listdir() # para listar tudo que está no diretório

# os.rename("vendas.txt", "arquivos/vendas.txt") # para mudar um arquivo de lugar

# automação para organizar os arquivos com final 22 pra pasta 22 e os com final 23 pra pasta 23

lista_arquivos = os.listdir("arquivos")

for nome_arquivo in lista_arquivos:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")
