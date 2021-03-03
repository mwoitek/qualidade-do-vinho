from typing import Tuple
import pandas as pd
from sklearn.preprocessing import StandardScaler


COL_QUAL = 'quality'
COL_TIPO = 'type'


def separa_tipo(
    todos_df: pd.core.frame.DataFrame,
    tipo: str
) -> Tuple[pd.core.frame.DataFrame, pd.core.series.Series]:
    feats = (
        todos_df[todos_df[COL_TIPO] == tipo]
        .drop(columns=COL_TIPO)
        .reset_index(drop=True)
    )
    lbls = feats.pop(COL_QUAL)

    return (feats, lbls)


def transforma_df_pd(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    medias = df.mean(axis=0)
    dps = df.std(axis=0, ddof=0)

    return df.sub(medias, axis=1).div(dps, axis=1)


def transforma_df_sk(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    scaler = StandardScaler().fit(df)
    dados_transf = scaler.transform(df)

    return pd.DataFrame(dados_transf, columns=df.columns)
