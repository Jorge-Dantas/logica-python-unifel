print("\n")
print("-" * 30)


def decompor_nome(nome_completo):
    partes = nome_completo.split()
    return (
        partes[0],
        partes[-1],
    )  # Retorna dois valores, sendo -1 o último elemento da coleção


primeiro, ultimo = decompor_nome(
    "Abacate Jorge Alex Pereira dos Santos da Silva Dantas Unifel"
)


print(f"\n Imprimindo elementos decompostos: {primeiro, ultimo}\n")  # Abacate Unifel"

print("-" * 30)
print("\n")


# Ex. Typing Hints: Uma função que retorna o valor final de um rendimento de juros compostos
def calcular_rendimento(valor: float, meses: int) -> float:
    return valor * (
        1.01**meses
    )  # Aplico 1% ao mês no valor informado |> **  é exponenciação


# OBS: Isso não calcula o LUCRO REAL, isso calcula o MONTANTE apenas!

# TYPE HINTS:
# 1. Legibilidade (código fácil de entender)
# 2. Ajuda o dev (ou equipe de devs)
# 3. Ajuda as ferramentas a nos ajudar (VS CODE, mypy, etc)

# NÃO SERVE PARA IMPEDIR ERROS NO RUNTIME


# IMPLEMENTANDO quantidades indefinidas de parâmetros/argumentos com *args
# Ex de função que soma valores de vendas acumulando o total (não precisamos saber a quantidade de valores)
def somar_vendas(*valores: float) -> float:
    total = 0
    for v in valores:
        total += v  # total = total + v
    return total


print(somar_vendas(150.50, 200.0, 50.25))  # Passando 3 parâmetros
print(somar_vendas(10.0, 20.0))  # Passando 2 apenas, funciona igual!
print("\n\n\n")

# FUNÇÕES LAMBDA (expressões Lambda)
# Ex. uma função que calcula o dobro de um número

# Pegue o número
# Multiplique o número por 2
# Devolva o resultado (return num * 2)


# Com def tradicional
def dobro(num):
    return num * 2


print(f" O dobro de 2 é: {dobro(2)}")  # 4

# Versão com LAMBDA (funções anônimas)
calcular_dobro = lambda num: num * 2

meu_numero = 5000  # "Usuário que digitou..."
print(f" O dobro de 5000 é: {calcular_dobro(meu_numero)} \n")  # 10000


# Lógica simples, porém robusta, com Lambda (já começa a ficar feio):
soma_ou_dobro = lambda numero: numero * 2 if numero > 10 else numero + 5

num = 15
print(f" {num} x 2 = {soma_ou_dobro(num)} \n")  # Tem que dar 30

num = 10
print(f" {num} + 5 = {soma_ou_dobro(num)} \n")  # Tem que dar 15
