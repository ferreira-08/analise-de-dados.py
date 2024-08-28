import pandas as pd

#1 TRAZER A BASE DE DADOS

tabela = pd.read_excel("Vendas.xlsx")
print(tabela)

#2 FATURAMENTO GERAL

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

#3 COMEÇAR A ANÁLISE TOP DOWN

#faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

#4 ENTRAR NO DETALHE PARA ENTENDER

faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)
