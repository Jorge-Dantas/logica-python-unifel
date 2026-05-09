# O Simulador de Leilão
# Cenário: Um leilão de arte onde os lances acontecem até o martelo bater,
# e o relatório final deve exibir.

print("-" * 30)
print(" LEILÃO DE ARTE 1.0 ")
print("-" * 30)


maior_lance = 0.0  # False
lance_ativo = True

# Parte 1
while lance_ativo:
    novo_lance = float(input(" Digite seu lance (0 para sair) "))

    if novo_lance == 0:
        lance_ativo = False
        break  # Garantia de saída do loop!

    # Se saiu um NOVO maior lance, salve ele!
    if novo_lance > maior_lance:
        maior_lance = novo_lance
        print(f" NOVO RECORDE: {maior_lance} \n")
    else:
        print(" Lance ignorado (lance menor que o maior lance)")

# Fase 2
print("-" * 30)
print("\n --- RESUMO DE LOTES DISPONÍVEIS --- ")
print("-" * 30)

# Simulando a quantidade de lotes disponíveis do leilão
for lote in range(101, 106):
    print(f" Lote #{lote}: Ainda disponível para lances!!! ")


print("-" * 30)
print()
