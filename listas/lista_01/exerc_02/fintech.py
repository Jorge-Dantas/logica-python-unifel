# 02. Fintech: Um banco digital quer premiar clientes. Receba três depósitos: d1 =
# 0.1, d2 = 0.1 e d3 = 0.1.
# ● Cálculo: Faça a soma total. Se a soma for exatamente 0.3, exiba "Bônus
# Ativado".
# ● Se não for, exiba "Erro de cálculo, ".
# ● OBS: No final, seu algoritmo deve testar (e provar) se a soma dá
# exatamente 0.3 dentro do print. Deve sair algo como: “Soma correta: True”
from decimal import Decimal

print("\n")
d1 = Decimal(input("Digite o valor do 1º depósito (R$): "))
d2 = Decimal(input("Digite o valor do 1º depósito (R$): "))
d3 = Decimal(input("Digite o valor do 1º depósito (R$): "))

# 0.3 exato!
soma_total = d1 + d2 + d3

if soma_total == Decimal("0.3"):
    print("\nBônus Ativado")
else:
    print(
        f"\nErro de cálculo, a Soma Total foi de {soma_total}. Depósitos fora das regras da Fintech! \n"
    )

print("-" * 30)
print(f"Soma correta: {soma_total == Decimal("0.3")}")
print("-" * 30)
print("\n" * 1)
