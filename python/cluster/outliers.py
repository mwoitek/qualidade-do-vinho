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
# # Detectando e removendo os outliers
# ## Importações

# %%
from pathlib import Path
import pandas as pd
from funcoes_cluster.funcoes_comuns import separa_tipo
from funcoes_cluster.funcoes_outliers import remove_outliers

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
# ## Removendo os outliers
# ### Mild outliers

# %%
t_mild, ql_t_mild = remove_outliers(tintos_df, qual_tintos, 'mild', verbose=True)
t_mild.head(N_HEAD)

# %%
ql_t_mild.head(N_HEAD)

# %%
b_mild, ql_b_mild = remove_outliers(brancos_df, qual_brancos, 'mild', verbose=True)
b_mild.head(N_HEAD)

# %%
ql_b_mild.head(N_HEAD)

# %% [markdown]
# ### Strong outliers

# %%
t_strong, ql_t_strong = remove_outliers(tintos_df, qual_tintos, 'strong', verbose=True)
t_strong.head(N_HEAD)

# %%
ql_t_strong.head(N_HEAD)

# %%
b_strong, ql_b_strong = remove_outliers(brancos_df, qual_brancos, 'strong', verbose=True)
b_strong.head(N_HEAD)

# %%
ql_b_strong.head(N_HEAD)
