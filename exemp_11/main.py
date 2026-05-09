# # EX. Sinal de trânsito
# sinal = "amarelo"

# if sinal == "verde":
#     print("SIGA!")
# elif sinal == "amarelo":
#     print("SIGA!")
# else:
#     print("PARE!!")


# Validação de faixa de idade
idade = int(input(" Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade! ")
elif 18 <= idade <= 20:
    print("Você é maior de idade (jovem, acabou de sair da adolescência)")
elif 21 <= idade <= 29:
    print("Você é um jovem adulto")
elif 30 <= idade <= 45:
    print("Parabéns. Você está maduro!")
elif 46 <= idade <= 64:
    print("Comemore! Você é uma pessoa na terceira idade")
else:
    print("Você é um idoso! \nCoroa, já anda de graça no buzu!! =)")


# TRUTHY / FALSY
# NEM SEMPRE você precisa usar: variavel == True
# O if já faz uma pergunta implítica com o método bool()

# print("\n")
# nome = input("Qual o seu nome? ")

# if nome:  # True. INTERNAMENTE: bool(nome) == True
#     print(f"Bem-vindo ao curso de Lógica com Python - UNIFEL 2026.3, {nome}!! \n")
# else:  # nome = "" (False)
#     print("ERRO: O nome do usuário não pode ser vazio!! \n")


# # IF TERNÁRIO (3) -> IF SIMPLES (condição única)
# # FORMA TRADICIONAL:
# idade = 15

# if idade > 18:
#     status = "Pode entrar"
# else:
#     status = "Acesso Negado"

# # IF TERNÁRIO:
# status = "Pode entrar" if idade > 18 else "Acesso Negado"


# # A Ordem dos Fatores Altera o Resultado (ELIF)
# # ARMADILHA DO IF: Ele para na primeira verdade que encontrar (a única)

# # ERRADO: O 70 anos entra no primeiro IF e nunca chega no Idoso
# if idade >= 18:
#     print("Adulto")
# elif idade >= 65:  # Nunca será testado se idade for maior que 18!!
#     print("Idoso")

# # CERTO (Sempre da MAIOR RESTRIÇÃO para a MENOR):
# if idade >= 65:
#     print("Idoso")
# elif idade >= 18:
#     print("Adulto")
