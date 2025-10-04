import pandas as pd
import numpy as np
from datetime import date, timedelta
import csv # Importação necessária para corrigir o erro de aspas no CSV

# --- 1. CONFIGURAÇÃO E SIMULAÇÃO DE DADOS ---
print("1. Simulação do Dataset de Vendas...")

# Definir o período e o número de registros (mínimo 50)
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)
num_records = 150 # Usando 150 para uma simulação mais robusta
num_products = 10

# Listas de Produtos e Categorias
products = [f'Produto_{i}' for i in range(1, num_products + 1)]
categories = ['Eletrônicos', 'Vestuário', 'Alimentos', 'Casa & Decoração', 'Livros']

# Gerar dados aleatórios
data = {
    'ID': range(1, num_records + 1),
    'Data': [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(num_records)],
    'Produto': np.random.choice(products, num_records),
    'Categoria': np.random.choice(categories, num_records),
    'Quantidade': np.random.randint(1, 20, num_records), # Quantidade de 1 a 19
    'Preco': np.round(np.random.uniform(10.0, 500.0, num_records), 2) # Preços de 10.00 a 500.00
}

df_vendas = pd.DataFrame(data)

# --- 2. ADIÇÃO DE RUÍDO PARA TESTAR A LIMPEZA ---
# Adicionar valores faltantes (NaN) para teste [cite: 23]
df_vendas.loc[np.random.choice(df_vendas.index, 5, replace=False), 'Preco'] = np.nan
df_vendas.loc[np.random.choice(df_vendas.index, 3, replace=False), 'Quantidade'] = np.nan

# Adicionar linhas duplicadas para teste [cite: 24]
df_vendas = pd.concat([df_vendas, df_vendas.sample(5)], ignore_index=True)
df_vendas.sort_values(by='ID', inplace=True) # Reordenar para simular dados mais realistas

# Adicionar um tipo incorreto (ex: um ID como string)
df_vendas.loc[df_vendas.index[-1], 'ID'] = 'INV-ID'

# --- 3. LIMPEZA DOS DADOS ---
print("2. Limpeza de Dados: Tratamento de Nulos, Duplicatas e Tipos...")

# a) Remoção de Duplicatas [cite: 24]
# Usamos .copy() para evitar o SettingWithCopyWarning e garantir manipulação segura.
df_limpo = df_vendas.drop_duplicates().copy()
print(f"  - Linhas removidas por duplicidade: {len(df_vendas) - len(df_limpo)}")

# b) Conversão de Tipos de Dados [cite: 25]
# ID: Tentar converter para numérico. Erros serão coercidos a NaN
df_limpo['ID'] = pd.to_numeric(df_limpo['ID'], errors='coerce')
# Data: Garantir que esteja no formato datetime
df_limpo['Data'] = pd.to_datetime(df_limpo['Data'])

# c) Tratamento de Valores Faltantes (NaN) [cite: 23]
# Para colunas críticas (ID, Quantidade, Preço), removemos linhas com nulos
df_limpo.dropna(subset=['ID', 'Quantidade', 'Preco'], inplace=True)

# CONVERSÃO FINAL NECESSÁRIA PARA O POSTGRESQL (Remove o .0 dos IDs e garante tipos corretos)
df_limpo['ID'] = df_limpo['ID'].astype(int)
df_limpo['Quantidade'] = df_limpo['Quantidade'].astype(float)
df_limpo['Preco'] = df_limpo['Preco'].astype(float)

# --- 4. SALVAR DATASET LIMPO (COM CORREÇÃO DE CITAÇÃO E CODIFICAÇÃO) ---
file_name = 'data_clean.csv'

# AS CORREÇÕES FINAIS:
# 1. quoting=csv.QUOTE_NONE: Evita aspas duplas em torno dos números, resolvendo o erro de tipo no SQL.
# 2. encoding='utf-8': Garante que acentos e 'ç' sejam preservados, resolvendo o erro de codificação.
df_limpo.to_csv(file_name,
                index=False,
                quoting=csv.QUOTE_NONE,
                escapechar='\\',
                encoding='utf-8')
print(f"3. Dataset limpo e CORRIGIDO salvo em: {file_name} ")

# --- 5. ANÁLISE INICIAL DE VENDAS ---
print("4. Análise de Vendas por Produto...")

# a) Calcule o Total de Vendas (Quantidade * Preço) [cite: 28]
df_limpo['Total_Vendas'] = df_limpo['Quantidade'] * df_limpo['Preco']

# b) Calcule o Total de Vendas por Produto [cite: 28]
vendas_por_produto = df_limpo.groupby('Produto')['Total_Vendas'].sum().reset_index()
vendas_por_produto.columns = ['Produto', 'Soma_Total_Vendas']

# c) Identifique o produto com o maior número de vendas totais [cite: 29]
produto_maior_venda = vendas_por_produto.loc[vendas_por_produto['Soma_Total_Vendas'].idxmax()]

print("\n--- Resultados da Análise ---")
print("Total de Vendas por Produto (Top 5):")
print(vendas_por_produto.sort_values(by='Soma_Total_Vendas', ascending=False).head())

print(f"\nProduto com o MAIOR número de vendas totais: {produto_maior_venda['Produto']}")
print(f"Valor Total de Vendas: R$ {produto_maior_venda['Soma_Total_Vendas']:.2f}")