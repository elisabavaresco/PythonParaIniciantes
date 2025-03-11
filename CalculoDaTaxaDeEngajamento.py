seguidores = int(input("Número de seguidores: "))
likes = int(input("Número de likes: "))
comentarios = int(input("Número de comentários: "))

engajamento = ((likes + comentarios)/seguidores)

if engajamento <= 0.01:
    print(f"A taxa de engajamento é {engajamento:.2%}, o que é abaixo da média")

if engajamento > 0.01 and engajamento < 0.05:
    print(f"A taxa de engajamento é {engajamento:.2%}, o que é dentro da média")

if engajamento >= 0.05:
    print(f"A taxa de engajamento é {engajamento:.2%}, o que é acima da média")

print("Fim")