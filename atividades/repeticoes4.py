# contador de cedulas referente ao valor a ser pago
# Exemplo
# Digite o valor a paga:745
# 14 cedulas(s) de R$50
# 2 cedulas(s) de R$20
# 0 cedulas(s) de R$10
# 1 cedulas(s) de R$5


# recebe o valor como string
valor_str = input("Digite o valor a pagar: ")
valor_str = valor_str.replace('.', '')
valor_str = valor_str.replace(',', '.')

valor = float(valor_str) # converte de string para float e atribui a variavel valor

if valor <= 0:
      print("Valor inválido!")
else:
    centavos = int(valor * 100 + 0.5) # converte para centavos e arredonda o valor
    apagar = centavos
    atual = 10000 # como o valor inicial é R$100 equivalem a 10000 centavos
    cedulas = 0

    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            if cedulas > 0:  # Só imprime se houver unidades usadas
                if atual >= 100:  # É uma nota (R$ 1 ou mais)
                    print(f"{cedulas} cédula(s) de R${atual // 100}")
                else:  # É uma moeda (menos de R$ 1)
                    print(f"{cedulas} moeda(s) de R$0,{atual:02d}")

            # Transições para a próxima unidade (em centavos) - AGORA DENTRO DO ELSE
            if atual == 10000:  # R$ 100
                atual = 5000   # R$ 50
            elif atual == 5000:  # R$ 50
                atual = 2000   # R$ 20
            elif atual == 2000:  # R$ 20
                atual = 1000   # R$ 10
            elif atual == 1000:  # R$ 10
                atual = 500    # R$ 5
            elif atual == 500:  # R$ 5
                atual = 200    # R$ 2
            elif atual == 200:  # R$ 2
                atual = 100    # R$ 1,00
            elif atual == 100:  # R$ 1,00
                atual = 50     # R$ 0,50
            elif atual == 50:   # R$ 0,50
                atual = 25     # R$ 0,25
            elif atual == 25:   # R$ 0,25
                atual = 10     # R$ 0,10
            elif atual == 10:   # R$ 0,10
                atual = 5      # R$ 0,05
            elif atual == 5:    # R$ 0,05
                atual = 1      # R$ 0,01
            else:
                break   

            cedulas = 0  # Reset de cedulas AGORA DENTRO DO ELSE, após as transições