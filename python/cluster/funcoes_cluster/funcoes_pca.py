import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from .funcoes_comuns import separa_amostra_dados
from .parametros import COL_QUAL


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


def plota_dados_projetados(dados_proj, tam_amostra):
    dim = dados_proj.shape[1] - 1
    eh_3d = dim == 3

    fig = plt.figure()

    if eh_3d:
        ax = fig.add_subplot(111, projection='3d')
        coords = {'xs': None, 'ys': None, 'zs': None}
    else:
        ax = fig.add_subplot(111)
        coords = {'x': None, 'y': None}

    for qual_val, amostra_array in separa_amostra_dados(dados_proj, tam_amostra).items():
        for i, coord in enumerate(coords):
            coords[coord] = amostra_array[:, i]

        ax.scatter(**coords, label=str(qual_val))

    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')

    ax.set_xticks([])
    ax.set_yticks([])

    if eh_3d:
        ax.set_zlabel('x_3')
        ax.set_zticks([])

    ax.set_title(f'Dados Projetados em {dim}D')
    ax.legend()
