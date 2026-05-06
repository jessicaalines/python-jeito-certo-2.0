valor_produto = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

def calcula_preco_final(valor_produto, quantidade):
    valor_total = valor_produto * quantidade

    if quantidade >= 10:
        desconto = valor_total * 0.1
        return (valor_total - desconto)

    else:
        return "Não há desconto. A quantidade é menor do que dez."

valor_final = calcula_preco_final(valor_produto, quantidade)
print(f"O valor final com desconto é: {valor_final:.2f}")