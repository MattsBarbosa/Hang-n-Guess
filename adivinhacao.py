import random
def jogar():
    print("***************************************")
    print("***Bem vindo ao jogo de Adivinhação!***")
    print("***************************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Selecione o Nível:"))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}. Sua pontuação é: {pontos}.")
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou" , chute)

        if (chute < 1 or chute > 100):
            print("Você digitou um número inválido.")
            continue

        acertou = chute == numero_secreto
        menor   = chute < numero_secreto
        maior   = chute > numero_secreto

        if (acertou):
            print(f"Você acertou! Com a pontuação de: {pontos}!")
            break
        else:
            if(menor):
                print("Você errou, O seu chute foi menor que o número.")
            elif(maior):
                print("Você errou, O seu chute foi maior que o número")
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

    #while(rodada <= total_tentativas):
    #rodada = rodada + 1
    #range(start, stop, [step])
    #print("Tentativa {} de {}.".format(rodada, total_tentativas))

