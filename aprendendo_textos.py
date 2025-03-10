faturamento = 1000
custo = 700

lucro = faturamento - custo

# Operações de texto
# 1a froma de colocar fatores dinâmicos dentro de um texto:
print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")
# 2a froma de colocar fatores dinâmicos dentro de um texto:
print("Faturamento:" + str(faturamento) + ", Custo:" + str(custo) + ", Lucro:" + str(lucro))

# letras maíusculas e minúsculas são coisas diferentes em Python, uma forma de padronizar essa variável string 
# é atribuindo a ela a funçao de texto 'lower'
email = "EMAIL_falso@gmail.com"

print (email.lower())

# é possível buscar por caracteres específicos dentro de uma string, usando a funçao 'find'

print (email.find("@"))

# ao rodar o programa, ele devolve a resposta "11" pro print acima, isso ocorre pois quando se tem um texto, automaticamente, o python atribui
# um índice para cada caracter do seu texto, no exemplo acima, a letra "E" é o indice 0, a letra "L" é o indice 5, e o "@" é o indice 11.
# E se não existisse o "@"? Ele devolveria a resposta "-1". A função 'find' traz a resposta -1 se não encontrar o elemento.

# Para descobrir o que está na posição '11' fazemos o seguinte:

print(email[11])

# Para pegar um pedaço de texto desejado:
# Exemplo de tudo que vem depois do '@':
posicao = email.find("@")
servidor = email[posicao:] # para pegar de um índice até o final, deve ser adicionar o ':', então, ex: [11:], [posicao:]
print(servidor)

# Exemplo de tudo que vem antes do '@':
nome_email = email[:posicao]
print(nome_email)

# Exemplo de pegar o servidor mas nem incluir o '@'
servidor_sem_arroba = email[posicao+1:]
print(servidor_sem_arroba)

# Como pegar o tamanho de um texto
tamanho = len(email)
print(tamanho)

# Como trocar um pedaço do texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print (email_trocado)