# Base de Conhecimento

## Dados Utilizados

A Base de Conhecimento será composta por arquivos locais contendo conceitos, regras e critérios relacionados à análise de capabilidade de processos industriais.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|----------------------|
| `conceitos_capabilidade.md` | Markdown | Conceitos sobre Cp, Cpk, Pp e Ppk |
| `criterios_interpretacao.json` | JSON | Regras para classificação dos indicadores |
| `formulas.md` | Markdown | Fórmulas estatísticas utilizadas na análise |
| `limitacoes.md` | Markdown | Limitações, cuidados e boas práticas |
| `exemplos_respostas.md` | Markdown | Exemplos de interpretações geradas pelo agente |

---

## Organização da Base

A estrutura da Base de Conhecimento está organizada da seguinte forma:

```text
data/
├── conceitos_capabilidade.md
├── criterios_interpretacao.json
├── formulas.md
├── limitacoes.md
└── exemplos_respostas.md
```

Cada arquivo possui uma responsabilidade específica, permitindo que o modelo de linguagem consulte apenas as informações necessárias para interpretar os resultados produzidos pelo sistema.

---

## Como a Base é Utilizada

Durante a execução do agente, o fluxo será o seguinte:

1. O usuário envia um arquivo CSV contendo as medições do processo.
2. O Python realiza o tratamento dos dados e os cálculos estatísticos.
3. Os resultados calculados são organizados em um formato estruturado.
4. O LLM consulta a Base de Conhecimento para obter conceitos e critérios de interpretação.
5. O agente gera uma explicação técnica baseada nos resultados e nas informações da Base de Conhecimento.

A Base de Conhecimento **não realiza cálculos** e **não altera os dados enviados pelo usuário**. Sua função é fornecer contexto ao modelo de linguagem, garantindo respostas mais consistentes e reduzindo o risco de alucinações.

---

## Exemplo de Conteúdo

### `criterios_interpretacao.json`

```json
{
  "cpk_menor_1": {
    "classificacao": "Processo potencialmente incapaz",
    "descricao": "O processo apresenta risco de produzir itens fora dos limites de especificação."
  },
  "cpk_entre_1_e_1_33": {
    "classificacao": "Capacidade limitada",
    "descricao": "O processo atende parcialmente aos requisitos, sendo recomendada a redução da variabilidade."
  },
  "cpk_maior_1_33": {
    "classificacao": "Processo potencialmente capaz",
    "descricao": "O processo apresenta capacidade adequada em relação aos limites de especificação."
  }
}
```

---

## Benefícios da Base de Conhecimento

- Padroniza as interpretações dos resultados.
- Reduz respostas inconsistentes do modelo de linguagem.
- Centraliza conceitos e regras de negócio em arquivos de fácil manutenção.
- Permite atualizar critérios de interpretação sem alterar o código da aplicação.
- Facilita a expansão do agente para novas funcionalidades no futuro.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O tema inicialmente proposto para o agente foi alterado. Em vez de um agente voltado para educação financeira, optou-se pelo desenvolvimento de um agente especializado em **tratamento de dados e análise de capabilidade de processos industriais**.
Em função dessa mudança, foi necessário substituir os arquivos disponibilizados no projeto base do curso por novos arquivos relacionados ao domínio da qualidade e da estatística aplicada.
Dessa forma, a Base de Conhecimento passou a atender especificamente às necessidades do novo domínio da aplicação, mantendo a mesma arquitetura proposta no curso, porém com conteúdo adaptado ao contexto industrial.

---

## Estratégia de Integração

### Como os dados são carregados?

A Base de Conhecimento é composta por arquivos locais armazenados na pasta `data`. Esses arquivos são carregados pela aplicação em Python durante a inicialização do agente e utilizados para fornecer contexto ao modelo de linguagem.

Além da Base de Conhecimento, o agente recebe como entrada um arquivo CSV contendo as medições do processo industrial. Esse arquivo é enviado pelo usuário através da interface desenvolvida em Streamlit e processado durante a execução da análise.

Exemplo de carregamento dos arquivos:

```python
from pathlib import Path
import json

# Base de conhecimento
conceitos = Path("data/conceitos_capabilidade.md").read_text(encoding="utf-8")
limitacoes = Path("data/limitacoes.md").read_text(encoding="utf-8")
exemplos = Path("data/exemplos_respostas.md").read_text(encoding="utf-8")

with open("data/criterios_interpretacao.json", encoding="utf-8") as arquivo:
    criterios = json.load(arquivo)
```

Os dados enviados pelo usuário (CSV) são carregados utilizando a biblioteca Pandas.

```python
import pandas as pd

dados = pd.read_csv("medicoes.csv")
```

---

### Como os dados são usados no prompt?

Os cálculos estatísticos são realizados exclusivamente em Python.

Após a validação e processamento dos dados, os principais resultados (como média, desvio-padrão, Cp e Cpk) são organizados em um contexto estruturado e enviados ao LLM juntamente com a Base de Conhecimento.

Dessa forma, o modelo de linguagem recebe apenas as informações necessárias para interpretar os resultados, sem realizar cálculos estatísticos.

> Exemplo de contexto enviado ao modelo:

```text
Base de Conhecimento

- Conceitos sobre Cp e Cpk
- Critérios de interpretação
- Limitações da análise
- Exemplos de respostas

Resultados Calculados

Quantidade de medições: 250
Média: 10.02 mm
Desvio padrão: 0.05 mm
LIE: 9.90 mm
LSE: 10.10 mm

Cp: 1.33
Cpk: 1.28

Objetivo:
Interpretar os resultados de forma técnica, destacando a capacidade do processo, possíveis riscos e limitações da análise.
```

---

## Exemplo de Contexto Montado

> O exemplo abaixo representa o contexto enviado ao LLM após o processamento dos dados pelo Python.

```text
BASE DE CONHECIMENTO

- O índice Cp mede a capacidade potencial do processo.
- O índice Cpk considera a dispersão e o deslocamento da média.
- Um Cpk maior ou igual a 1,33 indica, em geral, um processo potencialmente capaz.
- O Cpk não deve ser utilizado isoladamente para afirmar que um processo está sob controle estatístico.

RESULTADOS DA ANÁLISE

Quantidade de medições: 250

Média: 10,02 mm

Desvio padrão: 0,05 mm

Limite Inferior (LIE): 9,90 mm

Limite Superior (LSE): 10,10 mm

Cp: 1,33

Cpk: 1,28

TAREFA DO AGENTE

Interpretar os resultados apresentados, explicando o significado dos indicadores, os pontos de atenção encontrados e as limitações da análise. Não realize novos cálculos nem invente informações que não estejam presentes no contexto.
```
