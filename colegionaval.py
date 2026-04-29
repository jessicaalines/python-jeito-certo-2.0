nota = 4
media_alta = 7
media_baixa = 5

if nota >= media_alta:
    print("Aprovado direto! :D")

elif nota >= media_baixa:
    print("Fazer prova final")

    nota_pf = 6.0

    if nota_pf >= media_baixa:
        print("Aprovado na prova final")

    else:
        print("Precisa fazer a recuperação final")

else:
    print("Fazer recuperação final")

    nota_rf = 5.0

    if nota_rf >= media_baixa:
        print("Aprovado na recuperação final!")

    else:
        print("REPROVADO!")
