salario = 5000  # tipo => INT (inteiro)
bonus_salario = "500.05"  # tipo: STRING (letra)

# salario_com_bonus = salario + bonus_salario  # TYPE ERROR (Erro de tipo)
# salario_com_bonus = str(salario) + bonus_salario  # Solução: usar métodos de casting (ex: str())

salario_com_bonus = salario + float(bonus_salario)

# Usando concatenação de string (antigo)
# print("\n Salário final: " + salario_com_bonus + "\n")

# INTERPOLAÇÃO de string (MODERNO)
print(f"\n Salário final: {salario_com_bonus} \n")
