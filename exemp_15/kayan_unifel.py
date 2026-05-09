from datetime import datetime
import random

# dict => dicionário!!
contas = {
    "12345": {"senha": "1234", "nome": "Kaian", "saldo": 1250.00},  # uma conta
    "12375": {"senha": "4353", "nome": "Jorge", "saldo": 58250.00},  # OUTRA conta
}

NOTAS = [50, 20, 10]  # Constantes numa lista
LIMITE = 500  # Limite para o aviso do programa
conta = None  # Cria uma conta VAZIA!


def linha():
    print("-" * 40)


def login():
    global conta
    linha()
    print("  ATM SIMULATOR".center(40))
    linha()
    numero = input("  Conta : ")
    senha = input("  Senha : ")

    if numero in contas and contas[numero]["senha"] == senha:
        conta = contas[numero]
        print(f"\n  Bem-vindo, {conta['nome']}!")
    else:
        print("\n  Conta ou senha incorretos.")
        exit()


def calcular_notas(valor):
    resto, resultado = valor, {}
    for nota in NOTAS:
        qtd = resto // nota
        resto %= nota
        if qtd > 0:
            resultado[nota] = qtd
    return resultado


def sacar(valor):
    if valor > conta["saldo"]:
        print("  Saldo insuficiente.")
        return
    if valor > LIMITE:
        print(f"  Aviso: limite diario e R$ {LIMITE:.2f}.")

    notas = calcular_notas(valor)
    saldo_anterior = conta["saldo"]
    conta["saldo"] -= valor

    linha()
    print(f"  Saque de R$ {valor:.2f} aprovado!")
    print(f"  Cedulas: ", end="")
    print("  |  ".join(f"R${n},00 x{q}" for n, q in notas.items()))
    linha()
    print(f"  Saldo anterior : R$ {saldo_anterior:.2f}")
    print(f"  Saldo atual    : R$ {conta['saldo']:.2f}")
    print(f"  Data           : {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"  Codigo         : ATM-{random.randint(10000,99999)}")
    linha()


login()

linha()
print(f"  Saldo: R$ {conta['saldo']:.2f}")
linha()

try:
    valor = int(input("  Valor do saque: R$ "))
    if valor <= 0:
        print("  Valor invalido.")
    elif valor % 10 != 0:
        print("  So notas de R$10, R$20 e R$50.")
    else:
        sacar(valor)
except ValueError:
    print("  Digite apenas numeros.")

print("\n  Obrigado!".center(40))
linha()
