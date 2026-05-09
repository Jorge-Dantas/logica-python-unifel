#  Simulador de ATM (Caixa Eletrônico): Peça um valor de saque.
# Verifique se o valor é múltiplo de 10 (operador).
# Se for, use a estrutura apropriada para simular a entrega de notas; se não for,
# avise que a máquina só possui notas de 10, 20 e 50.
# OBS: Emitir o aviso "Saque de alto valor: Verifique o limite diário."
# caso o saque seja MAIOR QUE 500.
# OBS 2: Tem que tratar as notas (10, 20, 50) com MATCH-CASE
valor_saque = int(input("Quanto vai sacar?? (notas de 10, 20 e 50): "))

if valor_saque > 0 and valor_saque % 10 == 0:  # O valor é múltiplo de 10?

    # Decomposição
    # Ex: 130
    # D1 = 130 / 50 = 2
    # Resto D1 = 30
    # D2 = 30 / 20 = 1
    # Resto D2 = 10
    notas_50 = valor_saque // 50  # Quebrando o valor em 50
    resto = valor_saque % 50  # Pegando o resto da divisão acima

    notas_20 = resto // 20  # Quebrando o resto da divisão acima em 20
    resto = resto % 20  # Pegando o resto da divisão acima

    notas_10 = resto // 10  # Quebrando o valor em 50

    print(f"\n Saque autorizado | Valor de: R$ {valor_saque} \n")

    match valor_saque:

        case 10 | 20 | 50:
            print(f" Saque simples: Entregando 1 nota de R$ {valor_saque}")

        case _ if valor_saque > 500:
            print(f"\n Saque de alto valor: Verifique o limite diário \n")

            # Impressões com a decomposição
            if notas_50:  # Truthy / Falsy
                print(f" - {notas_50} notas(s) de R$ 50,00 \n")
            if notas_20:
                print(f" - {notas_20} notas(s) de R$ 20,00 \n")
            if notas_10:
                print(f" - {notas_10} notas(s) de R$ 10,00 \n")

        case _:
            # Impressões com a decomposição
            if notas_50:  # Truthy / Falsy
                print(f" - {notas_50} notas(s) de R$ 50,00 ")
            if notas_20:
                print(f" - {notas_20} notas(s) de R$ 20,00 ")
            if notas_10:
                print(f" - {notas_10} notas(s) de R$ 10,00 \n")
else:
    print(" [ERRO]: Valor inválido!")
    print(" Este caixa só trabalha com notas de 10,00 | 20,00 | 50,00 \n")
    print(" Ou você digitou um valor negativo ou zerado. Tente novamente !! \n")

print("-" * 30)
print("\n\n")

# PARTE 1: Raciocínio Lógico)
# 1. A Ordem dos Fatores: Explique por que, em um sistema de faixas de desconto,
# começar a verificação por if valor > 100: antes de if valor > 1000:
# pode ser considerado um "bug lógico".
# Nesse contexto, qual a regra de ouro para a ordem dos elif?

# 2. Anatomia do ATM: No exercício do caixa eletrônico, utilizamos a combinação de
# // e % antes do match-case.
# Explique qual a função de cada um desses operadores na preparação dos dados
# para que o match possa exibir as notas corretamente.

# 4. Aninhamento vs. Conjunção: Em termos de experiência do usuário (UX),
# por que usar if idade >= 18: seguido de um if possui_ingresso:
# interno é mais vantajoso do que usar uma única linha com
# if idade >= 18 and possui_ingresso:?

# 5. Curto-Circuito Estratégico:
# Analise o código if usuario_ativo and validar_token_no_servidor():.
# Como o Python utiliza o conceito de curto-circuito para economizar
# recursos de rede (internet) nessa linha específica?

# 6. Boas Práticas Profissionais: Por que um desenvolvedor sênior prefere
# escrever if not ativo: em vez de if ativo == False:?
# Explique o conceito envolvido.


# 7. O Operador Ternário: Converta a estrutura abaixo para
# uma única linha de código (Operadores Lógicos), mantendo a mesma lógica:

# if saldo >= valor_saque:
#     status = "Autorizado"
# else:
#     status = "Saldo Insuficiente"

# status = saldo >= valor_saque and "Autorizado" or "Saldo Insuficiente"


# 8. Analise o match-case abaixo e indique o resultado para v = 50:

# match v:
#     case 10 | 20: print("A")
#     case 50: print("B")
#     case _ if v > 40: print("C")
#     case _: print("D")

# a) B e C
# b) D
# c) C
# d) B


# 9. Sobre o operador de pertencimento in, qual o resultado de if "10" in [10, 20, 30]:?

# a) True
# b) False
# c) Error
# d) Converte "10" para int e retorna True.


# 10. Qual a saída do código abaixo considerando pontos = 0?

# status = "Iniciante"
# if pontos:
#     status = "Veterano"
# print(status)

# a) Iniciante
# b) Veterano
# c) True
# d) None


# 11. Qual a diferença entre == e is na avaliação de uma condição?
# a) == checa se os nomes são iguais; is checa se o valor é igual.
# b) == checa o conteúdo; is vê se os objetos tem o mesmo endereço (MEMÓRIA).
# c) is é uma versão mais rápida do == usada apenas para números int e float.
# d) == é para if e is é exclusivo para match-case e strings.

# HEAP X STACK
# == COMPARA CONTEÚDO (VALOR) *HEAP
# IS = COMPARA IDENTIDADE (ENDEREÇO) * PARA ONDE A STACK APONTA?


# 12. No match-case, se quisermos que um case aceite qualquer valor entre
# 100 e 200, como devemos escrever?
# a) case _ 100-200:
# b) case _ : range(100, 200)
# c) case _ if 100 <= valor <= 200:
# d) case _ if: valor > 100 and valor < 200


# 13. O que acontece se houver um erro de identação dentro de um elif?
# a) O Python ignora o erro e executa o else.
# b) O programa roda, mas o resultado será imprevisível.
# c) O Python interrompe a execução com um IndentationError.
# d) O if pai assume o controle da linha desalinhada.


# 14. Analise a expressão: print(True or print("Erro") and False). O que será exibido?
# a) Erro
# b) True
# c) False
# d) True e Erro
# print(True or print("Erro") and False)
# print     (True or          (print("Erro") and False)               )


# 15. If ternário (moderno): Qual o resultado final da variável res após:
# res = "Acesso" if 10 > 5 else 0 or "Negado"?

# a) Acesso
# b) 0
# c) Negado
# d) True


# E se fosse assim?
# res = "Acesso" if 10 < 5 else 0 or "Negado"
# res = "Negado"
