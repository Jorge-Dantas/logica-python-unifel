# print("Olá, mundo! Meu primeiro app Python!!")


# 🧠 QUIZ: Compilação vs. Interpretação
# Pergunta 1: O que é o Bytecode no Python?
# a) O código que o processador entende diretamente.
# b) Uma linguagem intermediária que a Máquina Virtual do Python (PVM) lê.
# c) Um vírus que o Python cria para travar o PC.
# d) O texto que nós digitamos no VS Code.
# Resposta: b

# Pergunta 2: Onde ficam guardadas as instruções otimizadas (.pyc) do Python?
# a) Na pasta Documents.
# b) Na pasta oculta __pycache__.
# c) Dentro do processador.
# d) No GitHub.
# Resposta: b


# Pergunta 3: Qual a vantagem do Python usar uma "Máquina Virtual" (PVM)?
# a) Ele fica mais lento que o Excel.
# b) Portabilidade: O mesmo código roda em qualquer sistema operacional que tenha o Python instalado.
# c) Ele economiza energia elétrica.
# d) Ele apaga o lixo de memória automaticamente (embora o GC faça isso, a PVM foca na execução)
# Resposta: b

# Pergunta 4: O Python compila o código para um arquivo .exe como o C# ou C++?
# a) Não, ele interpreta o Bytecode em tempo real (Runtime).
# b) Sim, sempre.
# c) Sim, mas apenas se o arquivo for muito grande.
# Resposta: a

# Pergunta 5: Se eu deletar a pasta __pycache__, meu programa para de funcionar?
# a) Sim, você perdeu tudo.
# b) Não, o Python simplesmente a criará novamente na próxima execução.
# Resposta: b


# Pergunta 6: Python é compilada ou interpretada?
# a) Compilada, pois gera arquivos executáveis (.exe) antes de rodar.
# b) Interpretada, pois executa o código linha por linha sem nenhuma etapa anterior.
# c) ❌ Nenhuma das alternativas, Python não se encaixa em nenhuma categoria.
# d) Interpretada com compilação intermediária para Bytecode antes da execução.
# Resposta: d


# int a = 30 -> ERRADO

# a = 30  # CERTO (INT)
# nome_funcionario = None
# nome_funcionario = "Maria"
# print(nome_funcionario)


class Pessoa:
    def apresentar(self):
        print("Olá, eu sou uma pessoa!")


jorge_dantas = Pessoa()
jorge_dantas.apresentar()

# POR DEBAIXO DOS PANOS
Pessoa.apresentar(jorge_dantas)


class Pessoa:
    especie = "Ser Humano"

    @classmethod
    def mostrar_especie(cls):
        print(cls.especie)


class Conta:
    def __init__(self):
        self.saldo = 5000  # publico: todos podem acessar esse atributo!!


# FORA DA CLASSE
conta_falcao = Conta()
print(conta_falcao.saldo)  # saldo está diretamente acessível, PERIGO!!!
conta_falcao.saldo = 1000000  # qualquer um pode alterar o saldo, PERIGO!!!


class Conta:
    def __init__(self):
        self._saldo = 1000  # PROTEGIDO (convenção)! Ainda pode ser alterado.


# OUTRA CLASSE
conta_grasi = Conta()
print(conta_grasi._saldo)  # É POSSÍVEL, mas não recomendado!


class Conta:
    def __init__(self):
        self.__saldo = 500  # NAME MANGLING (PRIVADO COM MAIS FORÇA)

    # Um método público que acessa o saldo privado (encapsulamento).
    def mostrar_saldo(self):
        print(self.__saldo)


# OUTRA CLASSE
conta_antonio = Conta()
# ERRO, a outra classe não pode acessar diretamente saldo que está privado!!
print(conta_antonio.__saldo)
print(conta_antonio.mostrar_saldo())  # CERTO!!

print(conta_antonio._Conta__saldo)  # O python muda o nome do atributo para
# evitar acesso direto e erros de HERANÇA!
