
# leitura de dois números e exibição da soma
numero1 = int(input("Digite o primeiro número: "))
numer2 = int(input("Digite o segundo número: "))
soma = numero1 + numer2
print(f"A soma de {numero1} + {numer2} é igual a {soma}")

# ==============================================================================================================================================================

# conversão de metros para milímetros
metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"O valor em milímetros é: {milimetros} mm")

# ==============================================================================================================================================================

# cálculo do total de segundos a partir de dias, horas, minutos e segundos
dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))
total_segundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
print(f"O total em segundos é: {total_segundos}")

# ==============================================================================================================================================================

# cálculo do novo salário com base em aumento percentual
salario = float(input("Digite o salário do funcionário: "))
aumento = float(input("Digite o percentual de aumento (em %): "))
novo_salario = salario + (salario * aumento / 100)
print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}, teve um aumento de R$ {novo_salario - salario:.2f}")

# ==============================================================================================================================================================

# cálculo do valor final de uma mercadoria após desconto
NomeMercadoria = str(input("Digite o nome da mercadoria: "))
ValorMercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o valor do desconto: "))
valorFinal = ValorMercadoria - desconto
print(f"A {NomeMercadoria}, sofreu um desconto de R$ {desconto:.2f}, O valor final é: R$ {valorFinal:.2f}")

# ==============================================================================================================================================================

# conversão de temperatura de Celsius para Fahrenheit
temperaturaCelsius = float(input("Digite a temperatura em Celsius: "))
temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {temperaturaFahrenheit:.2f}")

# ==============================================================================================================================================================

# cálculo do custo total de um aluguel de carro
AluguelPorDia = 60
AluguelPorKm = 0.15
Dias = int(input("Quantos dias alugados? "))
Km = float(input("Quantos Km rodados? "))
Total = (AluguelPorDia * Dias) + (AluguelPorKm * Km)
print(f"O total a pagar é: R$ {Total:.2f}")

# ==============================================================================================================================================================

# cálculo de dias de vida perdidos por fumar cigarros
QuantidadeDeCigarrosPorDia = int(input("Quantos cigarros você fuma por dia? "))
AnosFumando = int(input("Há quantos anos você fuma? "))
perdaDeVidaPorCigarro = 10 # minutos
DiasDeVidaPerdidos = (QuantidadeDeCigarrosPorDia * perdaDeVidaPorCigarro * AnosFumando * 365) / 1440
print(f"Você perdeu aproximadamente {DiasDeVidaPerdidos:.2f} dias de vida devido ao tabagismo.")

# ==============================================================================================================================================================

# cálculo do tempo estimado de viagem com base na distância e velocidade média
distanciaEmKm = float(input("Digite a distância em Km: "))
velocidadeMediaEmKmh = float(input("Digite a velocidade média: "))
tempoEmHoras = distanciaEmKm / velocidadeMediaEmKmh
print(f"O tempo estimado de viagem é: {tempoEmHoras:.2f} horas")