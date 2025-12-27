import pandas as pd
import matplotlib.pyplot as plt

# A ideia aqui é pegar o faturamento bruto dos produtos

vendas_df = pd.read_excel('/home/darlanzin/Documentos/planilhaloja.xlsx')
camisa_df = vendas_df.loc[vendas_df['produto'] == 'camisa', ['produto', 'valor', 'quantidade']]
faturamento_camisa = camisa_df['valor'] * camisa_df['quantidade']

calça_df = vendas_df.loc[vendas_df['produto'] == 'calça', ['produto', 'valor', 'quantidade']]
faturamento_calça = calça_df['valor'] * calça_df['quantidade']

sapato_df = vendas_df.loc[vendas_df['produto'] == 'calça', ['produto', 'valor', 'quantidade']]
faturamento_sapato = sapato_df['valor'] * sapato_df['quantidade']

print('O faturamento de camisa é: ', faturamento_camisa.sum())
print('O faturamento de calça é: ', faturamento_calça.sum())
print('O faturamento de sapato é: ', faturamento_sapato.sum())

# Okay, agora que sei o faturamento, vou tentar montar um gráfico pra melhor vizualização

produtos = ['camisas', 'calças', 'sapatos']
faturamento_bruto = [
    faturamento_camisa.sum(),
    faturamento_calça.sum(),
    faturamento_sapato.sum()
]

# Decidi usar o gráfico de barra

plt.bar(produtos, faturamento_bruto, color=['#4285F4', '#EA4335', '#FBBC05'])
plt.title('Faturamento total por produto')
plt.xlabel('Produtos')
plt.xlabel('Faturamento (R$)')

plt.show()



