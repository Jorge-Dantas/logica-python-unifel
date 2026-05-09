from src.services.investimentos_services import obter_valor_valido, calcular_rendimento
from src.utils.formatador import formatar_moeda

print("-" * 30)
print("----- SISTEMA BANCÁRIO UNIFEL -----")
print("-" * 30)

capital = obter_valor_valido("\n Capital inicial: R$ ")
tempo = int(obter_valor_valido("\n A aplicação é de quantos meses? "))

rendimento, total = calcular_rendimento(capital, tempo)

print(f"\n O lucro real gerado foi de: {formatar_moeda(rendimento)}")
print(f"\n O montante final é de: {formatar_moeda(total)} \n")
