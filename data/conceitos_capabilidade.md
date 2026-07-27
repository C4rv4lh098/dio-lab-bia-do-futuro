# Conceitos de Capabilidade de Processos

## Objetivo deste arquivo

Este documento reúne os principais conceitos utilizados pelo agente para interpretar análises de capabilidade de processos industriais.

As informações presentes neste arquivo servem como Base de Conhecimento para o modelo de linguagem. Os cálculos estatísticos devem ser realizados pelas rotinas em Python, e não pelo LLM.

---

## O que é Capabilidade de Processo?

A capabilidade de um processo representa sua capacidade de produzir resultados dentro dos limites de especificação definidos para uma determinada característica.

Essa análise compara:

- a variabilidade observada no processo;
- a posição da média do processo;
- os limites de especificação estabelecidos para o produto ou processo.

Uma análise de capabilidade pode ajudar a identificar se o processo possui condições de atender às especificações de forma consistente.

A capabilidade não deve ser interpretada apenas com base em um único índice. Também devem ser consideradas a estabilidade do processo, a qualidade dos dados, o sistema de medição, a distribuição dos dados e o tamanho da amostra.

---

## Limites de Especificação

Os limites de especificação representam os valores aceitáveis para uma característica do produto ou processo.

### Limite Inferior de Especificação — LIE

É o menor valor permitido para a característica analisada.

### Limite Superior de Especificação — LSE

É o maior valor permitido para a característica analisada.

### Valor nominal

É o valor central ou desejado para a característica, quando definido pelo projeto.

Os limites de especificação são definidos a partir de requisitos técnicos, projetos, normas, desenhos, contratos ou necessidades do cliente.

Eles não devem ser calculados automaticamente com base nos dados do processo.

---

## Limites de Especificação e Limites de Controle

Limites de especificação e limites de controle possuem funções diferentes.

### Limites de especificação

- são definidos pelo projeto, cliente ou requisito técnico;
- representam os valores aceitáveis para o produto;
- não dependem diretamente do comportamento atual do processo.

### Limites de controle

- são calculados com base nos dados do processo;
- representam a variação estatística observada;
- são utilizados em gráficos de controle;
- ajudam a identificar causas especiais de variação.

Um processo pode estar sob controle estatístico e ainda assim produzir itens fora da especificação.

Também pode ocorrer de um processo apresentar resultados dentro da especificação, mas não estar estatisticamente estável.

---

## Média do Processo

A média representa o valor central das medições analisadas.

Ela é utilizada para verificar onde o processo está posicionado em relação ao LIE, ao LSE e ao valor nominal.

Quando a média está mais próxima de um dos limites de especificação, o processo pode apresentar maior risco de gerar resultados fora desse limite.

---

## Variabilidade do Processo

A variabilidade representa o quanto os resultados do processo se dispersam em torno da média.

Quanto maior a variabilidade, maior tende a ser o risco de ocorrência de resultados fora dos limites de especificação.

A variabilidade pode ser influenciada por fatores como:

- matéria-prima;
- máquina;
- método;
- mão de obra;
- sistema de medição;
- ambiente;
- desgaste de ferramentas;
- diferenças entre turnos;
- alterações de regulagem;
- causas especiais de variação.

A presença de variabilidade não significa necessariamente que exista um problema. Todo processo apresenta alguma variação. O objetivo da análise é avaliar se essa variação é estável e compatível com as especificações.

---

## Desvio-Padrão

O desvio-padrão é uma medida estatística utilizada para representar a dispersão dos dados em relação à média.

Um desvio-padrão pequeno indica que as medições estão mais concentradas próximas da média.

Um desvio-padrão elevado indica maior dispersão dos resultados.

Os índices de capabilidade utilizam o desvio-padrão para comparar a variação do processo com a faixa de especificação.

---

## Índice Cp

O Cp mede a capacidade potencial do processo.

Ele compara a largura da faixa de especificação com a variação estimada do processo.

O Cp considera apenas a dispersão dos dados e não considera a posição da média.

Por esse motivo, um processo pode apresentar Cp elevado e ainda assim possuir resultados próximos ou além de um dos limites de especificação, caso esteja descentrado.

### Interpretação geral do Cp

- Cp menor que 1: a variação do processo é maior que a faixa de especificação;
- Cp igual a 1: a variação estimada ocupa aproximadamente toda a faixa de especificação;
- Cp maior que 1: a variação estimada é menor que a faixa de especificação;
- Cp maior ou igual a 1,33: pode representar uma capacidade potencial adequada, dependendo do critério adotado pela organização.

Os critérios de aceitação podem variar entre empresas, clientes, produtos, processos e setores industriais.

---

## Índice Cpk

O Cpk mede a capacidade do processo considerando:

- a dispersão dos dados;
- a posição da média em relação aos limites de especificação.

