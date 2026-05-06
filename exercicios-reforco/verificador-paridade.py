
numero = int(input("Digite um número inteiro: "))

def eh_par(numero):
    if numero % 2 == 0:
        return "Par"

    else:
        return "Ímpar"

resultado1 = eh_par(numero)
print(f"O número {numero} é {resultado1}")

