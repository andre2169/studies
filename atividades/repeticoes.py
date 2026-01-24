
# Contagem de 0 a 100

x = 0
while x <= 100:
    print(x)
    x += 1


# =========================================================================================

# Contagem regressiva

y = 10
while y > 0:
    print(y)
    y -= 1
print("Fogo!")

# =========================================================================================

# imprimir de 1 até N

fim = int(input("Digite o ultimo numero a imprimir: "))
x = 1
while x <= fim:
    print(x)
    x = x + 1

# =========================================================================================

# imprimir so os pares

fim = int(input("Digite até onde quer imprimir para descobrir os numeros pares(ex: 0 a N): "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

# =========================================================================================

# imprimir so os impares

fim = int(input("Digite até onde quer imprimir para descobrir os numeros impares(ex: 0 a N): "))
x = 0
while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1

# =========================================================================================

# imprimir os 10 primeiros numeros multiplos de 3
# ex: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
x = 1
contador = 0
while contador < 10:
    if x % 3 == 0:
        print(x)
        contador += 1
    x += 1  
  
# =========================================================================================

# imprimir os 10 primeiros numeros multiplos de um numero fornecido pelo usuario
# ex: usuario digita 7, o programa imprime os 10 primeiros multiplos de 7
# ex: 7, 14, 21, 28, 35, 42, 49, 56, 63, 70

num = int(input("Digite um numero para descobrir os 10 primeiros multiplos: "))
x = 1
contador = 0
while contador < 10:
    if x % num == 0:
        print(x)
        contador += 1
    x += 1

# =========================================================================================
