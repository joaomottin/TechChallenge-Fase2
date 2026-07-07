# Tech Challenge - Fase 2

## Classificação da qualidade de vinhos

Trabalho acadêmico da FIAP com análise da base **WineQT.csv** e criação de modelos simples de Machine Learning para classificar vinhos como alta qualidade ou baixa/média qualidade.

## Objetivo

Prever se um vinho pode ser considerado de alta qualidade usando suas características físico-químicas.

A coluna `quality` foi transformada em uma variável binária:

- `1`: vinho de alta qualidade, com `quality >= 7`
- `0`: vinho de baixa ou média qualidade, com `quality < 7`

A coluna `Id` não foi usada no treinamento, pois é apenas um identificador.

## Base de dados

Arquivo utilizado:

```text
data/WineQT.csv
```

A base original possui **1.143 registros**. Durante a análise, foram removidas **125 duplicatas completas**, considerando todas as colunas exceto `Id`. Após essa limpeza, a base ficou com **1.018 registros**:

- **137 vinhos de alta qualidade**;
- **881 vinhos de baixa/média qualidade**.

Isso mostra que a base é desbalanceada, pois existem muito menos vinhos de alta qualidade.

## O que foi feito

O notebook principal está em:

```text
notebooks/analise_wine_quality.ipynb
```

Ele contém:

- leitura da base e remoção de duplicatas;
- criação da variável `quality_binary`;
- análise exploratória dos dados;
- gráficos de distribuição das notas e das classes;
- matriz de correlação;
- separação dos dados em 75% treino e 25% teste;
- treinamento de Logistic Regression e Random Forest;
- comparação dos modelos antes e depois do balanceamento;
- avaliação com acurácia, precisão, recall, F1-score e ROC-AUC;
- matrizes de confusão;
- análise dos fatores mais importantes para o vinho ser classificado como alta qualidade.

## Modelos utilizados

Foram usados dois modelos principais:

- **Logistic Regression:** modelo mais simples e interpretável, usado como comparação inicial.
- **Random Forest:** modelo baseado em árvores de decisão, útil para capturar relações mais complexas e analisar importância das variáveis.

Como a base é desbalanceada, os modelos também foram testados com `class_weight='balanced'`.

## Principais conclusões

A acurácia sozinha não é suficiente para avaliar o problema, porque a maioria dos vinhos está na classe baixa/média. Por isso, também foram avaliados precisão, recall, F1-score e ROC-AUC.

O melhor modelo deve ser escolhido olhando a tabela final de métricas no notebook. Dependendo da divisão dos dados e do balanceamento, a Regressão Logística pode ter resultado competitivo em relação ao Random Forest.

Na análise de importância das variáveis, os fatores mais relevantes aparecem ligados principalmente a características como:

- teor alcoólico;
- acidez volátil;
- sulfatos;
- densidade;
- acidez.

Esses fatores ajudam a entender quais características físico-químicas mais influenciam a classificação de um vinho como alta qualidade.

## Estrutura do projeto

```text
data/          Base de dados
notebooks/     Notebook principal da análise
results/       Gráficos e métricas gerados pelo notebook
presentation/  Material de apresentação e roteiro
```

## Como rodar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois abra e execute o notebook:

```bash
jupyter notebook notebooks/analise_wine_quality.ipynb
```

## Integrantes

| Nome | RM | E-mail |
|---|---|---|
| Felipe Macedo da Silva | RM373436 | felipemsdocs@gmail.com |
| João Pedro Mezzadri Mottin | RM372545 | joaopedromm.construtiva@outlook.com |
| Miguel Fernandes Martins de Bastos | RM373815 | miguelbastospro@gmail.com |
| Thanael Butewicz | RM373935 | zthanaelbutewicz@hotmail.com |
| Veronica de Fatima Machado Silva | RM371976 | v.machado10@hotmail.com |
