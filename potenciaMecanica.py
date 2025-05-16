import pandas as pd

# Lê o arquivo Excel
df = pd.read_excel(
    "BANCO DE DAODS DO HOSPITAL.xlsx",
    sheet_name="DADOS DAS FICHAS DE VENTILAÇÃO",
    header=4
)

# Função para calcular a potência mecânica
def gattinoniS(FR, Vt, Ppico, Pplato, PEEP):
    return 0.098 * FR * (Vt/1000) * (Ppico - 0.5 * (PEEP - Pplato))

# Define as colunas necessárias
colunas_necessarias = ["FREQUÊNCIA RESPIRATÓRIA", "Vt", "Ppico", "PRESSÃO PLATÔ ", "PEEP"]

# Garante que os dados estejam no formato float
df[colunas_necessarias] = df[colunas_necessarias].apply(pd.to_numeric, errors='coerce')

# Aplica a função somente nas linhas que têm todos os valores necessários
df["POTÊNCIA MECÂNICA"] = df.apply(
    lambda row: gattinoniS(
        row["FREQUÊNCIA RESPIRATÓRIA"],
        row["Vt"],
        row["Ppico"],
        row["PRESSÃO PLATÔ "],
        row["PEEP"]
    ) if pd.notnull(row["FREQUÊNCIA RESPIRATÓRIA"]) and
         pd.notnull(row["Vt"]) and
         pd.notnull(row["Ppico"]) and
         pd.notnull(row["PRESSÃO PLATÔ "]) and
         pd.notnull(row["PEEP"]) else None,
    axis=1
)

# Salva o novo Excel
df.to_excel("saida_potencia_mecanica.xlsx", index=False)
