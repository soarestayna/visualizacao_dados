import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

data_path = Path('../dataset/clientes-v3-preparado.csv')
df = pd.read_csv(data_path)
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70') # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')


# Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação')
plt.show()

# Gráfico de Dispersão Hexagonal
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()


# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))

