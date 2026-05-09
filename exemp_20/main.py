# Assinatura da função (criação)
def calcular_imposto(valor, taxa=0.15):  # taxa é um parâmetro default
    valor = 1500
    return valor * taxa


print()
valor_a_taxar = 1000
total = calcular_imposto(valor_a_taxar)  # Usa taxa padrão = 1000 * 15%
vip = calcular_imposto(valor_a_taxar, taxa=0.05)  # Parâmetro nomeado. 5%

print(f"Calculando imposto de 1000 (taxa padrão de 15%): {total} \n")

print(f"Calculando imposto de 1000 (taxa de 5%): {vip} \n")

print(f"Imprimindo a variável valor_a_taxar: {valor_a_taxar} \n\n")
print()

# PASSAGEM POR VALOR X REFERÊNCIA
# TUDO NO PYTHON É UM OBJETO!!!
