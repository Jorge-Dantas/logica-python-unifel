# OPERADOR IS => Dá o ENDEREÇO do objeto (na RAM)
a = [1, 2]
b = [1, 2]
print(a == b)  # TRUE
print(a is b)  # FALSE

b = a  # b agora aponta para o mesmo endereço que a, e o objeto [1,2] de b será destruído!
print(a == b)  # TRUE
print(a is b)  # TRUE

print("\n\n\n")

# FUNÇÃO BOOL() => Método que retorna o VALOR LÓGICO do objeto
print(bool(0))  # FALSE
print(bool(1))  # TRUE
print(bool(""))  # FALSE
print(bool("oi"))  # TRUE
print(bool([]))  # FALSE
