# exemp_11: A Herança Dividida (Divisão e Resto Real)
# Cenário: Um investidor deixou 1.000 barras de ouro para 7 herdeiros.
# O que não puder ser dividido igualmente (a sobra) deve ser doado para um museu.
# Objetivo: Calcule quantas barras cada herdeiro recebe e quantas barras serão doadas.
print("\n" * 1)
print("-" * 30)

# Saída esperada: "Herdeiros: X barras cada. Museu: Y barras."
total_barras = 1000
herdeiros = 7

# Quanto cada herdeiro recebe
barra_por_herdeiro = total_barras // herdeiros

# Sobra do museu
doacao_museu = total_barras % herdeiros

print("PARTILHA: \n")
print(f"HERDEIROS: {barra_por_herdeiro} barras para cada! \n")
print(f"MUSEU (doação): {doacao_museu} barras!")
print("-" * 30)
print("\n" * 2)


# _____________________________________
print("-" * 30)
print("10" == 10)  # FALSE
print(10 == 10)  # TRUE
print(10 != 10.0)  # FALSE


# ENCADEAMENTO DE EXPRESSÕES (COMPARAÇÃO)
print("\n" * 2)
idade = 20
print(18 <= idade <= 30)  # TRUE


# COMPARAÇÃO DE STRINGS (ORDEM LEXOCOGRÁFICA) => UNICODE (ASCII)
print("\n" * 2)

print("ana" == "ANA")  # FALSE: "A" 65 == "a" 97
print("banana" > "abacate")  # TRUE
print("unifel" != "Unifel")  # TRUE
print("unifel" < "Unifel")  # FALSE: NA UNICODE, as letras MAIÚSCULAS são MENORES!

print("ana" == "anaconda")  # FALSE!
print("ana" < "anaconda")  # TRUE!

print("zzz" < "anaconda")  # FALSE
print("abc" < "abd")  # TRUE
print("abc" < "ab")  # FALSE
print("aaa" < "zzz")  # TRUE
print("João" > "Maria")  # FALSE

print("Jorge" > "ana")  # FALSE, pois "J" = 74 > "a" = 97 = FALSE!

print(ord("a"))  # 97
print(ord("J"))  # 74
print(ord("A"))  # 65


print("10" > "2")  # FALSE!
# "10" = string
# "2" = string

# "1" = 49
# "2" = 50


# CURTO CIRCUITO
print(False and print("Olá"))  # FALSE (e o print NUNCA VAI EXECUTAR)
print(True or print("Oi"))  # TRUE (o print NUNCA SERÁ EXECUTADO)

print("-" * 30)
# TRUTHY E FALSY
# Python como um COMPARADOR (==, >, <, >=, <=). Retorna TRUE ou FALSE (sempre!)
resultado = 10 > 5  # TRUE
print(resultado)  # TRUE

# Python como um SELECIONADOR/JULGADOR (or, and)
# Retorna o objeto MAIS SIGNIFICATIVO DA EXPRESSÃO LÓGICA
# Ex. 1
nome_user = ""  # FALSE
login = nome_user or "Visitante"  # = VERDADEIRO
print(login)  # Visitante


# Ex. 2
user_ativo = True
permissao_adm = "Acesso Total"
status = user_ativo and permissao_adm
print(status)  # Acesso Total


# Ex. 3
cupom_desconto = 0  # Falsy!
desconto_padrao = 5.0  # Truthy!
# Se não tem cupom, use o cupom PADRÃO
valor_desconto = cupom_desconto or desconto_padrao
print(f"Desconto aplicado: {valor_desconto} \n")  # 5.0


# Ex. 4

# 0 (False)
resultado = "Conexão OK!" and 0 and "Dados recebidos! \n\n" and ""

# Dados recebidos! Pois o and (e or também) retornam o ÚLTIMO valor significativo quando não encontrar um valor de parada
resultado = "Conexão OK!" and 0.1 and "Dados recebidos! \n\n"  # TRUE
print(f"RESULTADO = {resultado}")


# Ex. 5
config_servidor = ""  # Falsy!
server_padrao = "192.168.1.100"  # Truthy!
server_ativo = server_padrao or config_servidor  # TRUE: "192.168.1.100"
print(f" Servidor conectado em: {server_ativo}")


# AND: Use para condições de segurança, prevenção de erros,
# filtro de acesso (autorização), validação em cadeia.

# OR: Use para ter um plano B (aquele valor que será usado caso o outro não sirva),
# alternativa, quando precisa ter um VALOR PADRÃO
