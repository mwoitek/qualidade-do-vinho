import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


COL_QUAL = 'quality'
COL_TIPO = 'type'

np.random.seed(0)


def separa_tipo(todos_dados, tipo):
    feats = todos_dados[todos_dados[COL_TIPO] == tipo].drop(columns=COL_TIPO).reset_index(drop=True)

    lbls = feats.pop(COL_QUAL)
    lbls.name = None

    return feats, lbls


def normaliza_dados(dados):
    scaler = StandardScaler().fit(dados)
    dados_normal = scaler.transform(dados)

    return pd.DataFrame(dados_normal, columns=dados.columns), scaler


def cria_objeto_pca(n_components, dados):
    return PCA(n_components=n_components, random_state=0).fit(dados)


def projeta_dados(n_components, feats, lbls):
    pca = cria_objeto_pca(n_components, feats)

    dados_proj = pd.DataFrame(
        pca.transform(feats),
        columns=['x_' + str(i + 1) for i in range(pca.n_components_)]
    )
    dados_proj[COL_QUAL] = lbls

    return dados_proj, pca


def imprime_variancia_explicada(pca):
    print('Percentual da variância explicada pelas componentes principais\n')

    total = 0
    for i, razao in enumerate(pca.explained_variance_ratio_):
        print(f'Componente {i + 1}: {100 * razao:.2f}%')
        total += razao

    print(f'\nTotal:        {100 * total:.2f}%')


def pega_valores_qualidade(qualidade):
    return np.sort(qualidade.unique())


def filtra_dados_projetados(dados_proj, qual_val):
    return dados_proj[dados_proj[COL_QUAL] == qual_val].drop(columns=COL_QUAL).to_numpy()


def separa_dados_projetados(dados_proj):
    dados_separados = {}

    for qual_val in pega_valores_qualidade(dados_proj[COL_QUAL]):
        dados_separados[qual_val] = filtra_dados_projetados(dados_proj, qual_val)

    return dados_separados


def amostra_array_dados_projetados(array_dados_proj, tam_amostra):
    num_obs = array_dados_proj.shape[0]

    if num_obs <= tam_amostra:
        return array_dados_proj
    return array_dados_proj[np.random.choice(num_obs, size=tam_amostra, replace=False), :]


def amostra_dados_separados(dados_sep, tam_amostra):
    dados_sep_amostra = {}

    for qual_val, array_dados_proj in dados_sep.items():
        dados_sep_amostra[qual_val] = amostra_array_dados_projetados(array_dados_proj, tam_amostra)

    return dados_sep_amostra


def separa_amostra_dados_projetados(dados_proj, tam_amostra):
    return amostra_dados_separados(separa_dados_projetados(dados_proj), tam_amostra)


def plota_2d(dados_proj, tam_amostra):
    _, ax = plt.subplots()

    for qual_val, amostra_array in separa_amostra_dados_projetados(dados_proj, tam_amostra).items():
        ax.scatter(amostra_array[:, 0], amostra_array[:, 1], label=str(qual_val))

    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title('Dados Projetados em 2D')
    ax.legend()
