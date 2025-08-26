# Visualização de Dados – Matplotlib & Seaborn

Este repositório faz parte do meu portfólio acadêmico desenvolvido durante o 
curso de **Análise de Dados – EBAC**.
Aqui estão reunidos notebooks, scripts e gráficos que exploram **técnicas 
de visualização de dados com foco em análise exploratória e comunicação visual** 
aplicadas em dados reais ou simulados.

---


## Objetivo

Demonstrar o uso das bibliotecas `Matplotlib` e `Seaborn` para:

- Criar gráficos informativos e esteticamente claros
- Explorar distribuições, correlações e padrões em dados reais
- Automatizar a geração de gráficos com scripts reutilizáveis
- Salvar visualizações para uso em relatórios e apresentações

---

## Conteúdo dos Notebooks

### **1. Visualização com `Pandas`**

- Gráficos básicos diretamente com pandas
- Histogramas, boxplots e gráficos de dispersão

### **2. Uso do `Matplotlib`**

- Criação de gráficos personalizados
- Ajuste de cores, títulos, eixos e legendas
- Subplots e visualizações combinadas

### **3. Uso do `Seaborn`**

- Gráficos estatísticos com estética aprimorada
- distplot, regplot, heatmap, pairplot, countplot
- Análise de correlação e distribuição por categoria

### **4. Exemplos e Aplicações**

- Casos práticos com dados de clientes
- Comparação entre tipos de gráficos
- Utilização das `matplotlib` e `seaborn` bibliotecas em um gráfico


## **Scripts Python**

Além dos notebooks interativos, este repositório inclui `scripts .py` 
que automatizam as etapas do projeto.  

Esses scripts são úteis para:

- Executar o processo em ambientes fora do Jupyter  
- Integrar o código em pipelines ou aplicações  
- Reutilizar funções com maior eficiência
- Automatizar a criação dos gráficos

Scripts disponíveis:

- `1_visualizacao_dados.py` – gráficos com `pandas`
- `2_uso_matplotlib.py` – visualizações com `matplotlib`
- `3_uso_searborn.py` - visualizações com `searborn`
- `4_exemplos_graficos` - gráficos visuais complexos
utilizando as bibliotecas `matplotlib` e `seaborn`


### Galeria de Gráficos

Os gráficos gerados estão na pasta graficos/ e pode ser utilizados para comparação. 

_(Total de 14 gráficos gerados automaticamente)_


### Componentes do Projeto

- pandas – manipulação de dados
- matplotlib – gráficos customizados
- seaborn – visualizações estatísticas
- pathlib – gerenciamento de caminhos e arquivos
- clientes-v3-preparado.csv – base de dados utilizada

---


## Aprendizados

- A visualização é essencial para entender padrões e comunicar insights.
- Matplotlib oferece controle total sobre os elementos gráficos.
- Seaborn facilita a criação de gráficos estatísticos com design refinado.
- Automatizar a geração de gráficos permite reprodutibilidade e agilidade.

---

## Como usar este repositório

Você pode explorá-lo de duas formas:

### Notebooks

Organizados por tema e executáveis em ambiente Jupyter.
Cada notebook contém explicações, exemplos e visualizações.

### Scripts Python

Executam os gráficos de forma automatizada.

Para executar:

````bash
python scripts/2_uso_matplotlib.py
````

Antes de executar, instale as dependências:

````
pip install -r requirements.txt
````

---

### Sobre mim

Sou estudante de Análise de Dados e este projeto representa minha evolução 
na comunicação visual de dados.
Cada gráfico foi pensado para transformar números em narrativas 
visuais que geram impacto.