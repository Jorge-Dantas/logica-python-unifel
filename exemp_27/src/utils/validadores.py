def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("[X]: Digite um valor decimal válido! ")


def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("[X]: Digite um valor inteiro válido! ")
