def formatar_moeda(valor):
    valor_formatado = f"R$ {valor:,.2f}"
    texto = valor_formatado.replace(",", "x").replace(".", ",").replace("x", ".")
    return texto


def tratar_input(texto_user):
    return texto_user.replace(",", ".")
