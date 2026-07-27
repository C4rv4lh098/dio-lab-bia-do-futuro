import os

import requests


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate",
)

MODELO_OLLAMA = os.getenv(
    "MODELO_OLLAMA",
    "gpt-oss",
)


class ErroOllama(Exception):
    """
    Erro personalizado para falhas de comunicação com o Ollama.
    """


def consultar_ollama(
    prompt: str,
    modelo: str = MODELO_OLLAMA,
    timeout: int = 180,
) -> str:
    """
    Envia o prompt para o Ollama e retorna a resposta do modelo.
    """
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
        },
    }

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=timeout,
        )

        resposta.raise_for_status()

    except requests.exceptions.ConnectionError as erro:
        raise ErroOllama(
            "Não foi possível conectar ao Ollama. Verifique se o "
            "serviço está em execução em http://localhost:11434."
        ) from erro

    except requests.exceptions.Timeout as erro:
        raise ErroOllama(
            "O Ollama demorou mais que o esperado para responder."
        ) from erro

    except requests.exceptions.HTTPError as erro:
        raise ErroOllama(
            f"O Ollama retornou um erro HTTP: {erro}"
        ) from erro

    try:
        dados = resposta.json()
    except ValueError as erro:
        raise ErroOllama(
            "O Ollama retornou uma resposta em formato inválido."
        ) from erro

    texto = dados.get("response")

    if not texto:
        mensagem_erro = dados.get(
            "error",
            "O modelo não retornou uma resposta.",
        )
        raise ErroOllama(mensagem_erro)

    return texto.strip()
