import pandas as pd
vendas_df = pd.read_excel('/home/darlanzin/Documentos/planilhaloja.xlsx')
#print(vendas_df)
camisa_df = vendas_df.loc[vendas_df['produto'] == 'camisa',['produto','valor','quantidade']]
faturamento_camisa = camisa_df['valor'] * camisa_df['quantidade']
print(camisa_df)
print('O valor de vendas em camisetas da loja é: ', faturamento_camisa.sum() )
