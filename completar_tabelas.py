import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

laudos_path = os.path.join(script_dir, "laudos_planilhados.xlsx")
exemplo_path = os.path.join(script_dir, "Exemplo.xlsx")

solo_laudos = pd.read_excel(laudos_path, sheet_name="SOLO")
agua_subterranea_laudos = pd.read_excel(laudos_path, sheet_name="AGUA SUBTERRANEA")
solo_industrial_exemplo = pd.read_excel(exemplo_path, sheet_name="solo_industrial")
agua_subterranea_exemplo = pd.read_excel(exemplo_path, sheet_name="agua_subterranea")

print("Colunas disponíveis na aba 'SOLO':", solo_laudos.columns)

print("Colunas disponíveis na aba 'solo_industrial':", solo_industrial_exemplo.columns)

coluna_conama_industrial = "CONAMA Nº420 - Valores de Investigação Industrial"
coluna_conama_agua = "CONAMA Nº420 - Águas Subterrâneas"

for index, row in solo_laudos.iterrows():
    parametro_solo = row["PARAMETRO"]
    match = solo_industrial_exemplo[solo_industrial_exemplo["Parâmetro"] == parametro_solo]
    if not match.empty:
        valor_conama = match.iloc[0][coluna_conama_industrial]
        solo_laudos.at[index, "CONAMA 420"] = valor_conama

for index, row in agua_subterranea_laudos.iterrows():
    parametro_agua = row["PARAMETRO"]
    match = agua_subterranea_exemplo[agua_subterranea_exemplo["Parâmetro"] == parametro_agua]
    if not match.empty:
        valor_conama = match.iloc[0][coluna_conama_agua]
        agua_subterranea_laudos.at[index, "CONAMA 420"] = valor_conama

solo_laudos.to_excel("resultado_solo.xlsx", index=False)
agua_subterranea_laudos.to_excel("resultado_agua_subterranea.xlsx", index=False)

print("Processamento concluído. Resultados salvos em 'resultado_solo.xlsx' e 'resultado_agua_subterranea.xlsx'.")