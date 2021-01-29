## Fatos Básicos

Para começar, vamos considerar alguns fatos básicos sobre o conjunto de
dados que está no arquivo `vinhos.csv`.

### Números de Observações

Nesse conjunto, tem dados para vinhos tintos e brancos. Então algumas
informações básicas sobre esse data set são as seguintes:

-   Número de observações relacionadas com vinhos tintos;
-   Número de observações relacionadas com vinhos brancos;
-   Número total de observações.

Esses valores são dados na tabela abaixo.

<table>
<thead>
<tr class="header">
<th style="text-align: center;">Tipo</th>
<th style="text-align: center;">Observações</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;">Tinto</td>
<td style="text-align: center;">1599</td>
</tr>
<tr class="even">
<td style="text-align: center;">Branco</td>
<td style="text-align: center;">4898</td>
</tr>
<tr class="odd">
<td style="text-align: center;">Todos</td>
<td style="text-align: center;">6497</td>
</tr>
</tbody>
</table>

Perceba que o número total de observações apresentado no site da UCI é
menor. Naquela página, são contabilizadas apenas as observações
relacionadas com os vinhos brancos.

### Missing Values

Os pesquisadores que compilaram os dados afirmaram que este data set não
possui valores faltando. É uma boa ideia confirmar que essa afirmação é
verdadeira. A quantidade de missing values para cada coluna do conjunto
de dados pode ser vista na próxima tabela.

<table>
<thead>
<tr class="header">
<th style="text-align: center;">Coluna</th>
<th style="text-align: center;">Missing Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;">fixed.acidity</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="even">
<td style="text-align: center;">volatile.acidity</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="odd">
<td style="text-align: center;">citric.acid</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="even">
<td style="text-align: center;">residual.sugar</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="odd">
<td style="text-align: center;">chlorides</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="even">
<td style="text-align: center;">free.sulfur.dioxide</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="odd">
<td style="text-align: center;">total.sulfur.dioxide</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="even">
<td style="text-align: center;">density</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="odd">
<td style="text-align: center;">ph</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="even">
<td style="text-align: center;">sulphates</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="odd">
<td style="text-align: center;">alcohol</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="even">
<td style="text-align: center;">quality</td>
<td style="text-align: center;">0</td>
</tr>
</tbody>
</table>

### Distribuição dos Dados

Para cada vinho no conjunto de dados, há 11 medidas associadas com as
propriedades químicas da bebida. É importante analisar a distribuição de
cada uma dessas variáveis numéricas. Então começamos calculando as
seguintes quantidades para cada variável:

-   Valor mínimo;
-   Primeiro quartil;
-   Mediana;
-   Média;
-   Terceiro quartil;
-   Valor máximo.

Por uma questão de conveniência, os dados para os vinhos tintos foram
combinados com os dados para os vinhos brancos. Essas bebidas têm
características semelhantes, mas elas são diferentes e devem ser
consideradas separadamente. Então primeiro apresentamos os resultados
para os vinhos tintos e depois aqueles para os vinhos brancos. Os
resultados que obtivemos estão organizados nas tabelas que seguem.

Resultados para os vinhos tintos:

