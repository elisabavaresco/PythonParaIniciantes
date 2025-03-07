# Desenvolva um um algoritmo capaz de imprimir na tela “Hello World”
print ("Hello World")

# Desenvolva um algoritmo que seja capaz de receber um valor de X pela função LEIA e calcular o valor e imprimir na tela o valor de Y
# para função de segundo grau: y = x**2 + x*2 + 16 (Lembre-se: ** indica exponencial)
x = int(input("Qual o valor de X?"))
y = x ** 2 + x * 2 + 16
print ("O valor de Y é", y)

# Para finalizar, desenvolva um algoritmo que receba (usando a função leia) 2 números e retorne o resto da divisão desses dois números na tela.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resto = num1 % num2
print ("O resto é: ", resto)