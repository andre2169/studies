# Programa que verifica se um empréstimo para compra de uma casa será aprovado ou negado
# O usuário informa o valor da casa, o salário do comprador e em quantos anos deseja pagar.
# A prestação mensal não pode ultrapassar 30% do salário do comprador.
# Função para ler valores monetários com vírgula ou ponto
#   Exemplo: "2500,75" ou "2500.75"

def ler_dinheiro(msg):
    valor = input(msg)
    valor = valor.replace(".", "").replace(",", ".")
    return float(valor)

ValorDaCasa = ler_dinheiro("Digite o valor da casa: ")
SalarioComprador = ler_dinheiro("Digite o salário do comprador: ")
AnosParaPagamento = int(input("Digite em quantos anos o comprador deseja pagar: "))
ValorDaPrestacao = ValorDaCasa / (AnosParaPagamento * 12)

if ValorDaPrestacao > (SalarioComprador * 0.30):
    print("Empréstimo negado.")
else:
    print(f"Empréstimo aprovado. Valor da prestação mensal: R$ {ValorDaPrestacao:.2f}")
