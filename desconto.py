valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra > 200:
    desconto = 0.20
    print("20% de desconto")
elif valor_compra > 100:
    desconto = 0.10
    print('10% de desconto')
else: 
    desconto = 0.05
    print('5% de desconto')
    
valor_final = valor_compra - (valor_compra * desconto)
print(f"Valor final: R$ {valor_final:.2f}")