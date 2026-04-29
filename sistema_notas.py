nota_numerica = float(input("Digite a sua nota: "))

if nota_numerica >= 9.7 and nota_numerica <= 10:
    print("Seu conceito é A+ \nParabéns")

elif nota_numerica >= 9.3 and nota_numerica <= 9.6:
    print("Seu conceito é A")

elif nota_numerica >= 9 and nota_numerica <= 9.2:
    print("Seu conceito é A-")

elif nota_numerica >= 8.7 and nota_numerica <= 8.9:
    print("Seu conceito é B+")

elif nota_numerica >= 8.3 and nota_numerica <= 8.6:
    print("Seu conceito é B")

elif nota_numerica >= 8.0 and nota_numerica <= 8.2:
    print("Seu conceito é B-")

elif nota_numerica >= 7.7 and nota_numerica <= 7.9:
    print("Seu conceiro é C+")

elif nota_numerica >= 7.3 and nota_numerica <= 7.6:
    print("Seu conceito é C")

elif nota_numerica >= 7.0 and nota_numerica <= 7.2:
    print("Seu conceito é C-")

elif nota_numerica >= 6.7 and nota_numerica <= 6.9:
    print("Seu conceito é D+")

elif nota_numerica >= 6.0 and nota_numerica <= 6.6:
    print("Seu conceito é D")

elif nota_numerica >= 0.0 and nota_numerica <= 5.9:
    print("Seu conceito é F \nIsso significa reprovação!")

else:
    print("Digite uma nota válida!")