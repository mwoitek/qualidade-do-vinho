import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from .parametros import COL_QUAL
from .parametros import COL_TIPO


def separa_tipo(todos_dados, tipo):
    feats = todos_dados[todos_dados[COL_TIPO] == tipo].drop(columns=COL_TIPO).reset_index(drop=True)

    lbls = feats.pop(COL_QUAL)
    lbls.name = None

    return feats, lbls


def pega_valores_qualidade(qualidade):
    return np.sort(qualidade.unique())


def filtra_dados_1_qualidade(dados, qual_val):
    return dados[dados[COL_QUAL] == qual_val].drop(columns=COL_QUAL).to_numpy()


def separa_dados_por_qualidade(dados):
    dados_sep = {}

    for qual_val in pega_valores_qualidade(dados[COL_QUAL]):
        dados_sep[qual_val] = filtra_dados_1_qualidade(dados, qual_val)

    return dados_sep


def amostra_array_dados(array_dados, tam_amostra):
    num_obs = array_dados.shape[0]

    if num_obs <= tam_amostra:
        return array_dados
    return array_dados[np.random.choice(num_obs, size=tam_amostra, replace=False), :]


def amostra_dados_separados(dados_sep, tam_amostra):
    dados_sep_amostra = {}

    for qual_val, array_dados in dados_sep.items():
        dados_sep_amostra[qual_val] = amostra_array_dados(array_dados, tam_amostra)

    return dados_sep_amostra


def separa_amostra_dados(dados, tam_amostra):
    return amostra_dados_separados(separa_dados_por_qualidade(dados), tam_amostra)


def normaliza_dados(dados):
    scaler = StandardScaler().fit(dados)

    return pd.DataFrame(scaler.transform(dados), columns=dados.columns), scaler
