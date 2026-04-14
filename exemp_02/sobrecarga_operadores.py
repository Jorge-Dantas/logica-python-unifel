# SOBRECARGA DE OPERADORES
# +
# ==
# *

# Misturas controladas
print(int("10") + 5)  # OK: 15 (o 10 se transformou em int)
print(str(10) + "5")  # OK: "105" (O 10 INT foi convertido para texto)

# Repetição
print("A" * 3)  # OK: "AAA" (o operador * repete quando é string)

minha_lista = [1, 2]  # NOVO CONCEITO: LISTA!!
print(minha_lista * 3)  # OK: [1,2,1,2,1,2] (o conteúdo da lista se repetiu 3 x)
print([1, 2] * 3)  # OK: [1,2,1,2,1,2] (o conteúdo da lista se repetiu 3 x)

minha_tupla = (3, 4)  # NOVO CONCEITO: TUPLA!!
print(minha_tupla * 3)  # OK: (3,4,3,4,3,4) (o conteúdo da tupla se repetiu 3 x)
print((10, 20) * 2)  # OK: (3,4,3,4,3,4) (o conteúdo da tupla se repetiu 3 x)


# Pertencimento
print("a" in "banana")  # OK: TRUE => in: ver se algum item está dentro do objeto
print(4 in [4, 5, 6, 7])  # OK: TRUE => in: ver se algum item está dentro do objeto


# print("abacate" * 2.5)  # ERRO! Só funciona com inteiro (string x int)
# print("jorge" - "jor")  # ERRO! Não existe subtração de string


# QUIZ: O Mestre da Sobrecarga e Precisão
# Pergunta 1: Por que print(0.6 + 0.3 == 0.9) resulta em False no Python?
# a) Devido à imprecisão do float binário (o resultado real é 0.8999_mais_alguma_coisa).
# b) Porque o Python errou a conta.
# c) Porque você esqueceu de usar parênteses.
# d) Porque 0.9 é um número inteiro para o Python.

# Pergunta 2: O que acontece se eu rodar print("Cuidado" * 0)?
# a) Imprime "Cuidado".
# b) Dá um erro de valor.
# c) Imprime uma string vazia.
# d) Imprime o número 0.

# Pergunta 3: Qual o resultado de print("5" == 5)?
# a) True, porque o valor é o mesmo.
# b) False, Python é fortemente tipado (String nunca é igual a um Int).
# c) TypeError.
# d) 55.

# Pergunta 4: Por que print("abc" * 2.5) gera um erro?
# a) Porque Strings só podem ser multiplicadas por Floats.
# b) Porque o Python não aceita números decimais em prints.
# c) Porque o resultado seria muito grande para a memória.
# d) Porque a sobrecarga de * p/ Strings exige multiplicador Int (discreto).


# Pergunta 5: Analise o código: x = [1, 2] e y = x + [3]. Qual o valor de y?
# a) [1, 2, 3] (O + em listas = junção/concatenação).
# b) [1, 2, [3]] pois o [3] foi agregado a uma lista já existente.
# c) TypeError: essa operação não pode existir em listas.
# d) [6], pois 3 * 2 = 6, e 6 * 1 = 6 mesmo.

# x = [1, 2]
# print(x)
# y = x + 3  # Erro! O operador de soma não pode adicinar um int numa lista.
# y = x + [3]  # OK! O operador de soma em listas é a concatenação, ou seja, juntar os itens.
# print(y)


def minha_funcao():
    print("\n\n\n")
    print("Olá, sou uma função!")
    idade = 37  # ISSO AQUI É UM HÓSPEDE DO QUARTO, SÓ EXISTE DENTRO DA FUNÇÃO!!
    print(f"A minha idade é: {idade}")


print(minha_funcao())  # ERRO: Idade não existe fora da função!!


# REFERÊNCIA DE MEMÓRIA NO PYTHON
a = 10  # Objeto a aponta (ponteiro) => objeto 10
b = 30  # Objeto b aponta (ponteiro) => objeto 30

a = b  # Agora b tem o mesmo ponteiro de a, que aponta para o objeto que guarda o valor 30.
b = 40  # Agora b tem um novo ponteiro, ele aponta para o objeto que guarda 40 agora.

print(f"Aqui é a: {a}")  # Vai imprimir 30
print(f"Aqui é b: {b}")  # Vai imprimir 40
