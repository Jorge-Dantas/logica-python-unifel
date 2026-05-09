# Analisador de Triângulos: Receba três lados (A, B e C) de um possível triângulo.
# Determine se eles podem formar um triângulo e, em caso positivo,
# defina a sua classificação (se ele é Equilátero, Isósceles ou Escaleno).

# Regra de Existência: Um triângulo só existe se a soma de dois lados for SEMPRE maior
# que o terceiro lado (independente de quais lados estamos verificando).
# Se (e somente se) o triângulo existir, classificar o tipo com base na igualdade dos lados.
# Equilátero: Todos os 3 lados são iguais.
# Isósceles: Apenas 2 lados são iguais.
# Escaleno: Todos os 3 lados são diferentes.

# OBS: Lados de um triângulo jamais podem ser 0 ou números negativos!!!
print("-" * 30)
print(f"{'ANALISADOR DE TRIÂNGULOS':^30}")
print("-" * 30)

a = float(input("Digite o Lado A: "))
b = float(input("Digite o Lado B: "))
c = float(input("Digite o Lado C: "))

# Um lado de triângulo NÃO PODE SER 0 ou negativo
if a > 0 and b > 0 and c > 0:

    if (a + b >= c) and (a + c >= b) and (b + c >= a):
        print(" Este triângulo é válido! Classificação: ", end="")
        # PRINT() => \\ O fim de todo print() é um "\n". O end="" tira essa quebra de linha!

        if a == b == c:  # a == b and b == c
            print("Seu triângulo é EQUILÁTERO")
        elif a == b or a == c or b == c:
            print("Seu triângulo é ISÓCELES")
        else:
            print("Seu triângulo é ESCALENO!")

    else:
        print("Os lados informados não podem gerar um triângulo!!")
        print(
            "MOTIVO: Um dos lados informados é maior que a soma dos outros dois lados! \n\n"
        )

else:
    print("ERRO: Não existem triângulos com lados nulos ou negativos!! \n")

print("-" * 30)
