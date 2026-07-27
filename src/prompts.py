import json
from pathlib import Path
from typing import Any


DIRETORIO_BASE = Path(__file__).resolve().parent.parent
DIRETORIO_DADOS = DIRETORIO_BASE / "data"


SYSTEM_PROMPT = """
Você é o CapabiliAI, um assistente especializado na interpretação
de análises de capabilidade de processos industriais.

OBJETIVO:
Explicar os resultados estatísticos calculados pela aplicação Python
de maneira clara, técnica, didática e responsável.

REGRAS:
- Utilize somente os dados e resultados fornecidos no contexto.
- Não invente valores, resultados, limites ou informações.
- Não refaça cálculos estatísticos.
- Os cálculos são responsabilidade exclusiva da aplicação Python.
- Diferencie fatos observados de possíveis hipóteses.
- Não afirme que o processo está estatisticamente estável com base
  apenas nos valores de Cp ou Cpk.
- Não determine causa-raiz sem evidências.
- Não aprove ou reprove produtos, lotes ou processos.
- Quando faltarem informações, informe claramente a limitação.
- Perguntas fora do tema de tratamento de dados e capabilidade devem
  ser recusadas educadamente.
- Use linguagem técnica, mas acessível.
- Seja objetivo e evite repetições.

ESTRUTURA PREFERENCIAL DA RESPOSTA:
1. Resumo da análise
2. Interpretação dos indicadores
3. Pontos de atenção
4. Limitações
5. Próximos passos sugeridos
"""


def ler_arquivo_markdown(nome_arquivo: str) -> str:
    """
    Lê um arquivo Markdown da pasta data.
    """
    caminho = DIRETORIO_DADOS / nome_arquivo

    if not caminho.exists():
        raise FileNotFoundError(
            f"O arquivo da Base de Conhecimento não foi encontrado: "
            f"{caminho}"
        )

    return caminho.read_text(encoding="utf-8")


def ler_arquivo_json(nome_arquivo: str) -> dict[str, Any]:
    """
    Lê um arquivo JSON da pasta data.
    """
    caminho = DIRETORIO_DADOS / nome_arquivo

    if not caminho.exists():
        raise FileNotFoundError(
            f"O arquivo da Base de Conhecimento não foi encontrado: "
            f"{caminho}"
        )

    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_base_conhecimento() -> dict[str, Any]:
    """
    Carrega os cinco arquivos definidos na documentação.
    """
    return {
        "conceitos": ler_arquivo_markdown(
            "conceitos_capabilidade.md"
        ),
        "criterios": ler_arquivo_json(
            "criterios_interpretacao.json"
        ),
        "formulas": ler_arquivo_markdown(
            "formulas.md"
        ),
        "limitacoes": ler_arquivo_markdown(
            "limitacoes.md"
        ),
        "exemplos": ler_arquivo_markdown(
            "exemplos_respostas.md"
        ),
    }


def formatar_resultados(resultados: dict[str, Any]) -> str:
    """
    Converte o dicionário de resultados em um texto estruturado
    para o modelo de linguagem.
    """
    return f"""
Quantidade de medições válidas: {resultados['quantidade']}
Média: {resultados['media']:.6f}
Mediana: {resultados['mediana']:.6f}
Desvio-padrão amostral: {resultados['desvio_padrao']:.6f}
Valor mínimo: {resultados['minimo']:.6f}
Valor máximo: {resultados['maximo']:.6f}
Amplitude: {resultados['amplitude']:.6f}

Limite Inferior de Especificação: {resultados['lie']:.6f}
Limite Superior de Especificação: {resultados['lse']:.6f}
Centro da especificação: {resultados['centro_especificacao']:.6f}
Deslocamento da média em relação ao centro:
{resultados['deslocamento_centro']:.6f}

Cp: {resultados['cp']:.4f}
Cpu: {resultados['cpu']:.4f}
Cpl: {resultados['cpl']:.4f}
Cpk: {resultados['cpk']:.4f}

Lado mais crítico: {resultados['lado_critico']}

Medições abaixo do LIE: {resultados['abaixo_lie']}
Medições acima do LSE: {resultados['acima_lse']}
Total fora da especificação: {resultados['fora_especificacao']}
Percentual observado fora da especificação:
{resultados['percentual_fora_especificacao']:.2f}%

Observação metodológica:
{resultados['observacao_metodologica']}
"""


def montar_prompt(
    resultados: dict[str, Any],
    pergunta_usuario: str,
    base_conhecimento: dict[str, Any],
) -> str:
    """
    Monta o prompt completo enviado ao modelo.
    """
    criterios_json = json.dumps(
        base_conhecimento["criterios"],
        indent=2,
        ensure_ascii=False,
    )

    resultados_formatados = formatar_resultados(resultados)

    return f"""
{SYSTEM_PROMPT}

==================================================
BASE DE CONHECIMENTO — CONCEITOS
==================================================

{base_conhecimento['conceitos']}

==================================================
BASE DE CONHECIMENTO — CRITÉRIOS
==================================================

{criterios_json}

==================================================
BASE DE CONHECIMENTO — FÓRMULAS
==================================================

{base_conhecimento['formulas']}

==================================================
BASE DE CONHECIMENTO — LIMITAÇÕES
==================================================

{base_conhecimento['limitacoes']}

==================================================
BASE DE CONHECIMENTO — EXEMPLOS DE RESPOSTAS
==================================================

{base_conhecimento['exemplos']}

==================================================
RESULTADOS CALCULADOS PELO PYTHON
==================================================

{resultados_formatados}

==================================================
PERGUNTA DO USUÁRIO
==================================================

{pergunta_usuario}

Responda apenas com a interpretação. Não repita integralmente a Base
de Conhecimento e não realize novos cálculos.
"""
