import pandas as pd
import plotly.express as px
import streamlit as st

st.sidebar.image('box7.png')
st.title('Vendas com Frete Alto')

file = st.sidebar.file_uploader("Carregue o arquivo em formato CSV", type=["csv"])

# Verificar se um arquivo foi carregado
if file is not None:
    vendas = pd.read_csv(file, sep=';', encoding='latin1', decimal=',')

    # Calculo de porcentagem de frete
    vendas['frete real'] = vendas['Tarifas de envio'] + vendas['Receita por envio (BRL)']
    fretePositivo = vendas['frete real'] - vendas['frete real'] - vendas['frete real']
    vendas['Porcentagem frete'] = fretePositivo / (vendas['Receita por produtos (BRL)'] / 100)
    frete30 = vendas[['N.º de venda', 'SKU', 'Receita por produtos (BRL)', 'Porcentagem frete', 'frete real']]
    maior_frete = frete30[frete30['Porcentagem frete'] > 30].sort_values('Porcentagem frete')
    media = vendas['frete real'].mean()


    fig = px.bar(maior_frete, x='SKU', y='Porcentagem frete',
                 title='Vendas com frete maior que 30%',
                 labels={'Porcentagem frete': 'Porcentagem frete', 'N.º de venda': 'N.º de venda'},
                 text='Porcentagem frete')

    # Ajustar a rotação do eixo x e alinhamento dos rótulos
    fig.update_xaxes(tickangle=45, tickmode='linear')

    # Exibir gráfico usando Streamlit
    if frete30 is not None:
        with st.expander("Vendas com frete maior que 30%"):
            st.markdown("----")
            st.plotly_chart(fig)
            st.markdown("----")
            st.write(maior_frete)
            st.markdown("----")
        with st.expander("Média de frete"):
            st.markdown(f'{media:.2f}')

    else:
        st.markdown("----")
        st.markdown("Não há vendas com frete maior que 30% no período informado")
else:
    st.write("Por favor, carregue um arquivo CSV.")
