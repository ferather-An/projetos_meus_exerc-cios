import matplotlib.pyplot as plt

def obter_dados():
    num_tubos = int(input("Digite o número de tubos utilizados: "))
    temperaturas = []
    vol_deslocado = []

    for i in range(num_tubos):
        print(f"Tubo {i + 1}:")
        temp = int(input("  Digite a temperatura (°C): "))
        vol = float(input("  Digite o volume deslocado (mL): "))
        temperaturas.append(temp)
        vol_deslocado.append(vol)

    return temperaturas, vol_deslocado

def calcular_resultados(temperaturas, vol_deslocado):
    densidade = 1.02
    massa_molar_etanol = 46
    massa_molar_acetaldeido = 44
    massa_molar_glicose = 180
    massa_molar_co2 = 88
    numero_avogadro = 6.02e23

    co2_produzido = []
    glicose_consumida = []
    moleculas_glicose = []

    for vol in vol_deslocado:
        massa_co2 = vol * densidade
        co2_produzido.append(massa_co2)

        massa_glicose = (massa_molar_glicose / massa_molar_co2) * massa_co2
        glicose_consumida.append(massa_glicose)

        num_moleculas = (massa_glicose / massa_molar_glicose) * numero_avogadro
        moleculas_glicose.append(num_moleculas)

    return co2_produzido, glicose_consumida, moleculas_glicose

def gerar_grafico(temperaturas, co2_produzido, glicose_consumida):
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Temperatura (°C)')
    ax1.set_ylabel('CO₂ Produzido (g)', color=color)
    ax1.plot(temperaturas, co2_produzido, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Glicose Consumida (g)', color=color)
    ax2.plot(temperaturas, glicose_consumida, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Produção de CO₂ e Consumo de Glicose em Diferentes Temperaturas')
    plt.show()

def exibir_resultados(temperaturas, vol_deslocado, co2_produzido, glicose_consumida, moleculas_glicose):
    print("Resumo dos Resultados")
    print("| Tubo | Temperatura (°C) | Vol. Deslocado (mL) | CO₂ Produzido (g) | Glicose Consumida (g) | Moléculas de Glicose |")
    print("| ---- | ---------------- | ------------------- | ----------------- | --------------------- | -------------------- |")
    for i in range(len(temperaturas)):
        print(f"| {i + 1}    | {temperaturas[i]}                | {vol_deslocado[i]}                 | {co2_produzido[i]:.2f}              | {glicose_consumida[i]:.2f}                 | {moleculas_glicose[i]:.2e}          |")

# Fluxo principal do programa
temperaturas, vol_deslocado = obter_dados()
co2_produzido, glicose_consumida, moleculas_glicose = calcular_resultados(temperaturas, vol_deslocado)
exibir_resultados(temperaturas, vol_deslocado, co2_produzido, glicose_consumida, moleculas_glicose)
gerar_grafico(temperaturas, co2_produzido, glicose_consumida)