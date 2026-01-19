numero1 = int(input("Digite o primeiro número: "))
numer2 = int(input("Digite o segundo número: "))
soma = numero1 + numer2
print(f"A soma de {numero1} + {numer2} é igual a {soma}")

# ==============================================================================================================================================================

metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"O valor em milímetros é: {milimetros} mm")

# ==============================================================================================================================================================

dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))
total_segundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
print(f"O total em segundos é: {total_segundos}")

# ==============================================================================================================================================================

salario = float(input("Digite o salário do funcionário: "))
aumento = float(input("Digite o percentual de aumento (em %): "))
novo_salario = salario + (salario * aumento / 100)
print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}, teve um aumento de R$ {novo_salario - salario:.2f}")

# ==============================================================================================================================================================

NomeMercadoria = str(input("Digite o nome da mercadoria: "))
ValorMercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o valor do desconto: "))
valorFinal = ValorMercadoria - desconto
print(f"A {NomeMercadoria}, sofreu um desconto de R$ {desconto:.2f}, O valor final é: R$ {valorFinal:.2f}")

# ==============================================================================================================================================================

temperaturaCelsius = float(input("Digite a temperatura em Celsius: "))
temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {temperaturaFahrenheit:.2f}")

# ==============================================================================================================================================================

AluguelPorDia = 60
AluguelPorKm = 0.15
Dias = int(input("Quantos dias alugados? "))
Km = float(input("Quantos Km rodados? "))
Total = (AluguelPorDia * Dias) + (AluguelPorKm * Km)
print(f"O total a pagar é: R$ {Total:.2f}")

# ==============================================================================================================================================================

QuantidadeDeCigarrosPorDia = int(input("Quantos cigarros você fuma por dia? "))
AnosFumando = int(input("Há quantos anos você fuma? "))
perdaDeVidaPorCigarro = 10 # minutos
DiasDeVidaPerdidos = (QuantidadeDeCigarrosPorDia * perdaDeVidaPorCigarro * AnosFumando * 365) / 1440
print(f"Você perdeu aproximadamente {DiasDeVidaPerdidos:.2f} dias de vida devido ao tabagismo.")

# ==============================================================================================================================================================

distanciaEmKm = float(input("Digite a distância em Km: "))
velocidadeMediaEmKmh = float(input("Digite a velocidade média: "))
tempoEmHoras = distanciaEmKm / velocidadeMediaEmKmh
print(f"O tempo estimado de viagem é: {tempoEmHoras:.2f} horas")