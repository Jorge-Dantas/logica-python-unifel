# exemp_04
# Operadores BÁSICOS

from decimal import Decimal

# Forma antiga:
# print("Soma: 10 + 3 = ")
# print(10 + 3)

# String formatada (interpolação)
print(f"Soma: 10 + 3 = {10 + 3}")  # 13
print(f"Potência: 2^3 = {2 ** 3}")  # Tem que dar 8
print(f"Divisão Float: 10 / 3 = {10 / 3}")  # 3.3333333333333335
print(f"Divisão Inteira (Truncada): 10 // 3 = {10 // 3}")  # 3, e esquece 1 (sobra)
print(f"Resto da Divisão (Módulo): 10 % 3 = {10 % 3}")  # 1, 10 / 3 = 3 e SOBRA 1.
print("\n\n")

# A base matemática da computação é toda 2!!
# 1, 2, 4, 8, 16, 32, 64, 128, 256, 516, 1024(1GB), 2048(2GB), 4096(4GB), 8192(8GB)


# SOBRECARGA DE OPERADORES
print("-" * 30)  # - 30 vezes..

# O PERIGO POR DEBAIXO DOS PANOS DO FLOAT...
print(
    # 0.90000000000000002220.. Ou outra coisa..
    f"FLOAT 0.8 + 0.1 = {0.8 + 0.1:.20f}"
)

# DECIMAL EXIGE O USO DE ASPAS SIMPLES ''
valor_decimal1 = Decimal("0.8")
valor_decimal2 = Decimal("0.1")
print(f"DECIMAL 0.8 + 0.1 = {valor_decimal1 + valor_decimal2:.15f}")  # 0.9 EXATO!!
print("\n\n")
