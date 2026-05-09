from decimal import Decimal


def obter_valor_valido(mensagem):
    while True:
        try:
            # Antes de tentar converter para Decimal estou tratando a vírgula
            valor = Decimal(input(mensagem).replace(",", "."))
            if valor > 0:
                return valor

            print("[ERRO]: O valor deve ser significativo (maior que zero)!! \n")

        except ValueError:
            print("[ERRO]: Entrada inválida! Digite um número no formato correto! \n")


# Perceba a taxa opcional, se você informar outra taxa no momento do uso dessa função,
# ela vai assumir esse outro valor informado no lugar de 0.01.
def calcular_rendimento(valor, meses, taxa=Decimal("0.01")):
    # Juros compostos de 1%/mês aplicados ao valor inicial por x meses
    saldo_final = valor * (1 + taxa) ** meses
    # Calculo do lucro real da aplicação
    lucro = saldo_final - valor
    return lucro, saldo_final  # Retorna tupla de resultados (top!!)
