import streamlit as st

def calcular_porcentagem_faltas(faltas, totalaulas):
    if faltas > totalaulas:
        raise ValueError('O número de faltas não pode ser maior do que o total de aulas.')
    return ((totalaulas - faltas) / totalaulas) * 100

st.title('Calculadora de faltas IFRN')
st.write('Calculadora simples para saber sua porcentagem de faltas em uma disciplina do IFRN')

totalaulas = st.number_input('Total de aulas', 1, 100)
faltas = st.number_input('Quantidade de faltas', 0, 100)

try:
    porcentagem = calcular_porcentagem_faltas(faltas, totalaulas)

    emoji = ':smile:'
    if porcentagem >= 90:
        emoji = ':grinning:'
    elif porcentagem >= 80:
        emoji = ':slightly_smiling_face:'
    elif porcentagem >= 75:
        emoji = ':neutral_face:'
    elif porcentagem >= 70:
        emoji = ':slightly_frowning_face:'
    elif porcentagem >= 60:
        emoji = ':white_frowning_face:'
    elif porcentagem >= 50:
        emoji = ':anguished:'
    elif porcentagem >= 40:
        emoji = ':disappointed_relieved:'
    elif porcentagem >= 30:
        emoji = ':cry:'
    elif porcentagem >= 20:
        emoji = ':cold_sweat:'
    elif porcentagem >= 10:
        emoji = ':sob:'
    else:
        emoji = ':scream:'

    if porcentagem >= 75:
        st.success(f'Você tem {porcentagem:.2f}% de presença! {emoji}')
    else:
        st.error(f'Você tem {porcentagem:.2f}% de presença. {emoji}')
except ValueError as erro:
    st.error(str(erro))

st.markdown('---')
st.header('Sobre')
st.text('Fórmula: ((total de aulas - faltas) / total de aulas) * 100')