O Cpk analisa separadamente a distância entre a média e cada limite de especificação. O menor resultado representa o lado mais crítico do processo.

### Interpretação geral do Cpk

- Cpk menor que 0: a média do processo está fora de pelo menos um dos limites de especificação;
- Cpk entre 0 e 1: existe risco relevante de produção fora da especificação;
- Cpk entre 1 e 1,33: o processo pode apresentar capacidade limitada ou pouca margem;
- Cpk maior ou igual a 1,33: o processo pode ser considerado potencialmente capaz, conforme o critério adotado;
- Cpk maior ou igual a 1,67: pode ser exigido para características especiais ou processos com maior nível de criticidade.

Esses valores são referências gerais. A classificação correta deve respeitar os critérios definidos pela organização ou pelo cliente.

---

## Relação entre Cp e Cpk

O Cp representa a capacidade potencial do processo.

O Cpk representa a capacidade considerando a centralização da média.

Quando Cp e Cpk possuem valores próximos, o processo tende a estar relativamente centralizado.

Quando o Cp é significativamente maior que o Cpk, isso pode indicar que o processo possui dispersão adequada, mas está deslocado em direção a um dos limites de especificação.

### Exemplo conceitual

Um processo pode apresentar:

- Cp = 1,60;
- Cpk = 0,90.

Nesse caso, a variabilidade potencialmente caberia dentro da faixa de especificação, mas a média do processo está deslocada para um dos lados.

---

## Índice Cpu

O Cpu avalia a capacidade do processo em relação ao Limite Superior de Especificação.

Ele mede a distância entre a média e o LSE em relação à variação do processo.

Um Cpu baixo indica que o limite superior é um ponto crítico.

---

## Índice Cpl

O Cpl avalia a capacidade do processo em relação ao Limite Inferior de Especificação.

Ele mede a distância entre a média e o LIE em relação à variação do processo.

Um Cpl baixo indica que o limite inferior é um ponto crítico.

O Cpk corresponde ao menor valor entre Cpu e Cpl.

---

## Índice Pp

O Pp avalia o desempenho global do processo.

Assim como o Cp, ele compara a faixa de especificação com a variabilidade do processo.

A principal diferença está no tipo de variação utilizada.

O Pp geralmente utiliza o desvio-padrão global dos dados, incluindo a variação observada ao longo de todo o período analisado.

---

## Índice Ppk

O Ppk avalia o desempenho global do processo considerando:

- a variabilidade total observada;
- a posição da média;
- a distância até os limites de especificação.

O Ppk está relacionado ao desempenho real observado no conjunto de dados analisado.

---

## Diferença entre Cp/Cpk e Pp/Ppk

Cp e Cpk são normalmente associados à capacidade potencial de curto prazo.

Pp e Ppk são normalmente associados ao desempenho global ou de longo prazo.

Em termos gerais:

- Cp avalia a dispersão potencial;
- Cpk avalia dispersão e centralização;
- Pp avalia a dispersão total observada;
- Ppk avalia dispersão total e centralização.

Quando Cpk e Ppk apresentam diferenças relevantes, isso pode indicar alterações no comportamento do processo ao longo do tempo, diferenças entre subgrupos ou presença de instabilidade.

---

## Processo Centralizado

Um processo é considerado centralizado quando sua média está posicionada de forma adequada em relação aos limites de especificação.

Em uma especificação bilateral simétrica, a média ideal geralmente fica próxima ao centro entre o LIE e o LSE.

Entretanto, o valor nominal nem sempre corresponde exatamente ao centro da especificação. A interpretação deve respeitar os requisitos técnicos do processo.

---

## Processo Estável

Um processo estável apresenta comportamento previsível ao longo do tempo, considerando apenas causas comuns de variação.

A estabilidade deve ser avaliada por ferramentas apropriadas, como gráficos de controle.

Os índices Cp e Cpk não confirmam, por si só, que o processo está estatisticamente estável.

Calcular a capabilidade de um processo instável pode produzir resultados pouco representativos ou enganosos.

---

## Causas Comuns e Causas Especiais

### Causas comuns

São fontes de variação naturais e permanentes do sistema.

Exemplos:

- pequenas diferenças de matéria-prima;
- variação normal do equipamento;
- pequenas alterações ambientais;
- limitações naturais do método.

### Causas especiais

São eventos não usuais que alteram o comportamento esperado do processo.

Exemplos:

- quebra de ferramenta;
- erro de regulagem;
- matéria-prima fora do padrão;
- falha de equipamento;
- erro de medição;
- troca inadequada de parâmetro;
- alteração inesperada de temperatura.

A presença de causas especiais deve ser investigada antes de conclusões definitivas sobre a capabilidade.

---

## Normalidade dos Dados

Muitos métodos tradicionais de capabilidade assumem que os dados seguem aproximadamente uma distribuição normal.