<table>
<thead>
<tr class="header">
<th style="text-align: center;">Variável</th>
<th style="text-align: center;">Mínimo</th>
<th style="text-align: center;">Primeiro quartil</th>
<th style="text-align: center;">Mediana</th>
<th style="text-align: center;">Média</th>
<th style="text-align: center;">Terceiro quartil</th>
<th style="text-align: center;">Máximo</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;">fixed.acidity</td>
<td style="text-align: center;">4.60000</td>
<td style="text-align: center;">7.1000</td>
<td style="text-align: center;">7.90000</td>
<td style="text-align: center;">8.3196373</td>
<td style="text-align: center;">9.200000</td>
<td style="text-align: center;">15.90000</td>
</tr>
<tr class="even">
<td style="text-align: center;">volatile.acidity</td>
<td style="text-align: center;">0.12000</td>
<td style="text-align: center;">0.3900</td>
<td style="text-align: center;">0.52000</td>
<td style="text-align: center;">0.5278205</td>
<td style="text-align: center;">0.640000</td>
<td style="text-align: center;">1.58000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">citric.acid</td>
<td style="text-align: center;">0.00000</td>
<td style="text-align: center;">0.0900</td>
<td style="text-align: center;">0.26000</td>
<td style="text-align: center;">0.2709756</td>
<td style="text-align: center;">0.420000</td>
<td style="text-align: center;">1.00000</td>
</tr>
<tr class="even">
<td style="text-align: center;">residual.sugar</td>
<td style="text-align: center;">0.90000</td>
<td style="text-align: center;">1.9000</td>
<td style="text-align: center;">2.20000</td>
<td style="text-align: center;">2.5388055</td>
<td style="text-align: center;">2.600000</td>
<td style="text-align: center;">15.50000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">chlorides</td>
<td style="text-align: center;">0.01200</td>
<td style="text-align: center;">0.0700</td>
<td style="text-align: center;">0.07900</td>
<td style="text-align: center;">0.0874665</td>
<td style="text-align: center;">0.090000</td>
<td style="text-align: center;">0.61100</td>
</tr>
<tr class="even">
<td style="text-align: center;">free.sulfur.dioxide</td>
<td style="text-align: center;">1.00000</td>
<td style="text-align: center;">7.0000</td>
<td style="text-align: center;">14.00000</td>
<td style="text-align: center;">15.8749218</td>
<td style="text-align: center;">21.000000</td>
<td style="text-align: center;">72.00000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">total.sulfur.dioxide</td>
<td style="text-align: center;">6.00000</td>
<td style="text-align: center;">22.0000</td>
<td style="text-align: center;">38.00000</td>
<td style="text-align: center;">46.4677924</td>
<td style="text-align: center;">62.000000</td>
<td style="text-align: center;">289.00000</td>
</tr>
<tr class="even">
<td style="text-align: center;">density</td>
<td style="text-align: center;">0.99007</td>
<td style="text-align: center;">0.9956</td>
<td style="text-align: center;">0.99675</td>
<td style="text-align: center;">0.9967467</td>
<td style="text-align: center;">0.997835</td>
<td style="text-align: center;">1.00369</td>
</tr>
<tr class="odd">
<td style="text-align: center;">ph</td>
<td style="text-align: center;">2.74000</td>
<td style="text-align: center;">3.2100</td>
<td style="text-align: center;">3.31000</td>
<td style="text-align: center;">3.3111132</td>
<td style="text-align: center;">3.400000</td>
<td style="text-align: center;">4.01000</td>
</tr>
<tr class="even">
<td style="text-align: center;">sulphates</td>
<td style="text-align: center;">0.33000</td>
<td style="text-align: center;">0.5500</td>
<td style="text-align: center;">0.62000</td>
<td style="text-align: center;">0.6581488</td>
<td style="text-align: center;">0.730000</td>
<td style="text-align: center;">2.00000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">alcohol</td>
<td style="text-align: center;">8.40000</td>
<td style="text-align: center;">9.5000</td>
<td style="text-align: center;">10.20000</td>
<td style="text-align: center;">10.4229831</td>
<td style="text-align: center;">11.100000</td>
<td style="text-align: center;">14.90000</td>
</tr>
</tbody>
</table>

Resultados para os vinhos brancos:

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: center;">Variável</th>
<th style="text-align: center;">Mínimo</th>
<th style="text-align: center;">Primeiro quartil</th>
<th style="text-align: center;">Mediana</th>
<th style="text-align: center;">Média</th>
<th style="text-align: center;">Terceiro quartil</th>
<th style="text-align: center;">Máximo</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;">fixed.acidity</td>
<td style="text-align: center;">3.80000</td>
<td style="text-align: center;">6.3000000</td>
<td style="text-align: center;">6.80000</td>
<td style="text-align: center;">6.8547877</td>
<td style="text-align: center;">7.3000</td>
<td style="text-align: center;">14.20000</td>
</tr>
<tr class="even">
<td style="text-align: center;">volatile.acidity</td>
<td style="text-align: center;">0.08000</td>
<td style="text-align: center;">0.2100000</td>
<td style="text-align: center;">0.26000</td>
<td style="text-align: center;">0.2782411</td>
<td style="text-align: center;">0.3200</td>
<td style="text-align: center;">1.10000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">citric.acid</td>
<td style="text-align: center;">0.00000</td>
<td style="text-align: center;">0.2700000</td>
<td style="text-align: center;">0.32000</td>
<td style="text-align: center;">0.3341915</td>
<td style="text-align: center;">0.3900</td>
<td style="text-align: center;">1.66000</td>
</tr>
<tr class="even">
<td style="text-align: center;">residual.sugar</td>
<td style="text-align: center;">0.60000</td>
<td style="text-align: center;">1.7000000</td>
<td style="text-align: center;">5.20000</td>
<td style="text-align: center;">6.3914149</td>
<td style="text-align: center;">9.9000</td>
<td style="text-align: center;">65.80000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">chlorides</td>
<td style="text-align: center;">0.00900</td>
<td style="text-align: center;">0.0360000</td>
<td style="text-align: center;">0.04300</td>
<td style="text-align: center;">0.0457724</td>
<td style="text-align: center;">0.0500</td>
<td style="text-align: center;">0.34600</td>
</tr>
<tr class="even">
<td style="text-align: center;">free.sulfur.dioxide</td>
<td style="text-align: center;">2.00000</td>
<td style="text-align: center;">23.0000000</td>
<td style="text-align: center;">34.00000</td>
<td style="text-align: center;">35.3080849</td>
<td style="text-align: center;">46.0000</td>
<td style="text-align: center;">289.00000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">total.sulfur.dioxide</td>
<td style="text-align: center;">9.00000</td>
<td style="text-align: center;">108.0000000</td>
<td style="text-align: center;">134.00000</td>
<td style="text-align: center;">138.3606574</td>
<td style="text-align: center;">167.0000</td>
<td style="text-align: center;">440.00000</td>
</tr>
<tr class="even">
<td style="text-align: center;">density</td>
<td style="text-align: center;">0.98711</td>
<td style="text-align: center;">0.9917225</td>
<td style="text-align: center;">0.99374</td>
<td style="text-align: center;">0.9940274</td>
<td style="text-align: center;">0.9961</td>
<td style="text-align: center;">1.03898</td>
</tr>
<tr class="odd">
<td style="text-align: center;">ph</td>
<td style="text-align: center;">2.72000</td>
<td style="text-align: center;">3.0900000</td>
<td style="text-align: center;">3.18000</td>
<td style="text-align: center;">3.1882666</td>
<td style="text-align: center;">3.2800</td>
<td style="text-align: center;">3.82000</td>
</tr>
<tr class="even">
<td style="text-align: center;">sulphates</td>
<td style="text-align: center;">0.22000</td>
<td style="text-align: center;">0.4100000</td>
<td style="text-align: center;">0.47000</td>
<td style="text-align: center;">0.4898469</td>
<td style="text-align: center;">0.5500</td>
<td style="text-align: center;">1.08000</td>
</tr>
<tr class="odd">
<td style="text-align: center;">alcohol</td>
<td style="text-align: center;">8.00000</td>
<td style="text-align: center;">9.5000000</td>
<td style="text-align: center;">10.40000</td>
<td style="text-align: center;">10.5142670</td>
<td style="text-align: center;">11.4000</td>
<td style="text-align: center;">14.20000</td>
</tr>
</tbody>
</table>

#### Boxplots

