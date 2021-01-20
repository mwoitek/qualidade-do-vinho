## Script do R para combinar os arquivos `winequality-red.csv` e
## `winequality-white.csv` num único arquivo csv um pouco mais organizado

## Importa as bibliotecas necessárias
library(dplyr)
library(magrittr)
library(readr)
library(tibble)

## Diretório dos arquivos de dados
diretorio <- "../dados"

## Nomes das colunas
nomes_colunas <- c(
  "fixed.acidity",
  "volatile.acidity",
  "citric.acid",
  "residual.sugar",
  "chlorides",
  "free.sulfur.dioxide",
  "total.sulfur.dioxide",
  "density",
  "ph",
  "sulphates",
  "alcohol",
  "quality"
)

## Cria um tibble usando os dados que estão em `winequality-red.csv`
tintos <-
  read_delim(
    file = paste(c(diretorio, "winequality-red.csv"), collapse = "/"),
    delim = ";",
    col_names = nomes_colunas,
    skip = 1
  ) %>%
  add_column(type = "red", .before = "fixed.acidity")

## Cria um tibble usando os dados que estão em `winequality-white.csv`
brancos <-
  read_delim(
    file = paste(c(diretorio, "winequality-white.csv"), collapse = "/"),
    delim = ";",
    col_names = nomes_colunas,
    skip = 1
  ) %>%
  add_column(type = "white", .before = "fixed.acidity")

# Combina `tintos` e `brancos` num único tibble
vinhos <- bind_rows(tintos, brancos)

# Cria um arquivo csv a partir do tibble acima
write_csv(
  vinhos,
  file = paste(c(diretorio, "vinhos.csv"), collapse = "/"),
  col_names = TRUE
)
