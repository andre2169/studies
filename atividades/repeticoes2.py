# Quiz de perguntas e respostas usando repetição
# foi utilizado while para repetir as perguntas e um contador para controlar o número da questão.
# Cada pergunta é apresentada com suas opções, e a resposta do usuário é verificada.
# nos inputs das respostas, é utilizado strip() para remover espaços em branco e upper() para padronizar a resposta em maiúsculas.
# A pontuação é incrementada para cada resposta correta, e ao final, a pontuação total é exibida.

pontos = 0
questao = 1

print("Responda as seguintes perguntas:\n")

while questao <= 3:

    if questao == 1:
        print("1. Qual a capital da França?")
        print("a) Berlim")
        print("b) Paris")
        print("c) Madrid")
        print("d) Roma")

        resposta = input("Sua resposta: ").strip().upper()

        if resposta == "B":
            pontos += 1

    elif questao == 2:
        print("\n2. Qual o maior planeta do sistema solar?")
        print("a) Júpiter")
        print("b) Saturno")
        print("c) Marte")
        print("d) Terra")

        resposta = input("Sua resposta: ").strip().upper()

        if resposta == "A":
            pontos += 1

    elif questao == 3:
        print("\n3. Quem escreveu 'Dom Quixote'?")
        print("a) William Shakespeare")
        print("b) Charles Dickens")
        print("c) Mark Twain")
        print("d) Miguel de Cervantes")

        resposta = input("Sua resposta: ").strip().upper()

        if resposta == "D":
            pontos += 1

    questao += 1 

print(f"\nVocê fez {pontos} pontos.")
