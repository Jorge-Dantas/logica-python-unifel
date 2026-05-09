# Simular um sistema que controla o acesso/clima de um evento da UNIFEL
# Caso 1: VALIDAÇÃO COM IN
convidados = ["jorge", "genaldo", "ewerton", "denise", "falcao", "milena"]
usuario = input(" Digite seu nome: ").lower()

if usuario in convidados:
    print(" LIBERADO! Seja bem-vindo ao evento!")

    # Aninhamento (um if dentro de outro)
    idade = int(input(" Qual sua idade? "))
    if idade >= 18:
        print("Você recebeu uma pulseira da área VIP! \n")
    else:
        print("Você recebeu uma pulseira da área KIDS (infantil)! \n")

else:
    print("ACESSO NEGADO. Seu nome não consta na lista. Procure a rececpção!")
print("-" * 30)


# Caso 2 -> Classificação do clima do evento
print("\n" * 1)
temp = float(input("Digite a temperatura atual da sala: "))
status = None

if temp > 35:
    status = "Calor extremo no salão"
elif 25 <= temp <= 35:  # Encadeamento lógico -> temp >= 25 and temp <= 35
    status = "Suportável"
elif 17 <= temp <= 24:
    status = "Agradável"
else:
    status = "Muito Frio"  # 16 pra baixo
    print(f"A temperatura está: {temp} (16 ou abaixo)!! \n")

# print(f"O clima está: {status} ({temp}º)!! \n")


"""
Comentário de múltiplas linhas
"""

# Comentário de uma linha


# CASO 3: Menu de comandos da gestão do evento
opcao = input("Escolha uma opção: A (Relatório) | B (Saldo) | C (Sair): ").upper()

match opcao:
    case "A":
        print("Gerando relatório detalhado do evento... \n")
    case "B":
        print("Calculando a receita consolidada atual do evento... \n")
    case "C":
        print("Saindo do sistema... Até logo! \n")


# QUIZ: O Arquiteto de Fluxos
# Qual a função da identação no if?

# O que acontece se o if for False e não houver um else?

# Para que serve o operador in dentro de um if?

# Se eu tiver 3 elif e o primeiro for verdadeiro,
# o Python avalia os outros dois?

# Qual a diferença entre
# if usuario == "admin" e if "admin" in lista_usuarios?

# O que o símbolo _ (underscore) faz no match-case?

# Posso colocar um if dentro de outro if? Como se chama isso?

# Os elif / else é obrigatório em toda estrutura de decisão?

# Qual a diferença entre == e is?

# Se x = 10, qual o resultado de: if x > 5 and x < 15:?
