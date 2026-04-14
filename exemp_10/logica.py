# Simulador de Aprovação de Crédito
# Objetivo: Desenvolver um algoritmo de decisão lógica para um
# banco digital que determine se um cliente pode ou não receber um empréstimo.


# Tarefas:
# Criar variáveis para armazenar os dados do cliente
# (Renda, Nome Limpo, Fiador e Idade).


# Aplicar as Regras de Negócio usando operadores lógicos e relacionais.
# Exibir o veredito final (True ou False) sobre a decisão de dar ou não o crédito.

# Regras de Negócio (Obrigatórias):

# Regra 1 (Saúde Financeira): O cliente deve ter renda acima de R$ 3.000,00
# E o nome deve estar limpo (não negativado).

# Regra 2 (Garantia Alternativa): Se o cliente não passar na Regra 1,
# ele ainda pode ser aprovado se tiver um Fiador.

# Regra 3 (Restrição Etária): Em qualquer um dos casos acima,
# o cliente NÃO pode ter menos de 18 anos e maior que 65.
from decimal import Decimal

print("-" * 30)
print("--- SISTEMA DE CRÉDITO | LÓGICA COM PYTHON 2026.3 ---")
print("-" * 30)

# ENTRADA DE DADOS
renda = Decimal(input("Digite a renda mensal: "))
sem_restricao = input("O nome está limpo? (sim/nao): ").lower() == "sim"
tem_fiador = input("Possui fiador? (sim/nao): ").lower() == "sim"
idade = int(input("Digite a idade: "))

# PROCESSAMENTO

# Regra 3 (Restrição Etária)
criterio_idade = 18 <= idade <= 65  # A idade do cara está entre 18 e 65?

# Regra 2 (Garantia Alternativa)
criterio_renda = tem_fiador == True

# Regra 1 (Saúde Financeira)
saude_financeira = (renda > 3000) and sem_restricao

aprovado = criterio_idade and (saude_financeira or criterio_renda)


# SAÍDA
print("-" * 30)
mensagem = aprovado and "PARABÉNS: Crédito aprovado!" or "Crédito negado."
print(f"RESULTADO DA ANÁLISE: {mensagem}")
print("-" * 40)


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
