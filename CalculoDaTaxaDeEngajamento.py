seguidores = int(input("Número de seguidores: "))
likes = int(input("Número de likes: "))
comentarios = int(input("Número de comentários: "))

engajamento = ((likes + comentarios)/seguidores)
   
print(f"A sua taxa de engajamento é: {engajamento:.1%}")