# tabuada de um numero com inicio e fim definidos pelo usuario
# ex: usuario digita 5, inicio 1 e fim 10
# o programa imprime a tabuada de 5 de 1 a 10

numero = int(input("Digite um numero para ver sua tabuada: "))
inicio_da_tabuada = int(input("Digite o inicio da tabuada: "))
fim_da_tabuada = int(input("Digite o fim da tabuada: "))

while inicio_da_tabuada <= fim_da_tabuada:
    print(numero * inicio_da_tabuada)
    inicio_da_tabuada = inicio_da_tabuada + 1

# =========================================================================================

# Ler dois numeros fornecidos pelo usuario e imprimir o resultado da multiplicacao do primeiro numero pelo segundo numero
# utilizando apenas somas e subtrações para calcular o resultado
# ex: usuario digita 4 e 3
# o programa imprime 12 (4 + 4 + 4)
# ou seja, 4 somado 3 vezes 

numero1 = int(input("Digite o primeiro numero : "))
numero2 = int(input("Digite o segundo numero : "))
resultado = 0
contador = 0
while contador < numero2:
    resultado = resultado + numero1
    contador = contador + 1
print("O resultado da multiplicacao de", numero1, "por", numero2, "é:", resultado)

# =========================================================================================

# Ler dois numeros fornecidos pelo usuario e imprimir a divisao inteira do primeiro numero pelo segundo numero
# utilizando apenas soma e subtrações para calcular o resultado
# ex: usuario digita 10 e 2
# o programa imprime 5 (2 + 2 + 2 + 2 + 2 = 10)
# ou seja, quantas vezes o segundo numero cabe no primeiro numero

numero1 = int(input("Digite o primeiro numero (dividendo): "))
numero2 = int(input("Digite o segundo numero (divisor): "))
if numero2 == 0:
    print("Divisao por zero nao e permitida.")
else:
    quociente = 0
    soma = numero2
    while soma <= numero1:
        soma += numero2
        quociente += 1
    print("O resultado da divisao inteira de", numero1, "por", numero2, "é:", quociente)  

# =========================================================================================

# Ler dois numeros fornecidos pelo usuario e imprimir a divisao inteira do primeiro numero pelo segundo numero
# utilizando apenas subtrações para calcular o resultado
# ex: usuario digita 10 e 2
# o programa imprime 5 (10 - 2 - 2 - 2 - 2 - 2 = 0)
# ou seja, quantas vezes o segundo numero cabe no primeiro numero

numero1 = int(input("Digite o primeiro numero (dividendo): "))
numero2 = int(input("Digite o segundo numero (divisor): "))
if numero2 == 0:
    print("Divisao por zero nao e permitida.")
else:
    quociente = 0
    restante = numero1
    while restante >= numero2:
        restante -= numero2
        quociente += 1
    print("O resultado da divisao inteira de", numero1, "por", numero2, "é:", quociente)   
