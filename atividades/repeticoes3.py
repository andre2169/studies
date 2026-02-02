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
