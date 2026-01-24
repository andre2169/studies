# Cálculo do valor a ser pago por consumo de energia elétrica
# O usuário informa a quantidade de kWh consumida e o tipo de instalação.
# Tipos de instalação:
# R - Residencial
# C - Comercial
# I - Industrial
# Tarifas:
# Residencial: até 500 kWh - R$ 0,40 por kWh
#              acima de 500 kWh - R$ 0,65 por kWh
# Comercial: até 1000 kWh - R$ 0,55 por kWh
#            acima de 1000 kWh - R$ 0,60 por kWh
# Industrial: até 5000 kWh - R$ 0,55 por kWh
#             acima de 5000 kWh - R$ 0,60 por kWh
 
quantidade_kwh = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R - Residencial, C - Comercial, I - Industrial): ").upper()

if tipo_instalacao == 'R':
    if quantidade_kwh <= 500:
        valor_total = quantidade_kwh * 0.40
    else:
        valor_total = quantidade_kwh * 0.65
elif tipo_instalacao == 'C':
    if quantidade_kwh <= 1000:
        valor_total = quantidade_kwh * 0.55
    else:
        valor_total = quantidade_kwh * 0.60
elif tipo_instalacao == 'I':
    if quantidade_kwh <= 5000:
        valor_total = quantidade_kwh * 0.55
    else:
        valor_total = quantidade_kwh * 0.60
else:
    valor_total = None
    print("Tipo de instalação inválido.")
if valor_total is not None:
    print(f"O valor total a ser pago é: R$ {valor_total:.2f}")

