# Programa que lê 5 notas e calcula a média 
# Utilizando acumuladores e repetição 
#contador = 1
#soma = 0
#while contador <= 5:
#    nota = float(input(f"{contador}. Digite as notas: "))
#    soma = soma + nota
#    contador = contador + 1 
#print(f"A soma das notas é: {soma/5:5.2f}")
# =============================================================================================================================

# Programa que calcula o saldo de uma poupança após 24 meses
# considerando um depósito inicial e uma taxa de juros mensal
#print("Cálculo do saldo de uma poupança após 24 meses")

#deposito_inicial = float(input("Digite o valor do depósito inicial: "))
#taxa_juros_poupanca = float(input("Digite a taxa de juros (em %): "))
#saldo = deposito_inicial
#total_juros = 0
#for mes in range(1, 25):
#    juros_mes = saldo * (taxa_juros_poupanca / 100)
#    saldo += juros_mes
#    total_juros += juros_mes
#    print(f"Mês {mes}: Saldo: {saldo:,.2f} | Juros ganhos: {juros_mes:,.2f}")
#print(f"Total de ganhos com juros em 24 meses: {total_juros:,.2f}")


# =============================================================================================================================

# Programa que calcula o saldo de uma poupança após 24 meses
# considerando um depósito inicial e uma taxa de juros mensal usando while
print("Cálculo do saldo de uma poupança após 24 meses")
deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros_poupanca = float(input("Digite a taxa de juros (em %): "))
saldo = deposito_inicial
total_juros = 0
mes = 1
while mes <= 24:
    juros_mes = saldo * (taxa_juros_poupanca / 100)
    saldo += juros_mes
    total_juros += juros_mes
    print(f"Mês {mes}: Saldo: {saldo:,.2f} | Juros ganhos: {juros_mes:,.2f}")
    mes += 1
print(f"Total de ganhos com juros em 24 meses: {total_juros:,.2f}")

# =============================================================================================================================