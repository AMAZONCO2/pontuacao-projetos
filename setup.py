import streamlit as st

#meta dados
st.set_page_config(
        page_title='ACC - Pontuação de projetos',
        page_icon=r"logo.jpg"                  
        )
# Dicionários com os valores de cada categoria
origem_valores = {
    "CONCORRÊNCIA PÚBLICA": 5,
    "PREFEITURAS": 4,
    "GOVERNOS": 5,
    "GRANDES INDÚSTRIAS": 4,
    "GRANDES EMPRESAS": 4,
    "GRANDES PROPRIEDADES": 4,
    "ASSOCIAÇÕES": 3,
    "COMUNIDADES": 3,
    "MÉDIAS EMPRESAS": 2,
    "MÉDIAS INDÚSTRIAS": 2,
    "MÉDIAS PROPRIEDADES": 2,
    "PEQUENAS PROPRIEDADES": 1,
    "PEQUENAS EMPRESAS": 1,
    "PEQUENAS INDÚSTRIAS": 1,
}

potencial_receita_valores = {
    "PEQUENO": 1,
    "MÉDIO": 2,
    "GRANDE": 4,
    "GIGANTE": 5,
}

elegibilidade_valores = {
    "SIM": 5,
    "NÃO": 1,
}

tipo_projeto_valores = {
    "ARR": 5,
    "REDD+": 4,
    "REDD": 3,
    "ALM": 2,
    "CRIEE": 1,
}

complexidade_valores = {
    "ARR": 1,
    "REDD+": 2,
    "REDD": 3,
    "ALM": 3,
    "CRIEE": 5,
}

prazo_entrega_valores = {
    "CURTO": 5,
    "MÉDIO": 3,
    "LONGO": 2,
}

# Função para calcular o valor total
def calcular_valor_total(origem, elegibilidade, potencial_receita, tipo_projeto, complexidade, prazo_entrega):
    valor_total = (origem_valores[origem] +
                   elegibilidade_valores[elegibilidade] +
                   (potencial_receita_valores[potencial_receita]*3) +
                   (tipo_projeto_valores[tipo_projeto] *2)+
                   complexidade_valores[complexidade] +
                   prazo_entrega_valores[prazo_entrega])
    return valor_total

# Interface do Streamlit
st.title("Calculadora de Valor de Projetos")



origem = st.selectbox("Origem", list(origem_valores.keys()))
elegibilidade = st.selectbox("Elegibilidade", list(elegibilidade_valores.keys()))
potencial_receita = st.selectbox("Potencial de Receita", list(potencial_receita_valores.keys()))
tipo_projeto = st.selectbox("Tipo de Projeto", list(tipo_projeto_valores.keys()))
complexidade = st.selectbox("Complexidade", list(complexidade_valores.keys()))
prazo_entrega = st.selectbox("Prazo de Entrega", list(prazo_entrega_valores.keys()))

def tipo_demanda(valor):
  if valor<=19:
    return "DEMANDA"
  if valor<=30:
    return "PRÉ-PROJETO"
  if valor<=40:
    return "PROJETO"
  
def prazo_entrega_total(valor):
  if valor == "DEMANDA":
    return "2 DIAS"
  if valor == "PRÉ-PROJETO":
    return "15 DIAS"
  if valor == "PROJETO":
    return "25 DIAS"
  
def documentos(valor):
  if valor == "DEMANDA":
    return "Análise Prévia / NDA"
  if valor == "PRÉ-PROJETO":
    return "Proposta Técnica e comercial / MOU"
  if valor == "PROJETO":
    return "Planejamento / CONTRATO"

if st.button("Calcular Valor Total"):
    valor_total = calcular_valor_total(origem, elegibilidade, potencial_receita, tipo_projeto, complexidade, prazo_entrega)
    resultado = tipo_demanda(valor_total)
    prazo = prazo_entrega_total(resultado)
    documento = documentos(resultado)
    st.text(f"O valor do projeto é: {valor_total}")
    st.text(f"O prazo de entrega é: {prazo}")
    st.text(f'Os documentos necessários são: {documento}')
    st.success(f"{resultado}")