Quando essa condição não é atendida, os índices calculados com métodos tradicionais podem gerar interpretações inadequadas.

Antes de interpretar a capabilidade, recomenda-se avaliar:

- histograma;
- gráfico de probabilidade;
- assimetria;
- presença de múltiplos grupos;
- possíveis misturas de processos;
- testes de normalidade, quando aplicáveis.

A reprovação em um teste de normalidade não deve ser interpretada automaticamente como invalidação completa da análise. O tamanho da amostra e o comportamento visual dos dados também devem ser considerados.

---

## Valores Discrepantes

Valores discrepantes, também chamados de outliers, são observações muito diferentes das demais.

Eles podem representar:

- erro de digitação;
- erro de medição;
- falha real do processo;
- causa especial;
- condição operacional diferente;
- produto ou lote de origem distinta.

Valores discrepantes não devem ser removidos automaticamente.

Antes da exclusão, deve existir uma justificativa técnica, registro da decisão e avaliação de seu impacto nos resultados.

---

## Tamanho da Amostra

A confiabilidade da análise depende da quantidade e da representatividade das medições.

Amostras muito pequenas podem produzir estimativas instáveis da média, do desvio-padrão e dos índices de capabilidade.

O agente deve informar quando houver poucos dados e evitar conclusões categóricas.

Não existe um único tamanho mínimo adequado para todos os casos. A quantidade necessária depende do processo, da estratégia de amostragem, da variabilidade e do objetivo da análise.

---

## Sistema de Medição

Antes de avaliar a capabilidade do processo, é importante verificar se o sistema de medição é adequado.

Um sistema de medição com elevada variação pode aumentar artificialmente a dispersão dos dados e reduzir os índices de capabilidade.

A avaliação do sistema de medição pode envolver:

- calibração;
- resolução do instrumento;
- repetibilidade;
- reprodutibilidade;
- estabilidade;
- tendência;
- linearidade;
- estudos de MSA;
- estudos de Gage R&R.

O agente não deve afirmar que o processo é incapaz sem considerar que parte da variação pode ter origem no sistema de medição.

---

## Especificação Bilateral

Uma especificação bilateral possui:

- Limite Inferior de Especificação;
- Limite Superior de Especificação.

Nesse caso, podem ser calculados Cp, Cpk, Cpu e Cpl.

---

## Especificação Unilateral

Uma especificação unilateral possui apenas um limite relevante.

Exemplos:

- apenas valor máximo permitido;
- apenas valor mínimo permitido.

Nesses casos, a interpretação deve utilizar o índice correspondente ao limite existente.

Não se deve inventar um segundo limite apenas para viabilizar o cálculo.

---

## Percentual Fora da Especificação

O percentual fora da especificação representa a proporção de medições observadas abaixo do LIE ou acima do LSE.

Esse indicador descreve o conjunto de dados analisado.

Ele não substitui os índices de capabilidade, pois Cp e Cpk utilizam a média e a variação estimada do processo para avaliar seu comportamento.

---

## Cuidados na Interpretação

Antes de concluir que um processo é capaz, devem ser avaliados:

- qualidade e integridade dos dados;
- quantidade de medições;
- estabilidade do processo;
- método de cálculo do desvio-padrão;
- normalidade ou distribuição dos dados;
- sistema de medição;
- representatividade da amostra;
- presença de valores discrepantes;
- alterações de máquina, lote, turno ou ferramenta;
- critérios definidos pelo cliente ou pela organização.

---

## Boas Práticas

- Não interpretar Cp ou Cpk isoladamente.
- Não confundir limites de especificação com limites de controle.
- Não remover dados sem justificativa.
- Não inventar limites de especificação.
- Registrar os tratamentos aplicados aos dados.
- Separar análises por máquina, turno, lote ou produto quando necessário.
- Verificar a estabilidade antes de interpretar a capabilidade.
- Comparar Cp com Cpk.
- Comparar Cpk com Ppk.
- Informar claramente as limitações da análise.
- Utilizar critérios de aceitação definidos pela organização.
- Tratar as conclusões como apoio à decisão técnica.

---

## Papel do Agente

O agente deve:

- interpretar resultados calculados pelo Python;
- explicar os indicadores de forma clara;
- identificar o lado mais crítico do processo;
- destacar possíveis sinais de descentramento;
- apontar limitações da análise;
- informar quando os dados não são suficientes;
- diferenciar resultados observados de hipóteses;
- utilizar apenas as informações disponíveis no contexto.

O agente não deve:

- inventar resultados;
- recalcular indicadores por conta própria;
- definir limites de especificação;
- remover valores automaticamente;
- identificar causa-raiz como se fosse um fato confirmado;
- afirmar estabilidade com base apenas no Cpk;
- substituir a avaliação de um profissional qualificado;
- aprovar ou reprovar produtos, lotes ou processos.
