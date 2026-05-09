from src.services.comissao_valores import aplicar_bonus_direto, aplicar_bonus_copia

vendas_mes_maio = [1000.0, 1500.00, 3575.99]


# SEGURO (CÓPIA RASA): Cria uma nova lista (memória) e copia os valores da original
vendas_com_bonus = aplicar_bonus_copia(vendas_mes_maio)
print(f"\n ORIGINAIS (seguro, cópia rasa): {vendas_mes_maio}\n")

# PERIGOSO: PERDI MEUS DADOS ORIGINAIS!!
aplicar_bonus_direto(vendas_mes_maio)
print(f"\n ORIGINAIS (perigoso, vai alterar): {vendas_mes_maio}\n\n")


print(id(vendas_mes_maio))  # Original
print(id(vendas_com_bonus))  # Lista nova que nasceu da cópia rasa
