# exemp_05: O Ingresso do Festival (Básico: Operadores e F-Strings)
# Cenário: Você está organizando um festival de música.
# Um cliente quer comprar 4 ingressos do setor VIP.
# Objetivo: Calcule o valor total da compra e exiba um recibo organizado.

# Preço VIP: R$ 450.00
# Taxa de conveniência por ingresso: R$ 35.00
# SUB TOTAL = Preço VIP * quantidade
# TAXA TOTAL = Conveniência(Preço) * quantidade
# VALOR FINAL = Sub-total + Taxa total

# Saída esperada: Um cabeçalho com "-" * 30, o subtotal, a taxa total e o valor final.


# ENTRADA DOS DADOS
preco_vip = 450.00
taxa_conveniencia = 35.00
quant_ingressos = 4

# OBS: Números com casas decimais serão dinamicamente tipados como FLOAT!!
# Deixamos float para demonstrar isso (mas para dinheiro use DECIMAL)

# PROCESSAMENTO
sub_total = preco_vip * quant_ingressos  # FLOAT
taxa_total = taxa_conveniencia * quant_ingressos  # FLOAT
valor_final = sub_total + taxa_total  # FLOAT + FLOAT

print("\n" * 1)

# SAÍDA (Recibo organizado)
print("-" * 30)
print(f"{"RECIBO DA COMPRA":^30} ")  # ^ centraliza (em 30 de largura)
print("-" * 30)

print(f" SUB-TOTAL: R$ {sub_total:>6.2f}")  # > alinha a esquerda
print(f" TAXAS: R$ {taxa_total:>6.2f}")
print("-" * 30)
print(f" VALOR FINAL (TOTAL): R$ {valor_final:>6.2f}")
print("-" * 30)

print("\n\n")


# print("TIPOS DAS VARIÁVEIS COM NOSSAS CONTAS: ")
# print(type(sub_total))
# print(type(taxa_total))
# print(type(valor_final))
