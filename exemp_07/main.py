# exemp_07: O Arquiteto de Piscinas (Potência e Float)
# Cenário: Um arquiteto precisa calcular o volume de uma piscina cúbica para
#  decidir a bomba de filtragem.
# Objetivo: Peça ao usuário (via input) o
# lado do cubo em metros e calcule o volume em litros.

# Fórmula do Volume: Lado^3
# Conversão: 1m^3 = 1000 litros.
# Saída esperada: "A piscina de lado "X"m suporta Y litros de água."

print("\n" * 1)

# ENTRADA DE DADOS VIA TECLADO
lado_em_metros = input("Digite o tamanho do lado da piscina (metros): ")
# lado = float(lado_em_metros) -> Entrada simples. Como resolver se o cara digitar com . ou ,?

# Se vier com vírgula(,)  converta para ponto (.)
lado = float(lado_em_metros.replace(",", "."))
print(f"Lado da piscina (em metros) = {lado}")

# Fórmula do Volume: Lado^3
volume_metro_cubico = lado**3

# Conversão: 1m^3 = 1000 litros
volume_litros = volume_metro_cubico * 1000


print("\n" * 1)
print("-" * 30)
print(f"A piscina de lado {lado}m suporta {volume_litros} litros de água.")
print("\n" * 1)
