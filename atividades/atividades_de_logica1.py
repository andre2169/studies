
# Calcule o valor da passagem de um ônibus com base na distância a ser percorrida.
# O valor da passagem é de R$ 0,50 por Km para viagens de até 200 Km.
# Para viagens acima de 200 Km, o valor da passagem é de R$ 0,45 por Km.
DistanciaEmKm = float(input("Digite a distância em quilômetros: "))
valorpassagem = 0.50
valorTotal = DistanciaEmKm * valorpassagem

if DistanciaEmKm <= 200:
    print(f"O valor da passagem é: R$ {valorTotal:.2f}")
else:
    valorpassagem = 0.45
    valorTotal = DistanciaEmKm * valorpassagem
    print(f"O valor da passagem é: R$ {valorTotal:.2f}")

# ==============================================================================================================================================================
# Cálculo do valor da conta telefônica com base no número de minutos utilizados.
# if aninhado para determinar a tarifa por minuto.
minutos = int(input("Quantos minutos você utilizou este mês?"))
if minutos <= 200:
    valorTotal = 0.20
else:
    if minutos < 400:
        valorTotal = 0.18
    valorTotal = 0.15
print(f"O valor total da conta é: R$ {valorTotal:.2f}")

# ==============================================================================================================================================================