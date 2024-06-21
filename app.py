import pandas as pd
import matplotlib.pyplot as plt

vendas = pd.read_csv('csv/20240618_Vendas_BR_Mercado_Livre_2024-06-18_12-26hs_53766196 1(Vendas BR).csv', sep = ';', encoding='latin1', decimal=',')

vendas['frete real'] = vendas['Tarifas de envio'] + vendas['Receita por envio (BRL)']
fretePositivo = vendas['frete real'] - vendas['frete real'] - vendas['frete real']
vendas['Porcentagem frete'] = fretePositivo / (vendas['Receita por produtos (BRL)'] / 100)
frete30 = vendas[['N.º de venda', 'SKU', 'Receita por produtos (BRL)', 'Porcentagem frete', 'frete real']]
maior_frete = frete30[frete30['Porcentagem frete'] > 30].sort_values('Porcentagem frete')

maior_frete.sort_values('Porcentagem frete').plot.bar(x='SKU', y='Porcentagem frete')
plt.title('Vendas com frete maior que 30%')
plt.ylabel('Porcentagem frete')
plt.xlabel('')
plt.xticks(rotation=45, ha='right')
plt.show()
