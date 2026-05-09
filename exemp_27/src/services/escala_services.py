# total_dias => Quantos dias serão escalados (ex 30: um mês)
# intervalo => De quantos em quantos dias um médico é escalado
# Função que cria um calendário automático mostrando em quais dias alguém está escalado
def definir_caledanrio_plantao(total_dias, intervalo_escala):

    if intervalo_escala <= 0:
        print(" Intervalo de escala inválido (deve ser maior que 0)! ")
        return

    print(f" -- ESCALA DE SOBREAVISO: Próximos {total_dias} dias -- ")

    # Comece po 1 e vá até o total de dias escalados
    # (lembre-se: precisamos do +1 para contemplar todos os dias)
    # O range vai pular no intervalo definido
    for dia in range(1, total_dias + 1, intervalo_escala):
        print(f" Dia {dia}: Médico Plantonista escalado! \n")


# Ex. total_dias=15, intervalo=3 => range(1, 16, 3)
# # Gera: 1, 4, 7, 10, 13
