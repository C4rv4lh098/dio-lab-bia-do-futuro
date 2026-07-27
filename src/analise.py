from typing import Any

import pandas as pd


def preparar_medicoes(
    dataframe: pd.DataFrame,
    coluna: str,
) -> tuple[pd.Series, dict[str, int]]:
    """
    Converte a coluna selecionada para formato numérico e remove
    registros que não podem ser utilizados nos cálculos.

    Retorna:
        - Série contendo apenas medições numéricas válidas;
        - Informações sobre os tratamentos aplicados.
    """
    if coluna not in dataframe.columns:
        raise ValueError(f"A coluna '{coluna}' não existe no arquivo.")

    quantidade_original = len(dataframe)

    valores_convertidos = pd.to_numeric(
        dataframe[coluna],
        errors="coerce",
    )

    quantidade_nao_numericos = int(valores_convertidos.isna().sum())

    medicoes = valores_convertidos.dropna()

    quantidade_duplicados = int(medicoes.duplicated().sum())

    informacoes = {
        "quantidade_original": quantidade_original,
        "quantidade_valida": len(medicoes),
        "quantidade_invalidos_ou_ausentes": quantidade_nao_numericos,
        "quantidade_duplicados": quantidade_duplicados,
    }

    return medicoes, informacoes


def validar_analise(
    medicoes: pd.Series,
    lie: float,
    lse: float,
) -> None:
    """
    Verifica se existem condições mínimas para realizar os cálculos.
    """
    if lie >= lse:
        raise ValueError(
            "O Limite Inferior de Especificação deve ser menor que "
            "o Limite Superior de Especificação."
        )

    if len(medicoes) < 2:
        raise ValueError(
            "São necessárias pelo menos duas medições válidas."
        )

    if medicoes.nunique() < 2:
        raise ValueError(
            "As medições não possuem variação suficiente para calcular "
            "o desvio-padrão e os índices de capabilidade."
        )


def calcular_capabilidade(
    medicoes: pd.Series,
    lie: float,
    lse: float,
) -> dict[str, Any]:
    """
    Calcula estatísticas descritivas e índices de capabilidade.

    Nesta versão inicial, Cp e Cpk utilizam o desvio-padrão amostral
    geral. Para uma análise industrial mais avançada, o desvio-padrão
    de curto prazo deve ser estimado a partir de subgrupos racionais.
    """
    validar_analise(medicoes, lie, lse)

    quantidade = int(medicoes.count())
    media = float(medicoes.mean())
    mediana = float(medicoes.median())
    desvio_padrao = float(medicoes.std(ddof=1))
    minimo = float(medicoes.min())
    maximo = float(medicoes.max())
    amplitude = maximo - minimo

    if desvio_padrao == 0:
        raise ValueError(
            "O desvio-padrão é igual a zero. Não é possível calcular "
            "os índices de capabilidade."
        )

    cp = (lse - lie) / (6 * desvio_padrao)
    cpu = (lse - media) / (3 * desvio_padrao)
    cpl = (media - lie) / (3 * desvio_padrao)
    cpk = min(cpu, cpl)

    abaixo_lie = int((medicoes < lie).sum())
    acima_lse = int((medicoes > lse).sum())
    fora_especificacao = abaixo_lie + acima_lse

    percentual_fora = (fora_especificacao / quantidade) * 100

    centro_especificacao = (lie + lse) / 2
    deslocamento_centro = media - centro_especificacao

    if cpu < cpl:
        lado_critico = "Limite Superior de Especificação"
    elif cpl < cpu:
        lado_critico = "Limite Inferior de Especificação"
    else:
        lado_critico = "Ambos os limites apresentam a mesma distância"

    return {
        "quantidade": quantidade,
        "media": media,
        "mediana": mediana,
        "desvio_padrao": desvio_padrao,
        "minimo": minimo,
        "maximo": maximo,
        "amplitude": amplitude,
        "lie": float(lie),
        "lse": float(lse),
        "centro_especificacao": centro_especificacao,
        "deslocamento_centro": deslocamento_centro,
        "cp": float(cp),
        "cpu": float(cpu),
        "cpl": float(cpl),
        "cpk": float(cpk),
        "abaixo_lie": abaixo_lie,
        "acima_lse": acima_lse,
        "fora_especificacao": fora_especificacao,
        "percentual_fora_especificacao": percentual_fora,
        "lado_critico": lado_critico,
        "observacao_metodologica": (
            "Nesta versão, Cp e Cpk foram calculados com o "
            "desvio-padrão amostral geral. Não foram utilizados "
            "subgrupos racionais."
        ),
    }


def classificar_cpk(cpk: float) -> str:
    """
    Retorna uma classificação geral baseada no valor do Cpk.

    Os limites representam referências gerais e podem ser alterados
    conforme os requisitos da organização ou do cliente.
    """
    if cpk < 0:
        return "Média do processo fora de pelo menos um limite"

    if cpk < 1:
        return "Processo potencialmente incapaz"

    if cpk < 1.33:
        return "Capacidade limitada"

    if cpk < 1.67:
        return "Processo potencialmente capaz"

    return "Excelente capacidade"
