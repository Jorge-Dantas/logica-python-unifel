import copy

# Imutáveis (SEGURO)
x = 10
y = x  # y é 10
x = 20


# Mutáveis
lista_a = [1, 2, 3]
lista_b = lista_a  # as duas listas apontam para o mesmo objeto
lista_a.append(4)  # Isso vai adicionar o número 4 a lista

# Mútáveis, veja como funcionam!!
print("\n Mutáveis:")
print(f"LISTA A: {lista_a} | LISTA B: {lista_b}")
print("\n\n")
# EFEITO ESPELHO!!

# Verificando o endereço de memória dos objetos (HEAP)
print(f" ID da lista A: {id(lista_a)} |  ID da lista B: {id(lista_b)}")
print("\n\n")

# Copiar sem criar um novo objeto (Cópia rasa). Isso cria um novo objeto.
lista_b = lista_a.copy()


# PEGADINHA
print("\n\n")
lista_1 = [[1, 2], [3, 4]]
lista_2 = lista_1.copy()

print(f" Conteúdo da lista 1: {lista_1} |  ID da lista 2: {lista_2}")
print("\n\n")

lista_1[0][0] = 999
print(f"LISTA 1: {lista_1}\n\n")

# 999, 2, 3, 4
# ALTEROU O ORIGINAL, NÃO CRIOU CÓPIA!!

# Cópia profunda:
lista_2 = copy.deepcop(lista_1)


# Pergunta 1: Eu tenho a = [1, 2] e b = a. Se eu fizer a = [1, 2, 3], o que acontece com b?
# a) b vira [1, 2, 3] pelo Efeito Espelho.
# b) O Python dá um erro de "Duplicate Reference".
# c) b continua sendo [1, 2].
# d) a e b passam a apontar para o mesmo endereço novo.


# Pergunta 2: Analise o código: x = "Python", y = "Python".
# O Python percebe que o conteúdo é igual e pode fazer ambos apontarem para
# o mesmo ID para economizar memória (Interning).
# Se eu fizer x = x + "3", o que acontece com o ID de x?

# a) O ID permanece o mesmo, pois strings são otimizadas.
# b) O Python apaga o objeto "Python" original.
# c) O ID de y muda junto.
# d) O ID muda, pois strings são imutáveis e qualquer alteração gera um novo objeto.


# Pergunta 3: Qual a diferença fundamental entre lista_b = lista_a e lista_b = lista_a.copy() na memória?
# a) Nenhuma, o resultado final no print é igual.
# b) Na primeira, o ID muda; na segunda, o ID é o mesmo.
# c) Na primeira, temos duas etiquetas para um objeto.
# Na segunda, temos dois objetos diferentes com o mesmo conteúdo.
# d) O .copy() só funciona para números inteiros.


# Pergunta 4: Se as Tuplas são imutáveis, o que acontece se eu tentar
# fazer minha_tupla.append(10)?
# a) O Python cria uma nova tupla com o 10.
# b) O Python converte a tupla em lista automaticamente.
# c) Erro (AttributeError): O objeto tupla sequer possui o método append.
# d) A tupla aceita o valor, mas não muda o seu ID.


# Pergunta 5: Por que entender o Garbage Collector é vital ao trabalhar com listas imensas?
# a) Para saber quando o Git vai apagar seu código.
# b) Para entender que, se você criar muitas referências (a=b, c=b, d=b),
# o objeto nunca será limpo da RAM, podendo causar lentidão.
# c) Porque o Garbage Collector converte globais em locais.
# d) Porque ele é o responsável por fazer o copy() das variáveis.


# Pergunta 6: Qual a saída deste código?

# a = [1, 2]
# b = a.copy()
# a.append(3)
# print(b)

# a) [1, 2, 3] (Efeito espelho: b acompanha mudanças em a)
# b) [1, 2] (b é uma cópia independente feita antes da alteração)
# c) [1, 2, [3]] (o append cria uma sublista dentro de b)
# d) Erro (AttributeError: copy não funciona com listas simples)
