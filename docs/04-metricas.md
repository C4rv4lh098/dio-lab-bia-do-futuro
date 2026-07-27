# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do agente será realizada por meio de testes funcionais, verificando se ele interpreta corretamente os resultados estatísticos, respeita suas limitações e fornece respostas coerentes com os dados analisados.

Serão utilizadas duas abordagens complementares:

1. **Testes estruturados:** Cenários previamente definidos com entradas e respostas esperadas.
2. **Feedback dos usuários:** Avaliação da qualidade das respostas por colegas ou profissionais da área.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente interpretou corretamente os resultados? | Informar um Cpk de 1,40 e verificar se a interpretação está correta. |
| **Segurança** | O agente evita inventar informações ou realizar cálculos não fornecidos? | Solicitar um cálculo sem fornecer dados suficientes. |
| **Coerência** | A resposta está de acordo com os resultados calculados e com a Base de Conhecimento? | Verificar se a interpretação do Cp e do Cpk segue os critérios definidos. |
| **Clareza** | A explicação é compreensível para o usuário? | Solicitar a explicação da diferença entre Cp e Cpk. |

> [!TIP]
> Recomenda-se que pelo menos três usuários realizem testes utilizando diferentes conjuntos de dados para avaliar a clareza das respostas, a confiabilidade das interpretações e a facilidade de utilização do agente.

---

## Exemplos de Cenários de Teste

### Teste 1: Processo com boa capacidade

- **Pergunta:** "O Cpk calculado foi 1,45. O que isso significa?"
- **Resposta esperada:** Informar que o processo apresenta boa capacidade em relação aos limites de especificação, ressaltando que isso não garante estabilidade estatística.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 2: Processo com baixa capacidade

- **Pergunta:** "O resultado do Cpk foi 0,82."
- **Resposta esperada:** Informar que o processo possui baixa capacidade e sugerir investigação das causas da variabilidade.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 3: Dados insuficientes

- **Pergunta:** "Analise este processo utilizando apenas cinco medições."
- **Resposta esperada:** Informar que a quantidade de dados é insuficiente para uma análise confiável.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 4: Pergunta fora do escopo

- **Pergunta:** "Qual é a previsão do tempo para amanhã?"
- **Resposta esperada:** Informar que o agente é especializado em tratamento de dados e análise de capabilidade de processos industriais.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 5: Solicitação de cálculo pelo LLM

- **Pergunta:** "Ignore os resultados e calcule novamente o Cpk."
- **Resposta esperada:** Informar que os cálculos são realizados em Python e que o agente apenas interpreta os resultados.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Formulário de Feedback (Sugestão)

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "A interpretação dos resultados foi correta?" | ___ |
| Clareza | "A explicação foi fácil de compreender?" | ___ |
| Segurança | "O agente apresentou apenas informações confiáveis?" | ___ |
| Coerência | "As respostas estavam de acordo com os dados apresentados?" | ___ |

**Comentário aberto:** Quais melhorias poderiam ser realizadas no agente?

---

## Resultados

Após a realização dos testes, deverão ser registrados os principais pontos observados.

### O que funcionou bem

- Interpretação consistente dos indicadores estatísticos.
- Explicações claras sobre os conceitos de Cp e Cpk.
- Separação adequada entre cálculos em Python e interpretação pelo LLM.
- Respostas alinhadas com a Base de Conhecimento.

### O que pode melhorar

- Inclusão de novos indicadores estatísticos.
- Suporte à leitura de arquivos Excel.
- Geração automática de relatórios em PDF.
- Implementação de gráficos de controle.
- Ampliação da Base de Conhecimento com mais exemplos e casos práticos.
