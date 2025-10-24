import marimo

__generated_with = "0.17.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # データ操作とpandas

    ## pandasとテーブルデータ

    [pandas](https://pandas.pydata.org/)
    """
    )
    return


@app.cell
def _():
    import pandas as pd

    df = pd.DataFrame(
        [
            ["C001", "製造業", 30],
            ["C002", "サービス業", 100],
            ["C003", "サービス業", None],
            ["C004", "小売業", 50],
            ["C005", "製造業", 20],
        ],
        columns=["会社コード", "業種", "従業員数"],
    )
    return df, pd


@app.cell
def _(mo):
    mo.md(r"""## データ型""")
    return


@app.cell
def _(df):
    type(df)
    return


@app.cell
def _(df):
    df["会社コード"]
    return


@app.cell
def _(df):
    df.会社コード
    return


@app.cell
def _():
    from datetime import date

    type(date(2020, 7, 1))
    return (date,)


@app.cell
def _(date, pd):
    ts = pd.to_datetime(date(2020, 7, 1))
    type(ts)
    return


@app.cell
def _(mo):
    mo.md(r"""## データの確認""")
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell
def _(df):
    df.index
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.head(2)
    return


@app.cell
def _(df):
    df.tail(1)
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(mo):
    mo.md(
        r"""Jupyter Notebookでpandasデータフレームを表示する際、浮動小数点の桁数をset_optionで設定できます。"""
    )
    return


@app.cell
def _(pd):
    pd.set_option("display.precision", 2)  # 小数第二桁まで表示
    return


@app.cell
def _(mo):
    mo.md(r"""## データ抽出・置換・代入""")
    return


@app.cell
def _(df):
    df[["会社コード", "業種"]]
    return


@app.cell
def _(df):
    df.loc[:, ["会社コード", "業種"]]
    return


@app.cell
def _(df):
    df.loc[:, "会社コード":"業種"]
    return


@app.cell
def _(df):
    df.iloc[:, [0, 1]]
    return


@app.cell
def _(df):
    df.iloc[:, 0:2]
    return


@app.cell
def _(df):
    df.iloc[:, :-1]
    return


@app.cell
def _(df):
    df.drop("従業員数", axis=1)
    return


@app.cell
def _(df):
    df.filter(regex="会社|業種")
    return


@app.cell
def _(df):
    df.iloc[:2, :]
    return


@app.cell
def _(df):
    df.iloc[:2, :2]
    return


@app.cell
def _(df):
    df[(df["業種"] != "製造業") & (df["従業員数"] >= 30)]
    return


@app.cell
def _(df):
    df.loc[(df["業種"] != "製造業") & (df["従業員数"] >= 30)]
    return


@app.cell
def _(df):
    df.query("業種 != '製造業' and 従業員数 >= 30")
    return


@app.cell
def _(df):
    df.query("業種 != '製造業' and 従業員数 >= 30")[["会社コード", "業種"]]
    return


@app.cell
def _(df):
    df.loc[(df["業種"] != "製造業") & (df["従業員数"] >= 30), ["会社コード", "業種"]]
    return


@app.cell
def _(df):
    df.assign(フラグ=0)
    return


@app.cell
def _(df):
    df.assign(**{"フラグ": 0})
    return


@app.cell
def _(df):
    df_original = df.copy()
    df["フラグ"] = 0
    df
    return (df_original,)


@app.cell
def _(df_original):
    print("元の df_original の id:", id(df_original))
    print("元の df_original:\n", df_original)

    # (1) ブラケット記法でインプレイス更新する方法
    df_inplace = df_original.copy()
    print("\n(1)インプレイス更新前の df_inplace の id:", id(df_inplace))
    df_inplace["フラグ"] = 0
    print("(1)インプレイス更新後の df_inplace の id:", id(df_inplace))
    print("(1)インプレイス更新後の df_inplace:\n", df_inplace)

    # (2) assign で新しいオブジェクトを作成する方法
    df_assign_before = df_original.copy()
    print("\n(2)assign 前の df_assign_before の id:", id(df_assign_before))
    df_assign_after = df_assign_before.assign(**{"フラグ": 0})
    print("(2)assign の結果 df_assign_after の id:", id(df_assign_after))
    print("(2)assign 後の df_assign_before (変更なし):\n", df_assign_before)
    print("(2)assign の結果 df_assign_after:\n", df_assign_after)
    return


@app.cell
def _(df_original):
    # (3) 【補足】assign で同じ変数に再代入する場合
    df_assign = df_original.copy()
    print("\n(3)再代入前の df_assign の id:", id(df_assign))
    df_assign = df_assign.assign(**{"フラグ": 0})
    print("(3)再代入後の df_assign の id:", id(df_assign))
    print("(3)再代入後の df_assign:\n", df_assign)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    - [inplaceについて](https://pandas.pydata.org/pdeps/0008-inplace-methods-in-pandas.html)
    - [チェーン代入について](https://pandas.pydata.org/docs/whatsnew/v2.2.0.html#chained-assignment)
    """
    )
    return


@app.cell
def _(df):
    df["フラグ"].mask(df["従業員数"] >= 30, 1)
    return


@app.cell
def _(df):
    df["フラグ"].where(df["従業員数"] > 30, -1)
    return


@app.cell
def _(df):
    df.replace("サービス業", "情報通信業")
    return


@app.cell
def _(df):
    df.rename(columns={"フラグ": "従業員30人以上フラグ"})
    return


@app.cell
def _(df):
    df.set_axis(["会社コード", "業種", "従業員数", "従業員30人以上フラグ"], axis=1)
    return


@app.cell
def _(mo):
    mo.md(r"""## 欠損値とNull""")
    return


@app.cell
def _(df):
    df.isna()
    return


@app.cell
def _(df):
    df[df["従業員数"].notna()]
    return


@app.cell
def _(df):
    df.dropna(axis=0, how="any")
    return


@app.cell
def _():
    df = df.assign(**{"従業員数": df["従業員数"].fillna(100)})
    df
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""## 重複とユニーク""")
    return


@app.cell
def _(df):
    df["業種"].unique()
    return


@app.cell
def _(df):
    df[["業種", "従業員数"]].duplicated(keep=False)
    return


@app.cell
def _(df):
    df.drop_duplicates(subset=["業種", "従業員数"])
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 分析しやすいデータ

    ### ワイドテーブルとロングテーブル

    ### 整然データ

    [Tidy Data](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://vita.had.co.nz/papers/tidy-data.pdf)

    ### 機械判読可能なデータ

    - [統計表における機械判読可能なデータの表記方法の統一ルールの策定](https://www.soumu.go.jp/menu_news/s-news/01toukatsu01_02000186.html)
    - [統計表における機械判読可能なデータ作成に関する表記方法](https://www.soumu.go.jp/main_content/000723626.pdf)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## データ成形""")
    return


@app.cell
def _(pd):
    import numpy as np

    df11 = pd.DataFrame(
        [
            ["a", "x", 2],
            ["a", "y", 0],
            ["b", "x", np.nan],
            ["b", "y", -5],
        ],
        columns=["A", "X", "V"],
    )
    df11
    return (df11,)


@app.cell
def _(df11):
    df13 = df11.set_index(["A", "X"])
    df13
    return (df13,)


@app.cell
def _(df13):
    df13.reset_index()
    return


@app.cell
def _(df11):
    df12 = df11.set_index("A")
    df12
    return (df12,)


@app.cell
def _(df12):
    df12.reset_index()
    return


@app.cell
def _(df12):
    df12.set_index("X", append=True)
    return


@app.cell
def _(df13):
    df13.reset_index(level=1)
    return


@app.cell
def _(df13):
    df23 = df13.unstack()
    df23
    return (df23,)


@app.cell
def _(df23):
    df23.stack(future_stack=True)
    return


@app.cell
def _(df23):
    df22 = df23.set_axis(df23.columns.levels[1], axis=1)
    df22
    return (df22,)


@app.cell
def _(df22):
    df31 = df22.transpose()
    df31
    return


@app.cell
def _(df22):
    df22.T
    return


@app.cell
def _(df22):
    df21 = df22.reset_index()
    df21
    return (df21,)


@app.cell
def _(df11):
    df11.pivot(columns="X", index="A", values="V")
    return


@app.cell
def _(df22, pd):
    pd.melt(df22, value_name="V", ignore_index=False)
    return


@app.cell
def _(df21, pd):
    pd.melt(df21, id_vars="A", value_vars=["x", "y"], value_name="V")
    return


@app.cell
def _(df11):
    df11.sort_values("V", ascending=False, na_position="last")
    return


@app.cell
def _(df11):
    df11.sort_index(ascending=False)
    return


@app.cell
def _(df11):
    df11.nlargest(2, columns="V")
    return


@app.cell
def _(df11):
    df11.nsmallest(2, columns="V")
    return


@app.cell
def _(mo):
    mo.md(r"""## データ結合""")
    return


@app.cell
def _(pd):
    df1 = pd.DataFrame(
        [
            ["a", 2],
            ["a", 0],
            ["b", 3],
            ["c", 2],
        ],
        columns=["A", "X"],
        index=range(1, 5),
    )

    df2 = pd.DataFrame([["a", 1], ["b", 3], ["d", 1]], columns=["A", "Y"])
    return df1, df2


@app.cell(hide_code=True)
def _(df1, df2):
    df1.merge(df2, how="cross", suffixes=("左", "右"))
    return


@app.cell
def _(df1, df2):
    df1.merge(df2, on="A", how="outer")
    return


@app.cell
def _(df1, df2):
    df1.merge(df2, on="A")
    return


@app.cell
def _(df1, df2, pd):
    pd.merge(df1, df2, on="A")
    return


@app.cell
def _(df1, df2):
    df1.merge(df2, left_on="X", right_index=True)
    return


@app.cell
def _(df1, df2, pd):
    pd.concat([df1, df2])
    return


@app.cell
def _(df1, df2, pd):
    pd.concat([df1, df2], join="inner")
    return


@app.cell
def _(df1, df2, pd):
    pd.concat([df1, df2], axis=1)
    return


@app.cell
def _(df1, df2):
    df1.merge(df2, left_index=True, right_index=True, how="outer")
    return


@app.cell
def _(df1, df2, pd):
    pd.concat([df1, df2], axis=1, join="inner")
    return


@app.cell
def _(df1, df2):
    df1.merge(df2, left_index=True, right_index=True)
    return


@app.cell
def _(df1, df2, pd):
    pd.concat([df1, df2], ignore_index=True)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## データの読み込み

    ### pandasでのデータの読み書き

    """
    )
    return


@app.cell(hide_code=True)
def _(pd):
    from pathlib import Path

    current_dir = Path(__file__).parent
    data_path = (current_dir / "data" / "ch02").resolve()
    csv_data = pd.read_csv(data_path / "法人データ.csv", encoding="utf-8")
    csv_data.iloc[:5, 1:7]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### ファイル形式

    [JSON](https://ecma-international.org/publications-and-standards/standards/ecma-404/)

    ### 文字コード

    [Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)
    """
    )
    return


if __name__ == "__main__":
    app.run()
