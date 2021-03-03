# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
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
import pandas as pd
from funcoes_cluster.funcoes_pca import separa_tipo
from funcoes_cluster.funcoes_pca import transforma_df_pd
from funcoes_cluster.funcoes_pca import transforma_df_sk

# %% [markdown]
# ## Parâmetros

# %%
N_HEAD = 10

# %% [markdown]
# ## Lendo o arquivo de dados

# %%
pasta_dados = Path('.').resolve().parents[1] / 'dados'
arquivo = pasta_dados / 'vinhos.csv'

vinhos_df = pd.read_csv(arquivo)
vinhos_df.head(n=N_HEAD)

# %% [markdown]
# ## Separando os dados

# %%
tintos_df, qual_tintos = separa_tipo(vinhos_df, 'red')
tintos_df.head(n=N_HEAD)

# %%
qual_tintos.head(n=N_HEAD)

# %%
brancos_df, qual_brancos = separa_tipo(vinhos_df, 'white')
brancos_df.head(n=N_HEAD)

# %%
qual_brancos.head(n=N_HEAD)

# %% [markdown]
# ## Pré-processando os dados

# %%
tintos_transf_pd = transforma_df_pd(tintos_df)
tintos_transf_pd.head(n=N_HEAD)

# %%
tintos_transf_sk = transforma_df_sk(tintos_df)
tintos_transf_sk.head(n=N_HEAD)

# %%
brancos_transf_pd = transforma_df_pd(brancos_df)
brancos_transf_pd.head(n=N_HEAD)

# %%
brancos_transf_sk = transforma_df_sk(brancos_df)
brancos_transf_sk.head(n=N_HEAD)

# %%
pd.testing.assert_frame_equal(tintos_transf_pd, tintos_transf_sk)
pd.testing.assert_frame_equal(brancos_transf_pd, brancos_transf_sk)
