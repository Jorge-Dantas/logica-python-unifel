# Com cópia RASA
def aplicar_bonus_copia(vendas):
    vendas_copia = vendas[:]  # CÓPIA RASA -> Shallow copy

    for i in range(len(vendas_copia)):
        vendas_copia[i] *= 1.05  # Aplicando 5% no valor de vendas
    return vendas_copia


# Fazendo DIRETO na lista
def aplicar_bonus_direto(vendas):
    for i in range(len(vendas)):
        vendas[i] *= 1.05  # Aplicando 5% no valor de vendas


# REGRA DE OURO:
# Quer segurança dos dados da lista original: LISTA NOVA
# Praticidade: Cópia rasa ([:])
# Quer uma cópia profunda?? => DEEPCOPY (lista.deepcopy())
