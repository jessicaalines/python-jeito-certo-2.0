idade = int(input("Digite a sua idade: "))

if idade < 16:
    print(f"Você ainda não pode votar. A idade mínima para voto no Brasil é de 16 anos e você ainda tem {idade} anos.")

if idade >= 18 and idade <= 69:
    print(f"Como você tem {idade}, você está na faixa de voto obrigatório.")

if idade >= 16 or idade <= 17 or idade >=70:
    print(f"Você pode votar apenas se quiser. Você tem {idade} anos e está na faixa do voto facultativo, juntamente com as pessoas não alfabetizadas.")