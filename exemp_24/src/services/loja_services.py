def calcular_carrinho(desconto: float, *precos: float) -> float:

    soma = sum(precos)  # sum é um método/função interno que soma iteráveis
    total = soma - (soma * desconto)
    return total


# Formatação com função Lambda:
formatar_real = lambda valor: f"R$ {valor:.2f}".replace(".", ",")
