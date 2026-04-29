nota_aluno = float(input("Digite a sua nota: "))
media_alta = 7
media_baixa = 5

if nota_aluno >= media_alta:
    print("Parabéns, você passou direto!")

elif nota_aluno < media_alta and nota_aluno >= media_baixa:
    print(" Você precisa fazer a prova final")

    prova_final = float(input("Digite a sua nota da prova final: "))

    if prova_final >= media_baixa:
        print("Você foi aprovado na prova final")

    else:
        print("Você terá que fazer a recuperação final")

        rf = float(input("Digite a sua nota da recuperação final: "))

        if rf >= media_baixa:
            print("Você passou na recuperação final, parabéns!")

        else:
            print("Você reprovou!")

elif nota_aluno < media_baixa:
    print("Você terá que fazer a recuperação final!")

    recup_final = float(input("Digite a sua nota da recuperação final: "))

    if recup_final >= media_baixa:
        print("Ufa, você foi aprovado na recuperação final!")

    else:
        print("Não foi dessa vez, amigão. Você reprovou!")