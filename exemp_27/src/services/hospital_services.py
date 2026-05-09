from src.utils.validadores import ler_float, ler_int
import os


# TRIAGEM HOSPITALAR
def processar_triagem(lista_paciente, id_paciente):

    # Guard clause -> Trata se a lista ta vazia logo no início e saí da função nesse ponto exato
    if not lista_paciente:
        print("[X] Lista de pacientes vazia! \n")
        return

    # try:
    paciente = lista_paciente[id_paciente]  # Pega o nome do paciente pelo ID

    # Aproveitando funções previamente construídas
    peso = ler_float(f"Peso do(a) {paciente}:")
    jejum = ler_int(f" O tempo de jejum (hs) do paciente {paciente}: ")

    # Calcula a dosagem proporcional (ex. 100 / 8 = 12.5)
    # Se jejum for 0, o erro ZeroDivisionError acontece aqui!
    dosagem = 100 / jejum

    # Gera uma string formada com os dados coletados/processados
    identificacao = (
        f"Paciente: {paciente}"
        | f"Peso: {peso}"
        | f"Dose recomendada: {dosagem:.2f} \n"
    )

    # Manda criar pasta logs/. Se já existir, pula e não faz nada
    # Sem o exist_ok=True, se logs/ já existisse, teríamos: FileExistsError❌
    os.makedirs("logs", exist_ok=True)

    # Mostra onde a pasta será criada
    print("Diretório atual (onde será criada a pasta):", os.getcwd())

    # Definindo o lugar: pasta logs, arquivo registro.txt
    # Modo "a" = append, ou seja, adiciona os dados acima ao final do arquivo (se não existir, CRIA)
    # utf-8 permite acentos e caracteres especiais (ç, ã, é...)
    with open("logs/registro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            identificacao
        )  # Escreva os dados no arquivo (como um save no BD)!


# except:
