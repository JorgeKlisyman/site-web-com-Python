import streamlit as st
st.title("Cadastro de Clientes")


nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o Endereço")
dt_nasc = st.date_input("Escolha a data de nascimento")
tipo_cliente = st.selectbox("Tipo de cliente", 
                            {"Pessoa fisica", "Pessoa juridica" })

cadastrar = st.button("Cadastrar cliente")

if cadastrar: 
    with open("clientes.cvs", "a") as arquivo: 
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso!")
        
       
# Adiciona o CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #1E90FF;
        text-align: center;
    }
    .stButton button {
        background-color: #1E90FF;
        color: white;
        padding: 10px;
        border-radius: 5px;
    }
    .stTextInput input {
        border: 2px solid #1E90FF;
        padding: 5px;
        border-radius: 5px;
    }
    .stDateInput input {
        border: 2px solid #1E90FF;
        padding: 5px;
        border-radius: 5px;
    }
    .stSelectbox select {
        border: 2px solid #1E90FF;
        padding: 5px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)