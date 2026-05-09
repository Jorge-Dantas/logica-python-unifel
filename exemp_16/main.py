import random

print()
print("-" * 30)

# SINTAXE (anatomalia)
# while condicao:
#     # código do while
# Condição de parada

# temperatura = 80


# def processar_dados():
#     print("Processando dados...")
#     print("Temperatura atual:", temperatura)
#     print("Dados processados com sucesso!")


# def ler_sensor():
#     return random.randint(15, 40)


# # Se temperatura for MENOR que 20, o While NEM EXECUTA!
# while temperatura > 20:
#     processar_dados()
#     print("")
# temperatura = ler_sensor()  # Condição de parada (quando random gerar um valor menor que 20)

# PERGUNTE PRIMEIRO, DEPOIS EXECUTE

# print()
# print("-" * 30)
# print()

# WHILE NO C# (para entendimento do DO.. WHILE)
# while (temperatura > 20){
#     processar_dados();
#     temperatura = ler_sensor();
# }

# PELO MENOS UMA VEZ, O DO WHILE RODA.
# do {
#     processar_dados();
#     temperatura = ler_sensor();
# } while (temperatura > 20);


# SIMULANDO UM DO... WHILE NO PYTHON
# Garantindo que rode PELO MENOS UMA VEZ..
# while True:
#     num = int(input("Digite um número maior que 0: "))

#     # Garantia de parada (condição de parada)
#     if num > 10:
#         print("\n LIMITE MÁXIMO ATINGIDO. Abortando o programa.... \n")
#         break  # INTERROMPE O LAÇO (ACABA O LAÇO)

# EXECUTE PRIMEIRO, DEPOIS PERGUNTE


# print()
# print("-" * 30)
# print()


# FOR + RANGE

# range(start, end, step)

# 1 - range(end)
# 2 - range(start,end)
# 3 - range(start, end, step)
# for mes in range(1, 13, 2):
#     print(f"\n --- Relatório do mês de {mes}")


# print(f"\n Variável mês: {mes} \n")  # 12


# print()
# print("-" * 30)
# print()

# For em um iterável real (literal)
# nomes = ["Monique", "Marlin", "André"]  # lista (strings)

# for nome in nomes:
#     print(f"Seja bem-vindo(a), {nome}!")


print()
print("-" * 30)
print()

# for de strings
# for letra in "Curso de Python com Jorge Dantas":
#     print(letra, end="")


print()
print("-" * 30)
print()


# Isso é um dict (dicionário) => conjunto de PARES "chave-valor"
# usuario = {" Nome": "Jorge", " Saldo Atual": 15.599}
# print("\n Dados da conta: ")

# for chave, valor in usuario.items():
#     print(f"{chave}: {valor}")


print()
print("-" * 30)
print()


# for com else (pouco conhecido)
# for num in range(11):

#     print(f"Número do range atual: {num}")

#     if num == 10:
#         print("\n O número 10 foi alcançado! \n")
#         break  # O FOR É INTERROMPIDO (inclusive o else pertencente a ele)!!

# else:
#     print(" O número 10 nunca foi alcançado! \n")

# O else só roda se o for for executado por completo (sem interrupção do break)

print()
print("-" * 30)
print()

# Outro de for com else (2.0)
# ÍNDICES SEMPRE COMEÇAM EM 0!
# João = 0, Grasi = 1, Alana = 2, Vanessa = 3
# users = ["João", "Grasi", "Alana", "Vanessa"]

# print(f"O item 0 da lista é o {users[0]}!! \n\n")

# for nome in users:

#     if nome == "Wanessa":  # Vanessa
#         print(" [ACHEII] ")
#         print(f" {nome}, seja muito bem-vinda! \n")
#         break
# else:
#     print(" Wanessa não encontrada =( \n")


print()
print("-" * 30)
print()

# for aninhados (um for dentro do outro)
# for linha in range(3):
#     for colunas in range(5):
#         print(f"{linha} | {colunas}")

# 0 0
# 0 1
# 0 2
# 0 3
# 0 4

# 1 0
# 1 1
# 1 2
# 1 3
# 1 4

# 2 0
# 2 1
# 2 2
# 2 3
# 2 4

print()
print("-" * 30)
print()


# List COMPREHENSION
# pares = [num for num in range(1, 11) if num % 2 == 0]

# Versão TRADICIONAL
# pares = []

# for num in range(1, 11):
#     if num % 2 == 0:  # Se true, o número é PAR!
#         pares.append(num)  # Adicione o número na minha lista!

# print(f" Números pares até 10: {pares}")


print()
print("-" * 30)
print()

# Range NEGATIVO
# for num in range(10, -1, -1):
#     print(num, end=" ")


print()
print("-" * 30)
print()

# PYTHON SEPAROU O ÍNDICE EM 2 (INTELIGENTEMENTE)
# A. Índice técnico (interno) = sempre começa em 0!
# B. Índice exibição (para nós humanos) = começa onde quisermos!!

# SINTÁXE:
# enumerate(iterável, valor_inicial_indice_exibido)

# lista = ["Python", "SQL", "Excel"]

# for i, item in enumerate(lista, start=1):
#     print(f"Lugar {i}: {item}")

# O enumarate RETORNA UMA TUPLA (índice, elemento)

# i = índice (valor dele)
# item = elemento (valor dele)

# enumerate(lista, start=1) retorna:
# (0, "Python")
# (1, "SQL")
# (2, "Excel")

# Na prática, isso que acontece (o for DESENPACOTAMENTO):
# i =1, item = "Python"
# i =2, item = "SQL"
# i =3, item = "Excel"


# Graças ao enumerate, não precisamos fazer isso (índica manual):
# for i in range(len(lista)):


"""
SÓ PARA CONHECIMENTO, COMO SERIA ISSO EM C#:
string[] lista = {"Python", "SQL", "Excel"};

for (int i = 0; i < lista.Length; i++){
    Console.WriteLine($"Lugar: {i + 1}: {lista[i]}");
}

"""

print()
print("-" * 30)
print()

print("FOR COM BREAK E CONTINUE")
for n in range(10):
    if n == 5:
        break  # Para tudo no 5

    if n % 2 == 0:
        continue  # Pula os pares
    print(n)

print(f" Imprimindo n fora do for: {n}")

# Em Python, não existe escopo de bloco para loops
# e condicionais (variáveis não morrem).

# APENAS CLASSES E FUNÇÕES CRIAM ESCOPO (variáveis morrem)

print()
print("-" * 30)
print()
