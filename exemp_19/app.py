# Estrutura básica
# try:
#     codigo_arriscado()
# except:
#     tratar_erro()

# Primeiro caso (exemplo 1)
# try:
#     numero = int(input("\n Digite o Número: "))
# except ValueError:
#     print("\n ❌Erro: Digite apenas números inteiros!")
# else:
#     print(f"\n ✅Sucesso! O número é {numero}")
# finally:
#     print(
#         "\n 🚀🎉Operação finalizada.\n\n"
#     )  # Independente de ser erro ou não acima, ele roda!!


# TRY      → tenta executar (mas pode dar erro)
# EXCEPT   → se o TRY falhar
# ELSE     → se o TRY deu certo (se não entrou no Except)
# FINALLY  → sempre executa (independente da condição)


# Quando (em que casos) usar o Try.. Excepty??
# Em operações que uma falha pode fugir do seu controle, como:
# ✅ entradas de teclado
# ✅ conexões de rede
# ✅ arquivos (TAMBÉM BD)
# ✅ parse JSON
# ✅ conversão numérica
# ✅ bibliotecas externas
# ✅ ORM/database
# ✅ APIs internas/externas


# ------------------

# FUNÇÕES (introdução)
# Anatomia de FUNÇÃO no Python (def)

# 1. Uma função é um bloco de código NOMEADO que realiza uma tarefa ESPECÍFICA.
# 2. Em Python, seguimos regras rígidas para garantir a legibilidade e obedecer a sintaxe.


# Regras e Sintaxe:
# a. Palavra-chave def => Inicia a declaração.

# b. Nome da Função => Deve ser em snake_case (letras minúsculas e sublinhados).

# c. Parâmetros => Valores que você pode passar para a função (ela recebe e usa dentro do bloco).
# -> Podem ser obrigatórios ou ter valores padrão (default).
# Os parâmetros são passados dentro dos parênteses ().

# d. Dois-pontos(:) => Obrigatórios após os parênteses,
# define o início do bloco da função (igual for, if, while...)

# e. return: Envia o resultado de volta para quem chamou a função.
# Se omitido, a função retorna None (void de outras linguagens como C#).

# ------------------


# Este exemplo integra os 5 erros em um fluxo lógico de processamento de dados médicos.
# Exemplo Real: Sistema de Triagem Hospitalar

# lista1 = []
# processar_triagem(lista1, 1) # Isso gera erro no Python (usando algo que ainda não foi definido!)

print("-" * 30)
print(" Sistema de Triagem Hospitalar")
print("-" * 30)
print()


def processar_triagem(lista_pacientes, id_paciente):

    try:
        # 1. IndexError: Tentar acessar um paciente que não está na lista
        paciente = lista_pacientes[id_paciente]

        # 2. ValueError: Tentar converter um peso mal digitado (ex: "70kg")
        peso = float(input(f"Peso do(a) {paciente} (apenas números): "))

        # 3. TypeError: Tentar somar a string do nome com o número do peso
        # print(
        #     paciente + peso
        # )  # Descomentar no teste 3. Vai gerar o erro de Type no Python (string + float)!
        identificacao = f"Paciente: {paciente} | Peso: {peso}kg"  # Comentar no teste 3, pois não gera o erro!

        # 4. ZeroDivisionError: Cálculo de dose se o tempo de jejum for 0
        jejum = int(input("Horas de jejum: "))
        dosagem = 100 / jejum

        # 5. FileNotFoundError: Tentar salvar o log em um arquivo inexistente/inacessível
        with open("Z:/hospital_logs/registro.txt", "a") as arquivo:
            arquivo.write(identificacao)

    except IndexError:
        print("\n ❌ Erro: ID do paciente inválido na base.")
    except ValueError:
        print("\n ❌ Erro: Peso deve conter apenas números decimais.")
    except TypeError:
        print("\n ❌ Erro: Falha interna ao processar tipos de dados.")
    except ZeroDivisionError:
        print(
            f"\n ❌ Erro: A dosagem é inválida, o jejum não pode ser {jejum} para este cálculo."
        )
    except FileNotFoundError:
        print("\n ❌ Erro: Servidor de arquivos inacessível.")


# ==========================================
# TESTES FORÇANDO CADA ERRO
# ==========================================

pacientes = ["Ana", "Bruno", "Carlos", "Monique", "Unifel"]

print("========== TESTE 1 - INDEXERROR ==========")
processar_triagem(
    pacientes, 10
)  # Se o paciente for i(10), não existe, temos apenas 4 -> ERRO!


print("\n========== TESTE 2 - VALUEERROR ==========")
# No peso da Ana, vamos digitar: 70kg. O código espera 70, e não o texto 70kg -> ERRO!
processar_triagem(pacientes, 0)


print("\n========== TESTE 3 - TYPEERROR ==========")
# Aqui vamos dar um peso válido para o Bruno: 70. Volte na função descomente a linha da soma (+)
# Ela vai tentar paciente + peso, o que seria "Bruno" + 85 -> ERRO!
processar_triagem(pacientes, 1)


# Antes de rodar o teste 4 e 5, volte a comentar a linha do erro acima (soma +)


print("\n========== TESTE 4 - ZERODIVISIONERROR ==========")
# Use:
# peso = 70
# depois digite jejum = 0
# Python vai fazer 100 / 0, divisão por 0 -> ERRO!
processar_triagem(pacientes, 2)


print("\n========== TESTE 5 - FILENOTFOUNDERROR ==========")
# Para rodar, informe jejum do teste acima diferente de zero
# Se não existir drive Z: ou pasta hospital_logs -> ERRO!
processar_triagem(pacientes, 0)


# Exemplo: Em vez de mostrar
# FileNotFoundError: [Errno 2] No such file,
# você mostra
# ❌ Erro: Servidor de arquivos inacessível.


# Observe esse trecho:
# apelido = ""
# nome = ""
# usuario = apelido or nome or "Anônimo"

# # Tenta pegar o apelido, se não tiver, pega o nome. Se não tiver nome, usa "Anônimo"
# # Se 'apelido' for uma string vazia (""), o Python pula para o próximo, o que pode ser um erro.


# # Como seria o Bom (Legível e Explícito):
# if apelido:
#     usuario = apelido
# elif nome:
#     usuario = nome
# else:
#     usuario = "Anônimo"