Não é tão simples ganhar um entendimento sobre a distribuição dos dados
apenas olhando para as tabelas acima. Sendo assim, na sequência
consideramos algumas maneiras de visualizar essa distribuição. Primeiro,
criamos uma série de boxplots. Esse passo é interessante, pois os
autores que compilaram este conjunto de dados afirmaram que nele há uma
grande quantidade de outliers. Queremos confirmar que essa afirmação é
verdadeira visualizando os diagramas de caixa.

Para cada característica do vinho, criamos um par de diagramas. Um deles
representa a distribuição dos dados para os vinhos tintos e o outro
corresponde aos vinhos brancos.

**Boxplot da variável na coluna `fixed.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_fixed_acidity-1.png)

**Boxplot da variável na coluna `volatile.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_volatile_acidity-1.png)

**Boxplot da variável na coluna `citric.acid`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_citric_acid-1.png)

**Boxplot da variável na coluna `residual.sugar`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_residual_sugar-1.png)

**Boxplot da variável na coluna `chlorides`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_chlorides-1.png)

**Boxplot da variável na coluna `free.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_free_sulfur_dioxide-1.png)

**Boxplot da variável na coluna `total.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_total_sulfur_dioxide-1.png)

**Boxplot da variável na coluna `density`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_density-1.png)

**Boxplot da variável na coluna `ph`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_ph-1.png)

**Boxplot da variável na coluna `sulphates`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_sulphates-1.png)

**Boxplot da variável na coluna `alcohol`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_alcohol-1.png)

#### Violin Plots

Na sequência, visualizamos a distribuição das variáveis contínuas de uma
maneira alternativa. Para cada uma delas, geramos um par de violin
plots. Como no caso anterior, uma figura está relacionada com os vinhos
tintos e a outra com os vinhos brancos.

**Violin plot da variável na coluna `fixed.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_fixed_acidity-1.png)

**Violin plot da variável na coluna `volatile.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_volatile_acidity-1.png)

**Violin plot da variável na coluna `citric.acid`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_citric_acid-1.png)

**Violin plot da variável na coluna `residual.sugar`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_residual_sugar-1.png)

**Violin plot da variável na coluna `chlorides`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_chlorides-1.png)

**Violin plot da variável na coluna `free.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_free_sulfur_dioxide-1.png)

**Violin plot da variável na coluna `total.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_total_sulfur_dioxide-1.png)

**Violin plot da variável na coluna `density`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_density-1.png)

**Violin plot da variável na coluna `ph`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_ph-1.png)

**Violin plot da variável na coluna `sulphates`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_sulphates-1.png)

**Violin plot da variável na coluna `alcohol`:**

![](analise_exploratoria_files/figure-markdown_strict/violin_alcohol-1.png)

#### Histogramas

Para continuar, consideramos outro modo de visualizar a distribuição das
variáveis contínuas. Especificamente, geramos os histogramas
correspondentes. Como antes, criamos um par de figuras para cada
variável. Uma delas representa a distribuição dos dados para os vinhos
tintos e a outra está associada com os vinhos brancos.

**Histograma da variável na coluna `fixed.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_fixed_acidity-1.png)

**Histograma da variável na coluna `volatile.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_volatile_acidity-1.png)

**Histograma da variável na coluna `citric.acid`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_citric_acid-1.png)

**Histograma da variável na coluna `residual.sugar`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_residual_sugar-1.png)

**Histograma da variável na coluna `chlorides`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_chlorides-1.png)

**Histograma da variável na coluna `free.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_free_sulfur_dioxide-1.png)

**Histograma da variável na coluna `total.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_total_sulfur_dioxide-1.png)

**Histograma da variável na coluna `density`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_density-1.png)

**Histograma da variável na coluna `ph`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_ph-1.png)

**Histograma da variável na coluna `sulphates`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_sulphates-1.png)

**Histograma da variável na coluna `alcohol`:**

