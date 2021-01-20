#!/bin/bash
# Script para baixar o conjunto de dados
diretorio="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality"
wget -o log1 "${diretorio}/winequality-red.csv"
wget -o log2 "${diretorio}/winequality-white.csv"
wget -o log3 "${diretorio}/winequality.names"
{ cat log1; cat log2; cat log3; } > download.log
rm -f log1 log2 log3
