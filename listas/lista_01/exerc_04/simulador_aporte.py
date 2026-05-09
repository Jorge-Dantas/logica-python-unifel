# 04. Simulador de Investimento com Aporte: Um acionista quer prever seu
# saldo. Receba o valor_inicial e a taxa_rendimento (EM %).
# ● Ex: Se a taxa de rendimento digitada for 5, isso equivale a 5% (converta no
# código para que funcione).
# ● Se o rendimento bruto (Valor * Taxa) for um número par na sua parte inteira,
# o banco cobra uma taxa de custódia de R$ 10,00.
# ● Se for ímpar, a taxa é de R$ 5,00.
# ● Saída: Exiba o lucro líquido (Rendimento - Taxa) usando o tipo adequado.
from decimal import Decimal

print("\n")
valor_inicial = Decimal(input(" Digite o valor inicial do Aporte: "))
taxa_rendimento = Decimal(input(" Digite o valor da taxa de rendimento (em %): "))

taxa_rendimento = taxa_rendimento / 100  # Convertendo número para porcentagem

# print(f"Taxa já convertida (%) = {taxa_rendimento} \n")

rendimento_bruto = valor_inicial * taxa_rendimento  # Decimal

# Pega só a parte INTEIRA de rendimento_final
rendimento_parte_int = int(rendimento_bruto)

if rendimento_parte_int % 2 == 0:
    custodia = Decimal("10.00")
else:
    custodia = Decimal("5.00")

lucro_liquido = rendimento_bruto - custodia

print("\n")
print("-" * 40)
print(f" Rendimento Bruto: R$ {rendimento_bruto}")
print(f" Parte inteira do Rendimento Bruto: {rendimento_parte_int}")
print(f" Taxa de custodia: R$ {custodia}")
print("-" * 40)
print(f" Lucro Líquido (REAL): R$ {lucro_liquido}")
print("-" * 40)
