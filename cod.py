import os
#o modulo os é usado para usado para obter informações do sistema operacional
import pandas as pd 
#pandas é uma biblioteca usada para manipulação de dados

caminho = r"C:\Users\livia\Documents\bases"
#lista o que está em um diretorio 
arquivos = os.listdir(caminho)
#DataFrame é uma tabela do python que nesse caso está vazia, onde vai ser usada para carga das tabelas
tabela_consolidada = pd.DataFrame() 

for nome_arquivo in arquivos:
    tabela_vendas = pd.read_csv(os.path.join(caminho, nome_arquivo)) #lê arquivo por arquivo que está em csv econcatena o nome do caminho com o nome do arquivo
    tabela_vendas["Data de Venda"] = pd.to_datetime ("01/01/1900") + pd.to_timedelta (tabela_vendas["Data de Venda"], unit="D") #pega a data inicio considerada pelo excel e soma a quantidade informada na coluna Data de Venda para descobrir a data no formado normal
    tabela_consolidada = pd.concat ([tabela_consolidada, tabela_vendas])
tabela_consolidada = tabela_consolidada.sort_values (by = "Data de Venda")
tabela_consolidada = tabela_consolidada.reset_index (drop = True)
tabela_consolidada.to_excel ("Vendas.xlsx", index= False)

