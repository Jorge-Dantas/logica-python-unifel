def app_reajuste_seguro(valores):
    nova_lista = []

    for v in valores:
        nova_lista.append(v * 1.10)  # Aplica 10% e salva!

    return nova_lista


def app_reajuste_perigoso(valores):
    # Altera o valor ORIGINAL NA MEMÓRIA
    for i in range(len(valores)):
        valores[i] *= 1.10  # Aplica 10% e salva!
