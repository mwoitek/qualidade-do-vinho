import numpy as np


def calcula_iqr(dados, retorna_quartis=False):
    q_1 = dados.quantile(0.25)
    q_3 = dados.quantile(0.75)
    iqr = q_3 - q_1

    if retorna_quartis:
        return iqr, q_1, q_3
    return iqr


def calcula_limite_inferior(q_1, iqr, k):
    return q_1 - k * iqr


def calcula_limite_superior(q_3, iqr, k):
    return q_3 + k * iqr


def calcula_limites_inner(iqr, q_1, q_3):
    return calcula_limite_inferior(q_1, iqr, 1.5), calcula_limite_superior(q_3, iqr, 1.5)


def calcula_limites_outer(iqr, q_1, q_3):
    return calcula_limite_inferior(q_1, iqr, 3), calcula_limite_superior(q_3, iqr, 3)


def cria_dict_limites(col, tipo_outlier):
    iqr, q_1, q_3 = calcula_iqr(col, retorna_quartis=True)
    limites = {}

    limites['inf_out'], limites['sup_out'] = calcula_limites_outer(iqr, q_1, q_3)
    if tipo_outlier == 'mild':
        limites['inf_in'], limites['sup_in'] = calcula_limites_inner(iqr, q_1, q_3)

    return limites


def eh_mild(val, inf_in, sup_in, inf_out, sup_out):
    return (inf_out <= val < inf_in) or (sup_in < val <= sup_out)


def eh_strong(val, inf_out, sup_out):
    return (val < inf_out) or (val > sup_out)


def acha_outliers_1_coluna(df, coluna, tipo_outlier, lista=False):
    col = df.loc[:, coluna] if isinstance(coluna, str) else df.iloc[:, coluna]
    func_teste = eh_mild if tipo_outlier == 'mild' else eh_strong
    limites = cria_dict_limites(col, tipo_outlier)
    idx_outliers = (idx for idx, val in enumerate(col) if func_teste(val, **limites))

    if lista:
        return sorted(list(idx_outliers))
    return idx_outliers


def acha_outliers_df_dict(df, tipo_outlier):
    return {col: acha_outliers_1_coluna(df, col, tipo_outlier, True) for col in df.columns.array}


def acha_outliers_df_lista(df, tipo_outlier):
    idx_outliers = set()

    for coluna in df.columns.array:
        idx_outliers.update(acha_outliers_1_coluna(df, coluna, tipo_outlier))

    return sorted(list(idx_outliers))


def acha_outliers_df(df, tipo_outlier, lista=True):
    func_acha = acha_outliers_df_lista if lista else acha_outliers_df_dict

    return func_acha(df, tipo_outlier)


def remove_idx(dados, idx):
    return dados.drop(index=idx).reset_index(drop=True)


def remove_outliers(feats, lbls, tipo_outlier, verbose=False):
    idx_outliers = acha_outliers_df(feats, tipo_outlier)

    if verbose:
        print(f'Número de {tipo_outlier} outliers removidos: {len(idx_outliers)}')

    return remove_idx(feats, idx_outliers), remove_idx(lbls, idx_outliers)


def log_coluna(df, coluna):
    col = df.loc[:, coluna] if isinstance(coluna, str) else df.iloc[:, coluna]
    log_col = col.apply(np.log)
    ok = not log_col.replace([-np.inf, np.inf], np.nan).hasnans

    if ok:
        return log_col, ok
    return col, ok


def log_df(df, verbose=False):
    novo_df = df.copy()

    if verbose:
        cols_prob = []

    for coluna in novo_df.columns.array:
        novo_df.loc[:, coluna], ok = log_coluna(novo_df, coluna)

        if verbose and not ok:
            cols_prob.append(coluna)

    if verbose and len(cols_prob) > 0:
        print('As seguintes colunas não foram alteradas:')
        for col in cols_prob:
            print(col)

    return novo_df
