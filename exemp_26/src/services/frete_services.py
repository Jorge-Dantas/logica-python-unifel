def gerar_orcamento_frete(distancia, peso, categoria="Padrão"):
    custo_base = distancia * 0.50
    adicional_peso = peso * 1.20

    if categoria.lower() == "fragil":
        adicional_peso *= 1.5

    custo_total = custo_base + adicional_peso

    prazo_estimado = (distancia // 500) + 1

    return custo_total, prazo_estimado
