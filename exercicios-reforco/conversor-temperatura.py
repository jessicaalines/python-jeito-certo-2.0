def celsius_para_fahrenheit(temperatura):
    fahrenheit = (temperatura * 9 / 5) + 32

    return fahrenheit

celsius = float(input("Digite uma temperatura: "))
resultado = celsius_para_fahrenheit(celsius)

print(f"A temperatura em Fahrenheit é: {resultado}")