# exemp_14 (Login): Crie duas variáveis user_db = "admin" e pass_db = "123".
# Receba via input o usuário e senha e exiba o valor lógico se ambos baterem.

# Exiba uma msg: "Login autorizado??" True/False que deve ser impresso a partir de uma variavel

# Exiba uma msg personalizada: "Bem-vindo Administrador" ou "User ou Senha incorretos" para
# o caso de ser True ou False ( SEM IF )

user_db = "admin"
pass_db = "123"

print("-" * 30)
print(f" {'SISTEMA DE ACESSO':^30}")
print("-" * 30)


db_user = input("Digite o nome do user: ")
password_db = str(input("Agora digite a senha: "))

acesso_concedido = (user_db == db_user) and (pass_db == password_db)

print(f"\n Login autorizado? {acesso_concedido}")
print("-" * 30)

msg_personalizada = (
    acesso_concedido and "Bem-vindo Administrador" or "User ou Senha incorretos"
)

print(f" STATUS LOGIN: {msg_personalizada}")
print("-" * 30)


# _____________________


# exemp_14 (Sensor): Crie um sistema que exiba True se uma temperatura estiver
# entre 20 e 30 graus (faixa ideal). Receba a temperatura do usuário.

temp = float(input("Digite a temperatura: "))

if 20 <= temp <= 30:
    print(f"Temperatura: {temp} => {20 <= temp <= 30}")

# WALACE
temp_user = float(input("Digite a temperatura: "))
faixa_ideal = 20 <= temp_user <= 30
temp_ideal = (
    faixa_ideal
    and "A temperatura está na faixa ideal."
    or "A temperatura está fora da faixa ideal."
)
print(temp_ideal)


# _____________________

# exemp_14 (Elegibilidade): Um eleitor só vota se tiver idade entre 16 e 70 anos.
# Receba do usuário a idade, e então
# exiba True ou False (valor lógico) para o candidato (teste candidatos com 15 anos,
# e também com 75 anos para ver se o código funciona).
idade = int(input("Digite sua idade: "))

pode_votar = (
    16 <= idade <= 70
    and "\n\nVocê pode votar!! \n"
    or "\n\nCandidato não elegível a voto. \n"
)

print(f"Candidato com {idade} anos!")

print(f"Pode votar?? {pode_votar}")
