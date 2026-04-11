numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))

mediaSimples = (numero1 + numero2) / 2
mediaPonderada = ((numero1 * 4) + (numero2 * 2)) / (4 + 2)
mediaHarmonica = 2 * (numero1 * numero2) / (numero1 + numero2)

print(f"A média simples de {numero1} e {numero2} é {mediaSimples}")
print(f"A média ponderada de {numero1} e {numero2} é {mediaPonderada:.2f}")
print(f"A média harmônica de {numero1} e {numero2} é {mediaHarmonica:.2f}")