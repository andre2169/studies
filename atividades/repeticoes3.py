# ler o numero que o usuario digita até que ele digite 0
# exibe quantidade de numeros digitados , soma de todos o numeros digitados e a media aritimetica.

soma_dos_numeros = 0
quantidade = 0

while True:
    valor_a_somar = int(input("Digite um número a somar ou 0 (zero) para sair do programa: "))
    
    if valor_a_somar == 0:
        break

    soma_dos_numeros += valor_a_somar
    quantidade += 1

if quantidade > 0:
    media = soma_dos_numeros / quantidade
    print("Quantidade de números digitados:", quantidade)
    print("Soma dos números:", soma_dos_numeros)
    print("Média aritmética:", media)
else:
    print("Nenhum número foi digitado.")

#=============================================================================================================================
# maquina de soma do valor dos produtos selecionados 

total = 0.0

while True:
    codigo = int(input("Digite o código do produto (0 para sair): "))

    if codigo == 0:
        break

    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Erro: código inválido!")
        continue

    quantidade = int(input("Digite a quantidade comprada: "))
    if quantidade <= 0:
        print("Quantidade invalida!!")
        continue
#    else:
    total += preco * quantidade

print("Total da compra: R$", total)
