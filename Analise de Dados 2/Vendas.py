import pandas as pd

# PASSO 1 - IMPORTAR A BASE DE DADOS

tabela = pd.read_excel("Vendas.xlsx")
print(tabela)

# PASSO 2 - FATURAMENTO GERAL

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

#PASSO 3 - COMEÇAR A ANÁLISE TOP DOWN

# FATURAMENTO POR LOJA

faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

# PASSO 4 - ENTRAR NO DETALHE PARA ENTENDER

faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)
