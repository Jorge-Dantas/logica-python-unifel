def app_politica_venda(valor_venda, sistema_ativo, estoque):
    valor_venda += 500
    sistema_ativo = False
    estoque.append("Cadeado Virtual SSL")  # Adiciona um item ao final de uma lista

    print("\n --- AINDA DENTRO DA FUNÇÃO (Executando política...) ---")
    print(
        f" \n Valor local (função): {valor_venda} | Sistema Ativo? {sistema_ativo} | Lista (estoque): {estoque} "
    )
    print(f"ID da lista (DENTRO DA FUNÇÃO): {id(estoque)}\n\n")


# MAIN (programa principal)
venda = 1000
status_sistema = True
lista_estoque = ["Antivírus Avast 7.0"]

app_politica_venda(venda, status_sistema, lista_estoque)  # Invocando a função

print(" --- FORA DA FUNÇÃO (O que sobrou?) --- ")
print(f" --- VENDA: {venda} --- ")
print(f" --- STATUS DO SISTEMA: {status_sistema} --- ")
print(f" --- ESTOQUE ATUAL: {lista_estoque} --- ")
print(f"ID da lista (FORA DA FUNÇÃO): {id(lista_estoque)} \n\n")


# NEM TODA ALTERAÇÃO DENTRO DA FUNÇÃO VOLTA PARA O MAIN
# Calling referecence (object reference)
# Imutáveis → parecem “cópia por valor” (seguros)
# Mutáveis → parecem “referência” (perigosos)
