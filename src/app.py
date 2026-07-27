import pandas as pd
import streamlit as st

from analise import (
    calcular_capabilidade,
    classificar_cpk,
    preparar_medicoes,
)
from llm import ErroOllama, consultar_ollama
from prompts import carregar_base_conhecimento, montar_prompt


st.set_page_config(
    page_title="CapabiliAI",
    page_icon="📊",
    layout="wide",
)


@st.cache_resource
def obter_base_conhecimento():
    """
    Carrega a Base de Conhecimento apenas uma vez durante a execução
    da aplicação.
    """
    return carregar_base_conhecimento()


def limpar_estado_analise():
    """
    Remove do estado da aplicação os resultados da análise anterior.
    """
    st.session_state.pop("resultados", None)
    st.session_state.pop("tratamentos", None)
    st.session_state.pop("medicoes", None)
    st.session_state.pop("mensagens", None)


st.title("📊 CapabiliAI")
st.caption(
    "Agente inteligente para tratamento de dados e interpretação "
    "de capabilidade de processos industriais."
)

try:
    base_conhecimento = obter_base_conhecimento()
except (FileNotFoundError, ValueError) as erro:
    st.error(f"Erro ao carregar a Base de Conhecimento: {erro}")
    st.stop()


with st.sidebar:
    st.header("Configuração da análise")

    arquivo_csv = st.file_uploader(
        "Carregue o arquivo de medições",
        type=["csv"],
        help="O arquivo deve conter pelo menos uma coluna numérica.",
        on_change=limpar_estado_analise,
    )

    separador = st.selectbox(
        "Separador do CSV",
        options=[",", ";", "\t"],
        format_func=lambda valor: {
            ",": "Vírgula (,)",
            ";": "Ponto e vírgula (;)",
            "\t": "Tabulação",
        }[valor],
    )


if arquivo_csv is None:
    st.info(
        "Carregue um arquivo CSV para iniciar a análise."
    )

    st.markdown(
        """
        ### Formato de exemplo

        ```csv
        medicao
        49.92
        50.05
        49.87
        50.11
        ```
        """
    )

    st.stop()


try:
    dataframe = pd.read_csv(
        arquivo_csv,
        sep=separador,
    )
except Exception as erro:
    st.error(f"Não foi possível ler o arquivo CSV: {erro}")
    st.stop()


if dataframe.empty:
    st.warning("O arquivo CSV não contém registros.")
    st.stop()


st.subheader("1. Visualização dos dados")

st.dataframe(
    dataframe.head(100),
    use_container_width=True,
)


colunas = dataframe.columns.tolist()

coluna_medicao = st.selectbox(
    "Selecione a coluna que contém as medições",
    options=colunas,
)


coluna_lie, coluna_lse = st.columns(2)

with coluna_lie:
    lie = st.number_input(
        "Limite Inferior de Especificação — LIE",
        value=0.0,
        format="%.6f",
    )

with coluna_lse:
    lse = st.number_input(
        "Limite Superior de Especificação — LSE",
        value=1.0,
        format="%.6f",
    )


if st.button(
    "Executar análise",
    type="primary",
    use_container_width=True,
):
    try:
        medicoes, tratamentos = preparar_medicoes(
            dataframe=dataframe,
            coluna=coluna_medicao,
        )

        resultados = calcular_capabilidade(
            medicoes=medicoes,
            lie=lie,
            lse=lse,
        )

        st.session_state["medicoes"] = medicoes
        st.session_state["tratamentos"] = tratamentos
        st.session_state["resultados"] = resultados
        st.session_state["mensagens"] = []

    except ValueError as erro:
        st.error(str(erro))


if "resultados" not in st.session_state:
    st.stop()


resultados = st.session_state["resultados"]
tratamentos = st.session_state["tratamentos"]
medicoes = st.session_state["medicoes"]


st.divider()
st.subheader("2. Qualidade e tratamento dos dados")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Registros originais",
    tratamentos["quantidade_original"],
)

col2.metric(
    "Medições válidas",
    tratamentos["quantidade_valida"],
)

col3.metric(
    "Ausentes ou inválidos",
    tratamentos["quantidade_invalidos_ou_ausentes"],
)

col4.metric(
    "Duplicados identificados",
    tratamentos["quantidade_duplicados"],
)

if tratamentos["quantidade_invalidos_ou_ausentes"] > 0:
    st.warning(
        "Os registros ausentes ou não numéricos foram desconsiderados "
        "nos cálculos."
    )

if tratamentos["quantidade_duplicados"] > 0:
    st.info(
        "Foram encontrados valores duplicados. Eles foram mantidos, "
        "pois podem representar medições válidas do processo."
    )


st.subheader("3. Resultados estatísticos")

linha1_col1, linha1_col2, linha1_col3, linha1_col4 = st.columns(4)

linha1_col1.metric(
    "Média",
    f"{resultados['media']:.4f}",
)

linha1_col2.metric(
    "Desvio-padrão",
    f"{resultados['desvio_padrao']:.4f}",
)

linha1_col3.metric(
    "Mínimo",
    f"{resultados['minimo']:.4f}",
)

linha1_col4.metric(
    "Máximo",
    f"{resultados['maximo']:.4f}",
)


linha2_col1, linha2_col2, linha2_col3, linha2_col4 = st.columns(4)

linha2_col1.metric(
    "Cp",
    f"{resultados['cp']:.3f}",
)

linha2_col2.metric(
    "Cpk",
    f"{resultados['cpk']:.3f}",
)

linha2_col3.metric(
    "Fora da especificação",
    resultados["fora_especificacao"],
)

linha2_col4.metric(
    "Percentual fora",
    f"{resultados['percentual_fora_especificacao']:.2f}%",
)


classificacao = classificar_cpk(resultados["cpk"])

st.info(
    f"**Classificação geral pelo Cpk:** {classificacao}"
)

st.write(
    f"**Lado mais crítico:** {resultados['lado_critico']}"
)

st.caption(resultados["observacao_metodologica"])


st.subheader("4. Distribuição das medições")

grafico = pd.DataFrame(
    {
        "Medição": medicoes.reset_index(drop=True)
    }
)

st.line_chart(
    grafico,
    y="Medição",
    use_container_width=True,
)


st.divider()
st.subheader("5. Interpretação com o CapabiliAI")

st.caption(
    "O modelo interpreta os resultados calculados pelo Python. "
    "Ele não realiza nem altera os cálculos estatísticos."
)


for mensagem in st.session_state["mensagens"]:
    with st.chat_message(mensagem["papel"]):
        st.markdown(mensagem["conteudo"])


pergunta_usuario = st.chat_input(
    "Pergunte sobre os resultados da análise..."
)


if pergunta_usuario:
    st.session_state["mensagens"].append(
        {
            "papel": "user",
            "conteudo": pergunta_usuario,
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta_usuario)

    prompt = montar_prompt(
        resultados=resultados,
        pergunta_usuario=pergunta_usuario,
        base_conhecimento=base_conhecimento,
    )

    with st.chat_message("assistant"):
        with st.spinner("Analisando os resultados..."):
            try:
                resposta = consultar_ollama(prompt)
                st.markdown(resposta)

                st.session_state["mensagens"].append(
                    {
                        "papel": "assistant",
                        "conteudo": resposta,
                    }
                )

            except ErroOllama as erro:
                st.error(str(erro))
