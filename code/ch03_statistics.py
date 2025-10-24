import marimo

__generated_with = "0.17.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 統計の基礎""")
    return


@app.cell
def _():
    import marimo as mo
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
    return df, mo


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
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
