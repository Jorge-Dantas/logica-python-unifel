# exemp_08: Cashback do E-commerce (Sobrecarga de Operadores)
# Cenário: Uma loja quer gerar uma barra de progresso visual para o cashback do cliente.
# Objetivo: O cliente ganhou 10 pontos. Cada ponto vale um caractere █.

# Desafio: Crie a barra de progresso usando "multiplicação de strings"
# e concatene com a porcentagem final.

# Saída esperada: Progressão: [██████████] 100% (Use o + para colar os textos).

print("\n")

pontos = 10
ponto_barra_progressao = "█"
porcentagem = "100%"

# Relacionando os conceitos para o Python saber como lidar
barra_visual = ponto_barra_progressao * pontos

# Concatenação (com +)
# barra_final = "Progressão: [" + barra_visual + "]" + porcentagem

# A versão INTERPOLADA ficaria:
barra_final = f"Progressão: [{barra_visual}] {porcentagem}"
print(barra_final)

print("\n")
print("-" * 30)
print("\n\n")
