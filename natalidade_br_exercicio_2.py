import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv("natalidade_br.csv")

# Função para classificar o peso dos bebês
def classificar_peso(peso):
    if peso >= 4500:
        return "Tamanho Excessivamente Grande"
    elif 2500 <= peso < 4000:
        return "Peso Normal"
    elif 1500 <= peso < 2500:
        return "Baixo Peso ao Nascer"
    elif 1000 <= peso < 1500:
        return "Muito Baixo Peso ao Nascer"
    else:
        return "Extremo baixo Peso ao Nascer"

# Adicionar coluna de classificação de peso
df["Classificacao_Peso"] = df["PESO"].apply(classificar_peso)

# Contagem de bebês em cada categoria de peso
contagem_peso = df["Classificacao_Peso"].value_counts()

# Gráfico de barras das classificações de peso
plt.figure(figsize=(10, 6))
plt.bar(contagem_peso.index, contagem_peso.values, color=['skyblue', 'lightgreen', 'salmon', 'orange', 'purple'])
plt.title("Quantidade de Bebês por Faixa de Peso ao Nascer")
plt.xlabel("Classificação de Peso")
plt.ylabel("Quantidade de Bebês")
plt.xticks(rotation=0)
plt.show()

# Distribuição da semana gestacional para bebês com extremo baixo peso
extreme_low_weight = df[df["Classificacao_Peso"] == "Extremo baixo Peso ao Nascer"]
gestational_weeks_counts = extreme_low_weight["GESTACAO"].value_counts()
gestational_weeks_counts.plot(kind="bar", color="salmon")
plt.title("Semana Gestacional de Bebês com Extremo Baixo Peso ao Nascer")
plt.xlabel("Semana Gestacional")
plt.ylabel("Quantidade de Bebês")
plt.xticks(rotation=0)
plt.show()

#menor e o maior peso de bebês
min_weight = df["PESO"].min()
max_weight = df["PESO"].max()
pesos = [min_weight, max_weight]
labels = ["Menor Peso", "Maior Peso"]

plt.figure(figsize=(8, 5))
plt.bar(labels, pesos, color=['lightblue', 'lightcoral'])
plt.title("Menor e Maior Peso ao Nascer")
plt.ylabel("Peso (gramas)")
plt.show()