import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('natalidade.csv')

#Taxa de natalidade por ano, separada entre Masculino e Feminino
"""
births_per_year_gender = df.groupby(['year', 'gender'])['births'].sum().unstack()
births_per_year_gender.plot(kind='bar', stacked=False)
plt.title("Taxa de Natalidade por Ano e Gênero")
plt.xlabel("Ano")
plt.ylabel("Número de Nascidos")
plt.legend(title="Gênero")
plt.show()

"""
##########################################################################################################################################################################################################################################################################################
# Média de nascidos para os dias da semana
"""df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['month'] = pd.to_numeric(df['month'], errors='coerce')
df['day'] = pd.to_numeric(df['day'], errors='coerce')

df['date'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')

df['day_of_week'] = df['date'].dt.dayofweek 
births_per_day_of_week = df.groupby('day_of_week')['births'].mean()
births_per_day_of_week.index = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

births_per_day_of_week.plot(kind='bar')
plt.title("Média de Nascidos por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Média de Nascidos")
plt.show()"""

##########################################################################################################################################################################################################################################################################################
# Taxa de nascimento para cada mês do ano de 2005
"""births_2005 = df[df['year'] == 2005]
births_per_month_2005 = births_2005.groupby('month')['births'].sum()
births_per_month_2005.plot(kind='bar')
plt.title("Taxa de Nascimento por Mês em 2005")
plt.xlabel("Mês")
plt.ylabel("Número de Nascidos")
plt.show()
"""
# Valor médio de nascimento para os meses do ano
"""births_avg_per_month = df.groupby('month')['births'].mean()
births_avg_per_month.plot(kind='bar')
plt.title("Média de Nascidos por Mês")
plt.xlabel("Mês")
plt.ylabel("Média de Nascidos")
plt.show()"""