import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo para os gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# --- 1. CARREGAMENTO E PRÉ-PROCESSAMENTO ---
file_name = 'data_clean.csv'
try:
    df = pd.read_csv(file_name)
    print(f"Dataset '{file_name}' carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO: Arquivo '{file_name}' não encontrado. Certifique-se de executar o script da Parte 1.A primeiro.")
    exit()

# Garantir que a coluna 'Data' seja do tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Calcular o Total de Vendas (se não tiver sido feito no script anterior)
if 'Total_Vendas' not in df.columns:
    df['Total_Vendas'] = df['Quantidade'] * df['Preco']

# Extrair o Mês/Ano para a análise de tendência
df['Mes_Ano'] = df['Data'].dt.to_period('M')

# --- 2. CÁLCULO DA TENDÊNCIA MENSAL ---
# Agrupar os dados para somar o total de vendas por mês/ano
vendas_mensais = df.groupby('Mes_Ano')['Total_Vendas'].sum().reset_index()

# Converter 'Mes_Ano' de volta para um formato de string/datetime que o Matplotlib entenda facilmente
vendas_mensais['Mes_Ano'] = vendas_mensais['Mes_Ano'].astype(str)

# --- 3. CRIAÇÃO DO GRÁFICO DE LINHA ---
print("\nGerando Gráfico de Linha da Tendência de Vendas...")

plt.figure(figsize=(14, 7))
sns.lineplot(
    x='Mes_Ano',
    y='Total_Vendas',
    data=vendas_mensais,
    marker='o', # Adiciona marcadores para cada mês
    color='blue'
)

# Títulos e Rótulos
plt.title('Tendência Mensal do Total de Vendas (Jan/2023 - Dez/2023)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45, ha='right') # Rotaciona os rótulos do eixo X para melhor visualização
plt.grid(True, linestyle='--', alpha=0.7)

# Adicionar rótulos de dados (opcional, mas útil para leitura)
for index, row in vendas_mensais.iterrows():
    plt.text(row['Mes_Ano'], row['Total_Vendas'] + 500, f'R${row["Total_Vendas"]:.0f}',
             ha='center', va='bottom', fontsize=8)

# Salvar a visualização
chart_file_name = 'tendencia_vendas_mensal.png'
plt.tight_layout()
plt.savefig(chart_file_name)
plt.show()

print(f"Gráfico de linha salvo como: {chart_file_name}")