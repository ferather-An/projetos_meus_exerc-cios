temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura < 10:
    print("Frio")
elif 10 <= temperatura < 20:
    print("Normal")
elif 20 <= temperatura < 30:
    print("Quente")