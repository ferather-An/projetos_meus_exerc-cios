hora = input("Digite a hora atual (hh:mm): ")

if hora >= "06:00" and hora <= "11:59":
    print("Bom dia!")
elif hora >= "12:00" and hora <= "18:00":
    print("Boa tarde!")
else:
    print("Boa noite!")