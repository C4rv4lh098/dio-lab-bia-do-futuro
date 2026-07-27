# CapabiliAI — Passo a Passo de Execução

O CapabiliAI é um agente inteligente desenvolvido para auxiliar no tratamento de dados e na interpretação de índices de capabilidade de processos industriais.

A aplicação utiliza:

- Python para validação, tratamento e cálculos estatísticos;
- Streamlit para a interface;
- Ollama para executar o modelo de linguagem localmente;
- arquivos Markdown e JSON como Base de Conhecimento.

---

## Estrutura do Projeto

```text
projeto/
├── data/
│   ├── conceitos_capabilidade.md
│   ├── criterios_interpretacao.json
│   ├── formulas.md
│   ├── limitacoes.md
│   └── exemplos_respostas.md
│
├── src/
│   ├── app.py
│   ├── analise.py
│   ├── llm.py
│   ├── prompts.py
│   └── README.md
│
└── requirements.txt
```

---

## Responsabilidade dos Arquivos

| Arquivo | Responsabilidade |
|---|---|
| `app.py` | Interface Streamlit e integração entre os módulos |
| `analise.py` | Validação, tratamento e cálculos estatísticos |
| `llm.py` | Comunicação com o Ollama |
| `prompts.py` | Carregamento da Base de Conhecimento e montagem do prompt |
| `requirements.txt` | Dependências Python do projeto |

---

# Setup do Ollama

## 1. Instalar o Ollama

Baixe e instale o Ollama pelo site oficial:

```text
https://ollama.com
```

## 2. Baixar o modelo

```bash
ollama pull gpt-oss
```

## 3. Verificar os modelos instalados

```bash
ollama list
```

## 4. Testar o modelo

```bash
ollama run gpt-oss "Explique de forma simples o que é Cpk."
```

## 5. Iniciar o serviço do Ollama

Caso o Ollama não esteja em execução:

```bash
ollama serve
```

Em alguns sistemas, o Ollama já é iniciado automaticamente após a instalação.

---

# Configuração do Ambiente Python

## 1. Acessar a pasta do projeto

```bash
cd caminho\para\o\projeto
```

## 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

No Linux ou macOS:

```bash
python3 -m venv .venv
```

## 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Windows Prompt de Comando:

```cmd
.venv\Scripts\activate.bat
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

## 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` ainda não esteja disponível:

```bash
pip install streamlit pandas requests
```

---

# Como Executar

Na pasta raiz do projeto, execute:

```bash
streamlit run .\src\app.py
```

No Linux ou macOS:

```bash
streamlit run ./src/app.py
```

Após a inicialização, a aplicação normalmente estará disponível em:

```text
http://localhost:8501
```

---

# Como Utilizar a Aplicação

1. Carregue um arquivo CSV contendo as medições do processo.
2. Selecione o separador utilizado no arquivo.
3. Selecione a coluna que contém os valores das medições.
4. Informe o Limite Inferior de Especificação — LIE.
5. Informe o Limite Superior de Especificação — LSE.
6. Clique em **Executar análise**.
7. Consulte os resultados estatísticos apresentados.
8. Faça perguntas ao CapabiliAI sobre a interpretação dos resultados.

---

# Formato Esperado do CSV

O arquivo deve possuir pelo menos uma coluna contendo valores numéricos.

Exemplo:

```csv
medicao
49.92
50.05
49.87
50.11
49.98
```

Também podem existir outras colunas:

```csv
data,maquina,turno,medicao
2026-07-01,M01,Manhã,49.92
2026-07-01,M01,Manhã,50.05
2026-07-01,M01,Tarde,49.87
2026-07-01,M01,Tarde,50.11
```

A coluna utilizada nos cálculos será escolhida na interface.

---

# Fluxo de Execução

```text
Arquivo CSV
     │
     ▼
Interface Streamlit
     │
     ▼
Validação e tratamento dos dados
     │
     ▼
Cálculos estatísticos em Python
     │
     ▼
Cp, Cpu, Cpl e Cpk
     │
     ▼
Base de Conhecimento
     │
     ▼
Ollama
     │
     ▼
Interpretação em linguagem natural
```

---

# Base de Conhecimento

A aplicação utiliza os seguintes arquivos:

| Arquivo | Conteúdo |
|---|---|
| `conceitos_capabilidade.md` | Conceitos sobre capabilidade |
| `criterios_interpretacao.json` | Critérios de classificação |
| `formulas.md` | Fórmulas estatísticas |
| `limitacoes.md` | Limitações e regras de segurança |
| `exemplos_respostas.md` | Exemplos de respostas esperadas |

Os cálculos são realizados pelo Python.

O modelo de linguagem utiliza a Base de Conhecimento apenas para interpretar e explicar os resultados.

---

# Solução de Problemas

## Erro de conexão com o Ollama

Verifique se o serviço está em execução:

```bash
ollama serve
```

Teste o modelo diretamente:

```bash
ollama run gpt-oss "Olá!"
```

---

## Modelo não encontrado

Baixe novamente o modelo:

```bash
ollama pull gpt-oss
```

Confira o nome instalado:

```bash
ollama list
```

O nome configurado no arquivo `llm.py` deve ser igual ao nome exibido pelo comando `ollama list`.

---

## Streamlit não encontrado

Instale o Streamlit:

```bash
pip install streamlit
```

Ou execute utilizando o módulo Python:

```bash
python -m streamlit run .\src\app.py
```

---

## Erro ao localizar a Base de Conhecimento

Confirme se a pasta `data` está na raiz do projeto e contém os cinco arquivos obrigatórios.

```text
projeto/
├── data/
└── src/
```

O diretório `data` não deve ficar dentro de `src`, a menos que os caminhos definidos em `prompts.py` sejam alterados.

---

## Erro ao ler o CSV

Verifique:

- se o separador selecionado está correto;
- se o arquivo possui cabeçalho;
- se existe pelo menos uma coluna;
- se a coluna de medição possui valores numéricos;
- se a codificação do arquivo é compatível.

---

# Evidência de Execução

Após executar a aplicação, adicione nesta seção uma captura de tela atualizada do CapabiliAI.

Exemplo:

```html
<img
  width="1920"
  alt="Tela do CapabiliAI em execução"
  src="CAMINHO_OU_URL_DA_IMAGEM"
/>
```

---

# Observações Importantes

- O modelo de linguagem não realiza os cálculos estatísticos.
- O Python é responsável pelo tratamento dos dados e pelos indicadores.
- O agente não deve inventar limites ou resultados.
- Cp e Cpk não comprovam, isoladamente, a estabilidade estatística do processo.
- A aplicação funciona como apoio à análise e não substitui a avaliação de um profissional qualificado.
