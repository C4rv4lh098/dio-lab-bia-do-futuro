# Fórmulas Estatísticas

## Objetivo deste arquivo

Este documento reúne as principais fórmulas utilizadas na análise estatística de capabilidade de processos.

As fórmulas aqui descritas servem como referência para interpretação dos resultados. Os cálculos devem ser realizados exclusivamente pelas rotinas implementadas em Python.

---

# Média

A média representa o valor central das medições.

Fórmula:

μ = Σx / n

Onde:

- μ = média das medições
- Σx = soma de todas as medições
- n = quantidade de medições

---

# Variância

A variância mede a dispersão dos dados em relação à média.

Fórmula:

σ² = Σ(x - μ)² / (n - 1)

Onde:

- σ² = variância
- μ = média
- n = quantidade de medições

---

# Desvio-Padrão

O desvio-padrão representa a dispersão das medições.

Fórmula:

σ = √σ²

Onde:

- σ = desvio-padrão
- σ² = variância

Quanto menor o desvio-padrão, menor a variabilidade do processo.

---

# Índice Cp

O índice Cp mede a capacidade potencial do processo.

Fórmula:

Cp = (LSE - LIE) / (6σ)

Onde:

- LSE = Limite Superior de Especificação
- LIE = Limite Inferior de Especificação
- σ = desvio-padrão

O Cp considera apenas a dispersão dos dados.

---

# Índice Cpu

Avalia a capacidade considerando apenas o limite superior.

Fórmula:

Cpu = (LSE - Média) / (3σ)

Onde:

- LSE = Limite Superior de Especificação
- Média = média das medições
- σ = desvio-padrão

---

# Índice Cpl

Avalia a capacidade considerando apenas o limite inferior.

Fórmula:

Cpl = (Média - LIE) / (3σ)

Onde:

- Média = média das medições
- LIE = Limite Inferior de Especificação
- σ = desvio-padrão

---

# Índice Cpk

O índice Cpk corresponde ao menor valor entre Cpu e Cpl.

Fórmula:

Cpk = min(Cpu, Cpl)

ou

Cpk = min((LSE - Média)/(3σ), (Média - LIE)/(3σ))

O Cpk considera tanto a dispersão quanto o posicionamento da média.

---

# Índice Pp

O índice Pp utiliza a variabilidade total observada.

Fórmula:

Pp = (LSE - LIE) / (6s)

Onde:

- s = desvio-padrão global

---

# Índice Ppk

O índice Ppk considera a posição da média utilizando a variabilidade total.

Fórmula:

Ppk = min((LSE - Média)/(3s), (Média - LIE)/(3s))

Onde:

- s = desvio-padrão global

---

# Amplitude

A amplitude representa a diferença entre o maior e o menor valor observado.

Fórmula:

Amplitude = Máximo - Mínimo

---

# Coeficiente de Variação

O coeficiente de variação permite comparar a dispersão relativa entre diferentes conjuntos de dados.

Fórmula:

CV = (σ / Média) × 100

Resultado expresso em porcentagem.

---

# Percentual Fora da Especificação

Representa a porcentagem de medições abaixo do LIE ou acima do LSE.

Fórmula:

Percentual =

(Número de medições fora da especificação / Total de medições) × 100

---

# Interpretação Geral dos Índices

## Cp

| Valor | Interpretação |
|--------|---------------|
| Cp < 1,00 | Processo potencialmente incapaz |
| 1,00 ≤ Cp < 1,33 | Capacidade limitada |
| Cp ≥ 1,33 | Processo potencialmente capaz |

---

## Cpk

| Valor | Interpretação |
|--------|---------------|
| Cpk < 1,00 | Processo potencialmente incapaz |
| 1,00 ≤ Cpk < 1,33 | Capacidade limitada |
| 1,33 ≤ Cpk < 1,67 | Processo capaz |
| Cpk ≥ 1,67 | Excelente capacidade |

---

# Observações Importantes

- Todas as fórmulas devem ser executadas pelas funções Python da aplicação.
- O modelo de linguagem não deve recalcular indicadores.
- Os resultados devem ser utilizados apenas para interpretação.
- Os índices devem ser avaliados juntamente com a estabilidade do processo, qualidade dos dados e critérios da organização.
- Os critérios apresentados neste documento representam referências gerais e podem variar conforme normas internas ou requisitos do cliente.
