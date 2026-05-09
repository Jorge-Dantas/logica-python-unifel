# 01. Gestão de Estoque Crítico: Uma importadora de hardware precisa de um
# sistema de reposição inteligente. Receba a categoria (string) e a quantidade (int).

# ● Se a categoria for "Acessórios": Repor se estoque estiver menor que 15.
# ● Se a categoria for "Periférico": Repor se estoque estiver menor que 25.

# ● O Desafio: Se a categoria for qualquer outra, o estoque mínimo de
# segurança é sempre 10.

# ● Saída: Exiba "REPOSIÇÃO SOLICITADA" apenas se o estoque estiver abaixo
# do limite para a categoria específica. Caso contrário, exiba "ESTOQUE
# INTEGRAL".


categoria = input("\n Digite a categoria (Acessórios / Periférico / Outros): ")
quantidade = int(input(" Digite a quantidade: "))

if categoria == "Acessórios":
    limite = 15
elif categoria == "Periférico":
    limite = 25
else:
    limite = 10

print("\n" * 1)
print("-" * 30)
if quantidade < limite:
    print(f"REPOSIÇÃO SOLICITADA '(Quantidade: {quantidade})'")
else:
    print(f"ESTOQUE INTEGRAL (OK) '(Quantidade: {quantidade})'")


#############

# ANDRÉ!
# categ = input("Entre com a categoria do produto: ").upper()
# quant = int(input("Entre com a quantidade do produto (inteiro): "))

# # match-case é ideal para condições com opções FIXAS!
# match categ:
#     case "ACESSÓRIOS":
#         repor = quant < 15  # expressão booleana (True/False)
#     case "PERIFÉRICOS":
#         repor = quant < 25
#     case _:
#         repor = quant < 10

# print(repor and "\n REPOSIÇÃO SOLICITADA" or "\nESTOQUE INTEGRAL")

print("-" * 30)
print("\n" * 1)


# QUIZ | Consolidar aprendizado da Lógica
# A) Qual a saída do comando print(10 > 5 and 2 < 3)?

# B) O que o Python imprime em print(not True or False)?

# C) Analise: print("" or "Backup"). Qual o valor exibido?

# D) Qual o resultado de print(5 < 10 < 20)?

# E) O que acontece se rodarmos print(False and print("Olá"))?

# F) Qual destes valores é considerado Truthy? (a: 0, b: 0.0, c: " ", d: [])

# G) Qual a ordem correta de precedência (do primeiro para o último)?

# H) O que resulta a comparação print("5" == 5)?

# I) Na expressão True or False and False, qual o resultado final?

# J) Se idade = 20, o que retorna print(18 <= idade <= 30)?

idade = 20
18 <= idade and idade <= 30
T and T = True # Regra and (E)
F or F = False # Regra aor (OU)
