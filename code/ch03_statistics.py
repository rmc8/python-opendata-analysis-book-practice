import marimo

__generated_with = "0.17.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 統計の基礎""")
    return


@app.cell
def _():
    import pandas as pd
    df = pd.DataFrame([
        ["いちごストア株式会社", "A4491", "上場", "小売業", 50, 250],
        ["メガハード株式会社", "A3547", "上場", "製造業", 50, 300],
        ["百聞半導体株式会社", "A2704", "上場", "製造業", 20, 180],
        ["五十音サーチ株式会社", "A8008", "上場", "小売業", 30, 200],
        ["利根川通販株式会社", "A4342", "上場", "小売業", 100, 240],
        ["超手本株式会社", "A3674", "上場", "サービス業", 20, 150],
        ["源内自動車株式会社", "A7514", None, "製造業", 10, 100],
        ["クローズサピエンス合同会社", "A0941", None, "サービス業", None, 120],
        ["富価自動車株式会社", "J7203", "上場", "製造業", 60, 120],
        ["ハード通信株式会社", "J9984", "上場", "サービス業", 15, 50],
        ["株式会社財前", "J3994", None, "サービス業", None, 30]
        ], columns=["会社名", "会社コード", "上場区分", "業種", "従業員数", "資本金"]
    )

    df
    return df, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 変数の種類

    ### 量的変数と質的変数

    ### ディメンジョンとメジャー

    ## 度数分布とヒストグラム
    """
    )
    return


@app.cell
def _(df):
    s = df["資本金"]
    freq_dist = (
        s.value_counts(bins=range(0, 501, 100), sort=False)
        .reset_index()
        .rename(columns={"index": "資本金階級", "資本金": "度数"})
    )
    freq_dist
    return (s,)


@app.cell
def _(s):
    s.hist(bins=range(0, 501, 100))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 要約統計量""")
    return


@app.cell
def _(df):
    df["従業員数"].size
    return


@app.cell
def _(df):
    df["従業員数"].count()
    return


@app.cell
def _(df):
    df["従業員数"].nunique()
    return


@app.cell
def _(df):
    df["資本金"].sum()
    return


@app.cell
def _(df):
    df["資本金"].mean()
    return


@app.cell
def _(df):
    df["資本金"].max(), df["資本金"].min()
    return


@app.cell
def _(df):
    df["資本金"].median()
    return


@app.cell
def _(df):
    df["資本金"].mode()
    return


@app.cell
def _(df):
    df["資本金"].var()
    return


@app.cell
def _(df):
    df["資本金"].std()
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 量的変数と質的変数の変換

    ### 離散化
    """
    )
    return


@app.cell
def _(df, pd):
    adf = df.assign(
        **{
            "資本金区分": pd.cut(df["資本金"], bins=3, right=False),
            "資本金区分等頻度離散化": pd.qcut(df["資本金"], q=3),
        },
    )
    adf[["資本金", "資本金区分", "資本金区分等頻度離散化"]]
    return (adf,)


@app.cell
def _(df, pd):
    pd.get_dummies(df["業種"], dtype=int).head(5)
    return


@app.cell
def _(adf, df):
    adf.assign(**{"小売業フラグ": (df["業種"]=="小売業").astype(int)}).iloc[:5, [-1]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### ダミー変数""")
    return


@app.cell
def _(adf):
    cols = ["資本金区分", "上場区分"]
    adf[cols].groupby(cols, dropna=False, observed=False).size().reset_index(name="度数")
    return (cols,)


@app.cell
def _(adf, cols):
    adf[cols + ["従業員数"]].groupby(cols, dropna=False, observed=False).mean().reset_index()
    return


@app.cell
def _(adf, cols):
    adf[cols + ["従業員数"]].groupby(cols, dropna=False, observed=False).count().reset_index()
    return


@app.cell
def _(adf, pd):
    table = adf.fillna(value={"上場区分": "非上場"})
    pd.pivot_table(
        table,
        values="従業員数",
        index="資本金区分",
        columns="上場区分",
        aggfunc="mean",
        observed=False,
    )
    return (table,)


@app.cell
def _(pd, table):
    pd.crosstab(
        index=table["資本金区分"],
        columns=table["上場区分"],
        values=table["従業員数"],
        aggfunc="mean",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## ２変量の統計""")
    return


@app.cell
def _(df):
    df_eng = df[["資本金", "従業員数"]].rename(columns={"資本金": "capital", "従業員数": "num of employees"})
    df_eng.plot.scatter(x="capital", y="num of employees")
    return (df_eng,)


@app.cell
def _(adf, df, pd):
    import seaborn as sns

    hdf = adf.assign(**{"従業員区分": pd.cut(df["従業員数"], bins=3, right=False)})
    heat_df = (
        hdf[["資本金区分", "従業員区分"]]
              .rename(columns={"資本金区分": "capital", "従業員区分": "num of employees"})
             )
    heat_crosstab = heat_df.pivot_table(
        index="capital",
        columns="num of employees",
        aggfunc="size",
        observed=False,
    )
    sns.heatmap(heat_crosstab, square=True, annot=True)
    return hdf, sns


@app.cell
def _(hdf):
    hdf[["資本金", "従業員数"]].cov()
    return


@app.cell
def _(hdf):
    hdf[["資本金", "従業員数"]].corr()
    return


@app.cell
def _(df_eng, sns):
    sns.heatmap(df_eng.corr(), square=True, annot=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 統計の分類と経済統計

    ### 調査統計・業務統計・加工統計および基幹統計

    ### 全数調査と標本調査

    ### 実質値と名目値

    ### 季節調整
    """
    )
    return


if __name__ == "__main__":
    app.run()
