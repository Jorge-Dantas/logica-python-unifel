# exemp_06: O Checkout do Hotel (Módulo e Divisão Inteira)
# Cenário: Um hotel cobra por diárias de 24 horas.
# Um hóspede ficou 80 horas no hotel.
# Objetivo: Transforme essas horas em "Dias" e "Horas restantes" para o extrato.
# Dica: Use // para os dias e % para as horas que sobraram.
# Saída esperada: "O hóspede ficou X dias e Y horas."

print("\n" * 1)

horas_hospede = 80

dias = horas_hospede // 24  # Divisão INTEIRA = 72

# Pega as horas restantes (RESTO) do que sobrou de 80 / 24.
horas_restantes = horas_hospede % 24  # Horas restantes = 8.

dias = 80 // 24
horas_rest = 80 % 24

print("-" * 30)
print("EXTRATO DA ESTADIA: ")
print(f"O hóspede ficou {dias} dias e {horas_restantes} horas.")
print("-" * 30)
