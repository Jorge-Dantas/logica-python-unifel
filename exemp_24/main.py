from src.services.loja_services import calcular_carrinho, formatar_real

valor_final = calcular_carrinho(0.50, 230.59, 270.99, 1500.00, 2000.99)

print(f"\n Total a pagar é: {formatar_real(valor_final)} \n")
