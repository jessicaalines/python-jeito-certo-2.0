nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
mediaAluno = (nota1 + nota2) / 2
mediaEscola = 6.0

if mediaAluno >= mediaEscola:
    print(f"Aprovado! A sua média é {mediaAluno}")

else:
    print(f"Reprovado! A sua média é {mediaAluno} média da escola é {mediaEscola}")