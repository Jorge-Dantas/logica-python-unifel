from src.services.frete_services import gerar_orcamento_frete

print("-" * 30)
print("--- SISTEMA DE FRETE (TRANSPORTADORA) ---")
print("-" * 30)

distancia = float(input(" Qual a distância desse envio (km) ? "))
peso = float(input(" Qual o peso da carga (kg) ? "))
categoria = input(" Qual a categoria (Padrão ou Frágil)? ")

# Parâmetro nomeado (a ordem não importa)!!
custo_final, prazo = gerar_orcamento_frete(
    categoria=categoria, peso=peso, distancia=distancia
)

print(f"\n O seu custo de frete é: {custo_final} \n")
print(f"\n O prazo de entrega é de: {prazo} \n")
