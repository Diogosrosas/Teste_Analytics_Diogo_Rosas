# Teste Analytics DIOGO DA SILVA ROSAS - Entrega Quod

## 1. Visão Geral do Projeto

Este repositório contém a entrega do Teste para Estagiário de Analytics da Quod, abrangendo as áreas de programação (Python), manipulação de dados, consultas SQL e interpretação de resultados.

**Ferramentas Utilizadas:** Python (Pandas, NumPy, Matplotlib), PostgreSQL/pgAdmin.

---

## 2. Estrutura do Repositório

O repositório está organizado da seguinte forma:

| Arquivo/Pasta | Conteúdo | Parte do Teste |
| :--- | :--- | :--- |
| `data_clean.csv` | Dataset de Vendas simulado, limpo e corrigido (sem aspas/UTF-8). | Parte 1 |
| `simulacao_e_limpeza.py` | Script Python para simulação, limpeza e salvamento do CSV. | Parte 1.A |
| `analise_exploratoria.py` | Script Python para geração do gráfico de tendência. | Parte 1.B |
| `tendencia_vendas_mensal.png` | Visualização da tendência mensal de vendas. | Parte 1.B |
| `consultas_sql.sql` | Consultas SQL solicitadas (cálculo de vendas e produtos de baixa performance). | Parte 2 |
| `relatorio_insights.md` | Relatório final de 300 palavras com insights e sugestões de ação. | Parte 3 |
| `README.md` | Este documento. | Documentação |

---

## 3. Como Executar os Scripts (Dependências)

Para replicar a análise, o ambiente de desenvolvimento deve ter as seguintes bibliotecas Python instaladas:

```bash
pip install pandas numpy matplotlib seaborn