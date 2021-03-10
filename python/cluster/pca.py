# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Principal Component Analysis (PCA)
# ## Importações

# %%
from pathlib import Path
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
from funcoes_cluster.funcoes_comuns import normaliza_dados
from funcoes_cluster.funcoes_comuns import separa_tipo
from funcoes_cluster.funcoes_pca import imprime_variancia_explicada
from funcoes_cluster.funcoes_pca import plota_dados_projetados
from funcoes_cluster.funcoes_pca import projeta_dados

# %% [markdown]
# ## Parâmetros

# %%
N_HEAD = 10
TAM_AMOSTRA = 150

np.random.seed(0)
plt.rcParams['figure.figsize'] = [12, 10]

# %% [markdown]
# ## Lendo o arquivo de dados

# %%
pasta_dados = Path('.').resolve().parents[1] / 'dados'
arquivo = pasta_dados / 'vinhos.csv'

vinhos_df = pd.read_csv(arquivo)
vinhos_df.head(N_HEAD)

# %% [markdown]
# ## Separando os dados

# %%
tintos_df, qual_tintos = separa_tipo(vinhos_df, 'red')
tintos_df.head(N_HEAD)

# %%
qual_tintos.head(N_HEAD)

# %%
brancos_df, qual_brancos = separa_tipo(vinhos_df, 'white')
brancos_df.head(N_HEAD)

# %%
qual_brancos.head(N_HEAD)

# %% [markdown]
# ## Normalizando os dados

# %%
tintos_normal, _ = normaliza_dados(tintos_df)
tintos_normal.head(N_HEAD)

# %%
brancos_normal, _ = normaliza_dados(brancos_df)
brancos_normal.head(N_HEAD)

# %% [markdown]
# ## PCA: 2 Componentes Principais

# %%
tintos_proj_2d, pca_tintos = projeta_dados(2, tintos_normal, qual_tintos)
tintos_proj_2d.head(N_HEAD)

# %%
imprime_variancia_explicada(pca_tintos)

# %%
plota_dados_projetados(tintos_proj_2d, TAM_AMOSTRA)

# %%
brancos_proj_2d, pca_brancos = projeta_dados(2, brancos_normal, qual_brancos)
brancos_proj_2d.head(N_HEAD)

# %%
imprime_variancia_explicada(pca_brancos)

# %%
plota_dados_projetados(brancos_proj_2d, TAM_AMOSTRA)

# %% [markdown]
# ## PCA: 3 Componentes Principais

# %%
tintos_proj_3d, pca_tintos = projeta_dados(3, tintos_normal, qual_tintos)
tintos_proj_3d.head(N_HEAD)

# %%
imprime_variancia_explicada(pca_tintos)

# %%
plota_dados_projetados(tintos_proj_3d, TAM_AMOSTRA)

# %%
brancos_proj_3d, pca_brancos = projeta_dados(3, brancos_normal, qual_brancos)
brancos_proj_3d.head(N_HEAD)

# %%
imprime_variancia_explicada(pca_brancos)

# %%
plota_dados_projetados(brancos_proj_3d, TAM_AMOSTRA)

# %% [markdown]
# ## PCA: 7 Componentes Principais

# %%
tintos_proj_7d, pca_tintos = projeta_dados(7, tintos_normal, qual_tintos)
tintos_proj_7d.head(N_HEAD)

# %%
imprime_variancia_explicada(pca_tintos)

# %%
brancos_proj_7d, pca_brancos = projeta_dados(7, brancos_normal, qual_brancos)
brancos_proj_7d.head(N_HEAD)

# %%
imprime_variancia_explicada(pca_brancos)