![](analise_exploratoria_files/figure-markdown_strict/histograma_alcohol-1.png)

#### Qualidade

Até o momento, levamos em consideração apenas as variáveis contínuas no
conjunto de dados. Mas esse conjunto possui uma variável discreta
bastante importante, a qualidade de cada vinho. Essa é a variável que
mais tarde usaremos como rótulo (label) para treinar os nossos modelos
de Machine Learning. Sendo assim, na sequência discutimos o que podemos
aprender ao considerar a qualidade.

É natural começar fazendo o seguinte questionamento: como os vinhos no
conjunto de dados estão distribuídos de acordo com a qualidade? A
próxima figura mostra o percentual de vinhos tintos em cada uma das
categorias.

![](analise_exploratoria_files/figure-markdown_strict/distribuicao_qualidade_tintos-1.png)

No gráfico acima, incluímos apenas as categorias de qualidade que
realmente aparecem nesse subconjunto dos dados. Por exemplo, entre os
vinhos tintos, não há nenhum vinho que recebeu a nota 9. Por esse
motivo, essa categoria foi omitida.

O rótulo podia assumir qualquer valor inteiro desde 1 até 10. Mas a
última figura deixa claro o seguinte: para os vinhos tintos, somente os
valores entre 3 e 8 realmente ocorrem. Então nesse caso não temos 10
categorias de qualidade e, sim, 6.

Além disso, observe que a maioria dos vinhos tintos no conjunto de dados
foi considerada de qualidade média. De fato, nesse caso os melhores
vinhos e aqueles de péssima qualidade correspondem a uma pequena fração
das observações.

Em seguida, plotamos a figura análoga para os vinhos brancos:

![](analise_exploratoria_files/figure-markdown_strict/distribuicao_qualidade_brancos-1.png)

Perceba que mais uma vez o rótulo não assume todos os valores possíveis.
No caso dos vinhos brancos, essa variável varia no intervalo desde 3 até
9. Sendo assim, na prática temos apenas 7 categorias de qualidade.

Como no caso dos vinhos tintos, grande parte dos vinhos brancos foi
considerada de qualidade média. Entretanto, a qualidade dos vinhos
brancos no conjunto de dados tende a ser melhor. Proporcionalmente, tem
mais vinhos desse tipo nas categorias associadas com uma qualidade mais
alta. E a proporção de vinhos brancos na pior categoria observada é
ligeiramente menor.

**Distribuição das variáveis contínuas dentro de cada categoria**

Na sequência, analisamos a distribuição das variáveis contínuas dentro
de cada uma das categorias de qualidade observadas. Para entender o
nosso propósito, considere qualquer uma dessas variáveis. O objetivo é
responder às seguintes perguntas: entre os vinhos de péssima qualidade,
como é a distribuição dessa variável? E entre os melhores vinhos?

A resposta para essas questões pode ser visualizada através de uma série
de boxplots.

**Boxplot da variável na coluna `fixed.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_fixed_acidity-1.png)

**Boxplot da variável na coluna `volatile.acidity`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_volatile_acidity-1.png)

**Boxplot da variável na coluna `citric.acid`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_citric_acid-1.png)

**Boxplot da variável na coluna `residual.sugar`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_residual_sugar-1.png)

**Boxplot da variável na coluna `chlorides`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_chlorides-1.png)

**Boxplot da variável na coluna `free.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_free_sulfur_dioxide-1.png)

**Boxplot da variável na coluna `total.sulfur.dioxide`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_total_sulfur_dioxide-1.png)

**Boxplot da variável na coluna `density`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_density-1.png)

**Boxplot da variável na coluna `ph`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_ph-1.png)

**Boxplot da variável na coluna `sulphates`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_sulphates-1.png)

**Boxplot da variável na coluna `alcohol`:**

![](analise_exploratoria_files/figure-markdown_strict/boxplot_qualidade_alcohol-1.png)
