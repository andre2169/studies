# ler o salário de uma pessoa e calcular o imposto de renda conforme a tabela progressiva
salario = float(input("Digite o salário para calcular o imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = (imposto + (base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = (imposto + (base - 1000) * 0.20)
    print(f"Salario: R$ {salario:6.2f} Imposto a pagar: R$ {imposto:6.2f}")

#============================================================================================================================================

# ler o salário de um funcionário e calcular o novo salário com aumento de 10% para salários acima de R$ 1.250,00 e 15% para salários iguais ou inferiores a R$ 1.250,00
salario = float(input("Digite o seu salário: "))
base = 1.250
aumento = 10
aumento_de_inferiores = 15
if salario <= base:
    salario = salario + (salario * aumento_de_inferiores / 100)
else:
    salario = salario + (salario * aumento / 100)

#============================================================================================================================================

# ler dois números inteiros e informar qual é o maior, ou se são iguais
a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
if a > b:
    print(f"O número {a} é maior que o número {b}.")
elif b > a:
    print(f"O número {b} é maior que o número {a}.")
else:
    print("Os números são iguais.") 

#============================================================================================================================================

# ler três números e informar qual é o maior
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"O número {numero1} é o maior.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} é o maior.")
elif numero3 > numero1 and numero3 > numero2:
    print(f"O número {numero3} é o maior.")
else:
    print("Os números são iguais.")

#============================================================================================================================================

# ler o ano de fabricação de um carro e informar se é velho (antes de 2000) ou novo (2000 ou depois)
AnoDoCarro = int(input("Digite o ano do carro: "))
if AnoDoCarro <= 2000:
    print("Carro velho")
else:
    print("Carro novo")

#============================================================================================================================================

# ler um número e informar se é par ou ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.") 
#============================================================================================================================================

# ler a idade de uma pessoa e informar se é maior ou menor de idade
idade = int(input("Digite a idade da pessoa: "))
if idade >= 18:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é menor de idade.")
#============================================================================================================================================

# ler a temperatura em graus Celsius e informar se está quente (acima de 30°C) ou frio (30°C ou abaixo)
temperatura = float(input("Digite a temperatura em graus Celsius: "))
if temperatura > 30:
    print("Está quente.")
else:
    print("Está frio.")
#============================================================================================================================================