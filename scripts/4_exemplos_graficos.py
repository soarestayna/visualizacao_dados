import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_style('whitegrid')  # Estilo visual para os gráficos

data_path = Path('../dataset/clientes-v3-preparado.csv')
df = pd.read_csv(data_path)

df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos',
              'nivel_educacao_cod', 'area_atuacao_cod']].corr()

# Heatmap de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

# Countplot
sns.countplot(x='estado_civil', data=df)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.show()

# Countplot com legenda
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.title('Distribuição do Estado Civil por Nível de Educação')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nível de Educação')
plt.show()

