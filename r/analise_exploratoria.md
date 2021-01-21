Fatos Básicos
-------------

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
cada uma dessas variáveis numéricas. Então vamos começar calculando para
cada variável as seguintes quantidades:

-   Valor mínimo;
-   Primeiro quartil;
-   Mediana;
-   Média;
-   Terceiro quartil;
-   Valor máximo.

Os resultados que obtivemos estão organizados na tabela que segue.
