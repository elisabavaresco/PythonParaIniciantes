nome = input("Digite aqui o seu nome: ")
email = input("Digite aqui o seu email: ")

# Descobrindo o servidor do email

posicao_arroba = email.find("@")
servidor = email[posicao_arroba + 1:]
print(servidor)

# Pegando o 1º nome do usuário

achando_primeiro_nome = nome.find(" ")
primeiro_nome = nome[:achando_primeiro_nome]
print(primeiro_nome)

# Construindo a mensagem: Usuário X cadastrado com sucesso com o email Y

print(f"Usuário {primeiro_nome} cadastrado com sucesso com o email {email}")

# Construindo a mensagem: Enviamos um link de confirmação para o email j******@gmail.com

numero_caracteres = len(email[1:posicao_arroba])
email_oculto = email.replace(email[1:posicao_arroba],"*" * numero_caracteres)
print(f"Enviamos um link de confirmação para o email {email_oculto}")