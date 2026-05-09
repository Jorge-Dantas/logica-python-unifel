# 15. Alternador de Status: A variável ativo começa como True. Imprima essa
# linha no início (para vermos): print(f"Início: {ativo} (Identidade: {ativo is True})").
# Após isso, em uma única linha, inverta o valor lógico dela (sem if - desafio
# simples, porém grande, de lógica).
# ● A tarefa: Você deve garantir que a inversão ocorra de forma que, se
# compararmos ativo is True no início e no fim, o resultado mude. Faça
# estes prints no início e no fim para comprovar o sucesso de sua lógica.
# ● O Desafio: Faça a inversão sem usar o operador not. Use apenas
# operadores matemáticos/lógicos.
# ● Imprima no fim: print(f"Fim: {ativo} (Identidade: {ativo is True})")
ativo = False
print(f"Início: {ativo} (Identidade: {ativo is True}) \n")
print("-" * 30)

# 0 -> FALSE e 1 -> TRUE
ativo = bool(1 - ativo)

print("\n")
print(f"Início: {ativo} (Identidade: {ativo is True}) \n")
# print(f"Status do Sistema: {status}")
print("-" * 30)
