from services.financeiro_services import app_reajuste_perigoso, app_reajuste_seguro

precos_originais = [100.50, 500.99, 45.67]


# Se eu rodar isso, o que vai rolar??
app_reajuste_seguro(precos_originais)
# Os 10% serão aplicados APENAS AS VARIÁVEIS DA FUNÇÃO (locais -> nova_lista)

print(f"\n ORIGINAIS (protegidos): {precos_originais}\n")

# Se eu rodar isso, o que vai rolar??
app_reajuste_perigoso(precos_originais)


print(f"\n ORIGINAIS (depois do perigoso): {precos_originais}\n")
