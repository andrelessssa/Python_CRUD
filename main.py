import streamlit as st;


with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira Seu nome")
    input_age = st.number_input(label="Digite sua idade", format="%d", step=1)
    input_occupation = st.selectbox(label="Selecione Sua profissão", options=["Desenvolvedor", "Músico"])
    input_button_submit = st.form_submit_button("Enviar") 

if input_button_submit:
    st.write(f"Olá {input_name}, você tem {input_age} anos e é {input_occupation}.")