# 03. Decomposição de Tempo (Automação Industrial): Um sensor de esteira
# conta o tempo de operação em segundos. Receba um valor inteiro de segundos
# (ex: 10.000) e decomponha-o em Horas, Minutos e Segundos restantes.
# ● Exemplo: 3661 segundos = 1 Hora, 1 Minuto e 1 Segundo.
# ● Use ferramentas dadas em aulas até aqui. Não use funções prontas.
print("\n")
total_em_segundos = int(input("Digite o tempo total (em segundos): "))

# Converte o total digitado em segundos para horas (mas sem resto)
tempo_em_horas = total_em_segundos // 3600

resto = total_em_segundos % 3600  # Pega o resto da operação acima
tempo_em_minutos = resto // 60  # Converte o resto em minutos
segundos_finais = resto % 60  # Pega o resto dos minutos e salva (segundos)

print(
    f" Horas: {tempo_em_horas} | Minutos: {tempo_em_minutos} | Segundos: {segundos_finais}"
)
print("\n")
