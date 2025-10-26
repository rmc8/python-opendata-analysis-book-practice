import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # データの可視化とPlotly

    - [Matplotlib](https://matplotlib.org/)
    - [seaborn](https://seaborn.pydata.org/)
    - [Bokeh](https://bokeh.org/)
    - [Plotly.py](https://plotly.com/python/)
    - [Plotly Express](https://plotly.com/python/plotly-express/)

    ## Plotly.pyとPlotly Express
    """
    )
    return


@app.cell
def _():
    import pandas as pd

    plot_df = pd.DataFrame(
        data=[[4, 2], [1, 3]],
        index=pd.Index(["前期", "当期"], name="期間"),
        columns=pd.Index(["東京", "大阪"], name="地域"),
    )
    plot_df
    return pd, plot_df


@app.cell
def _(plot_df):
    import plotly.graph_objects as go

    trace1 = go.Bar(x=plot_df.index, y=plot_df["東京"], name="東京")
    trace2 = go.Bar(x=plot_df.index, y=plot_df["大阪"], name="大阪")
    go_fig = go.Figure([trace1, trace2], layout=go.Layout(barmode="stack"))
    go_fig.show()
    return (go,)


@app.cell
def _(pd, plot_df):
    tidy_df = pd.melt(
        plot_df.reset_index(),
        id_vars=["期間"],
        value_vars=["東京", "大阪"],
        value_name="金額",
    )
    tidy_df
    return (tidy_df,)


@app.cell
def _(tidy_df):
    import plotly.express as px

    ex_fig = px.bar(tidy_df, x="期間", y="金額", color="地域")
    ex_fig.show()
    return (px,)


@app.cell
def _():
    # from pathlib import Path
    # import plotly.io as pio
    # pio.kaleido.scope.chromium_args += ("--single-process",)
    # THIS_DIR = Path(__file__).parent
    # IMG_DIR = THIS_DIR / "img" / "chap04"
    # ex_fig.write_html("bar_graph.html")
    # IMG_DIR.exists()
    # ex_fig.write_image(file=(IMG_DIR / "bar_graph.png"))
    return


@app.cell
def _(pd):
    composition_df = pd.DataFrame(
        [
            ["必要生活費", "衣類", 20],
            ["必要生活費", "食費", 30],
            ["必要生活費", "住居費", 40],
            ["教養娯楽費", "教養", 15],
            ["教養娯楽費", "趣味娯楽", 20],
        ],
        columns=["大分類", "中分類", "金額"],
    )
    composition_df
    return (composition_df,)


@app.cell
def _(composition_df, px):
    pie_fig = px.pie(composition_df, names="中分類", values="金額")
    pie_fig.update_traces(textinfo="label+percent", textfont_size=20, showlegend=False)
    pie_fig.show()
    return


@app.cell
def _(composition_df, px):
    sunburst_fig = px.sunburst(composition_df, path=["大分類", "中分類"], values="金額")
    sunburst_fig.update_traces(textinfo="label+value", textfont_size=20)
    sunburst_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### ツリーマップ""")
    return


@app.cell
def _(composition_df, px):
    treemap_fig = px.treemap(composition_df, path=["大分類", "中分類"], values="金額")
    treemap_fig.update_traces(textinfo="label+value", textfont_size=20)
    treemap_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 量の比較と推移の可視化""")
    return


@app.cell
def _(pd):
    ts_df = pd.DataFrame(
        [
            [2020, "必要生活費", "衣類", 20],
            [2020, "必要生活費", "食費", 30],
            [2020, "必要生活費", "住居費", 35],
            [2020, "教養娯楽費", "教養", 15],
            [2020, "教養娯楽費", "趣味娯楽", 15],
            [2021, "必要生活費", "衣類", 20],
            [2021, "必要生活費", "食費", 40],
            [2021, "必要生活費", "住居費", 35],
            [2021, "教養娯楽費", "教養", 10],
            [2021, "教養娯楽費", "趣味娯楽", 25],
            [2022, "必要生活費", "衣類", 15],
            [2022, "必要生活費", "食費", 25],
            [2022, "必要生活費", "住居費", 40],
            [2022, "教養娯楽費", "教養", 15],
            [2022, "教養娯楽費", "趣味娯楽", 30],
        ],
        columns=["年", "大分類", "中分類", "金額"],
    ).assign(**{"日付": lambda df: pd.to_datetime(df["年"], format="%Y")})
    return (ts_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 棒グラフ""")
    return


@app.cell
def _(px, ts_df):
    bar_fig = px.bar(ts_df, x="年", y="金額", color="中分類")
    bar_fig.update_layout(xaxis={"dtick": 1})
    bar_fig.show()
    return


@app.cell
def _(px, ts_df):
    groupbar_fig = px.bar(ts_df, x="日付", y="金額", color="大分類", barmode="group")
    groupbar_fig.update_layout(
        xaxis={"dtick": "M12", "tickformat": "%Y", "ticksuffix": "年"}
    )
    groupbar_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 折れ線グラフ""")
    return


@app.cell
def _(px, ts_df):
    line_fig = px.line(ts_df, x="日付", y="金額", color="中分類", markers=True)
    line_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 構成割合の推移の可視化

    ### エリアチャート
    """
    )
    return


@app.cell
def _(px, ts_df):
    area_fig = px.area(ts_df, x="日付", y="金額", color="中分類")
    area_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### その他の構成割合の推移の可視化

    ## レイアウトとグラフの組み合わせ

    ### Plotly Expressのカラースケール
    """
    )
    return


@app.cell
def _(px):
    px.colors.qualitative.Plotly
    return


@app.cell
def _(px):
    color_fig = px.colors.qualitative.swatches()
    color_fig.show()
    return


@app.cell
def _(px):
    px.colors.qualitative.Alphabet
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### グラフの組み合わせ""")
    return


@app.cell
def _(go, ts_df):
    fig2 = go.Figure()
    for cat in ts_df["大分類"].unique():
        tmp_df = (
            ts_df.loc[ts_df["大分類"] == cat, ["日付", "金額"]]
            .groupby("日付")
            .sum()
            .reset_index()
        )
        # add_traceメソッドで各大分類ごとに描画領域に折れ線グラフを追加
        fig2.add_trace(
            go.Scatter(
                x=tmp_df["日付"],
                y=tmp_df["金額"],
                name=cat,
                mode="lines+markers",  # 折れ線グラフにマーカー(点)を表示
                line={"width": 4, "dash": "dash"},  # 線の幅と形状を設定
                marker={
                    "size": 15,
                    "symbol": "diamond",
                },  # マーカーのサイズと形状を設定
                yaxis="y1",  # y軸(縦軸)の1軸目を使用
            )
        )
    total_df = ts_df[["日付", "金額"]].groupby("日付").sum().reset_index()
    # 各年の総計を棒グラフとして追加
    fig2.add_trace(
        go.Bar(
            x=total_df["日付"],
            y=total_df["金額"],
            name="総計",
            yaxis="y2",  # y軸(縦軸)の2軸目を使用
            opacity=0.6,  # 不透明度を0.6に設定
        )
    )
    # レイアウトを更新
    fig2.update_layout(
        width=1000,  # 描画領域の横幅を設定
        height=500,  # 描画領域の縦幅を設定
        font={"size": 14},  # フォントサイズを設定
        xaxis={
            "dtick": "M12",  # x軸(横軸)の目盛り間隔を12ヶ月に設定
            "tickformat": "%Y",  # x軸(横軸)の目盛りの表示形式を設定
            "ticksuffix": "年",  # x軸(横軸)の目盛りに単位を追加
            "title": None,  # x軸(横軸)のタイトルを非表示
        },
        yaxis={
            "title": "大分類の金額",
            "side": "left",  # y軸(縦軸)の1軸目を左側に設定
        },
        yaxis2={
            "ticksuffix": "円",  # y軸(縦軸)の2軸目の目盛りに単位を追加
            "title": "総計の金額",
            "side": "right",  # y軸(縦軸)の2軸目を右側に設定
            "overlaying": "y",  # y軸(縦軸)の2軸目をy軸(縦軸)の1軸目に重ねて表示
        },
        legend={"x": 1.1},  # 凡例の位置を右寄りに設定
        legend_title_text="支出",  # 凡例のタイトルを設定
        title={
            "text": "年ごとの支出",
            "x": 0.5,  # タイトルの位置を中央に設定
        },
    )
    fig2.show()
    return


@app.cell
def _(go, px, ts_df):
    from plotly.subplots import make_subplots

    # 1行2列の描画領域を用意
    subplot_fig = make_subplots(
        rows=1, cols=2, subplot_titles=("棒グラフ", "折れ線グラフ")
    )
    # 棒グラフに設定するカラーと模様を用意
    colors_pattern = px.colors.qualitative.Pastel1
    shape_pattern = "/.+x\\"
    # 棒グラフの追加
    bar_data = ts_df.loc[ts_df["年"] == 2022, ["中分類", "金額"]]
    for n, cat_ in enumerate(bar_data["中分類"]):
        tmp_df_ = bar_data[bar_data["中分類"] == cat_]
        # add_traceメソッドで中分類ごとに色や模様の異なる棒グラフを追加
        subplot_fig.add_trace(
            go.Bar(
                x=tmp_df_["中分類"],
                y=tmp_df_["金額"],
                name=cat_,
                texttemplate="%{y}万円",  # texttemplateでy軸の金額を棒グラフ中に表示
                textfont_size=15,  # フォントサイズを設定
                textposition="inside",  # 棒グラフの内側に表示
                marker_color=colors_pattern[n],  # 棒グラフの色を設定
                marker_pattern_shape=shape_pattern[n],  # 棒グラフの模様を設定
            ),
            row=1,  # 1行目の描画領域に表示
            col=1,  # 1列目の描画領域に表示
        )
    # 折れ線グラフの追加
    line_data_ = ts_df.pivot_table(
        index="日付", columns="大分類", values="金額", aggfunc="sum"
    )
    for col in line_data_:
        # add_traceメソッドで大分類ごとに折れ線グラフを追加
        subplot_fig.add_trace(
            go.Scatter(
                x=line_data_.index,
                y=line_data_[col],
                name=col,
                mode="lines+markers",  # 折れ線グラフにマーカー(点)を表示
            ),
            row=1,  # 1行目の描画領域に表示
            col=2,  # 2列目の描画領域に表示
        )
    # グラフのレイアウトを更新
    subplot_fig.update_layout(
        width=1000,
        height=400,
        legend={
            "orientation": "h",  # "h" は水平（horizontal）を意味し、凡例の項目が水平方向に並ぶ
            "x": 0.5,  # 0.5 はグラフの水平方向の中央
            "y": -0.5,  # -0.5 は、グラフ領域外の下部（グラフの下端からさらに10%下）に凡例を配置
            "xanchor": "center",  # 凡例の中央が x で指定された位置に配置
            "yanchor": "top",  # 凡例の上端が y で指定された位置に配置
        },
    )
    # x軸(横軸)の設定
    subplot_fig.update_xaxes(
        tickformat="%Y/%m",  # x軸(横軸)の目盛りの表示形式を設定
        tickangle=45,  # x軸(横軸)の目盛りを45度傾けて表示
    )
    subplot_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 分布の可視化""")
    return


@app.cell
def _(pd):
    df = pd.DataFrame(
        [
            ["いちごストア株式会社", "A4491", "上場", "小売業", 50, 250],
            ["メガハード株式会社", "A3547", "上場", "製造業", 50, 300],
            ["百聞半導体株式会社", "A2704", "上場", "製造業", 20, 180],
            ["五十音サーチ株式会社", "A8008", "上場", "小売業", 30, 200],
            ["利根川通販株式会社", "A4342", "上場", "小売業", 100, 240],
            ["超手本株式会社", "A3674", "上場", "サービス業", 20, 150],
            ["源内自動車株式会社", "A7514", "非上場", "製造業", 10, 100],
            ["クローズサピエンス合同会社", "A0941", "非上場", "サービス業", None, 120],
            ["富価自動車株式会社", "J7203", "上場", "製造業", 60, 120],
            ["ハード通信株式会社", "J9984", "上場", "サービス業", 15, 50],
            ["株式会社財前", "J3994", "非上場", "サービス業", None, 30],
        ],
        columns=["会社名", "会社コード", "上場区分", "業種", "従業員数", "資本金"],
    )
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### ヒストグラム""")
    return


@app.cell
def _(df, px):
    hist_fig = px.histogram(df, x="資本金")
    hist_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 箱ひげ図とバイオリン図""")
    return


@app.cell
def _(df, px):
    box_fig = px.box(df, x="上場区分", y="資本金")
    box_fig.show()
    return


@app.cell
def _(df, px):
    violin_fig = px.violin(df, x="上場区分", y="資本金", box=True, points="all")
    violin_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 関係性の可視化

    ### 散布図
    """
    )
    return


@app.cell
def _(df, px):
    scatter_fig = px.scatter(df, x="資本金", y="従業員数", color="上場区分")
    scatter_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### ヒートマップ""")
    return


@app.cell
def _(df, pd):
    hdf = df.assign(
        **{
            "従業員数区分": pd.cut(df["従業員数"], bins=3),
            "資本金区分": pd.cut(df["資本金"], bins=3),
        }
    )
    cols = ["従業員数区分", "資本金区分"]
    crosstab = (
        hdf[cols]
        .pivot_table(
            index="従業員数区分",
            columns="資本金区分",
            aggfunc="size",
            observed=False,
        )
        .sort_index(ascending=False)
    )
    crosstab
    return (crosstab,)


@app.cell
def _(crosstab, px):
    im_fig = px.imshow(
        crosstab.values,
        x=[str(i) for i in crosstab.columns],
        y=[str(i) for i in crosstab.index],
        labels={"x": crosstab.columns.name, "y": crosstab.index.name},
        text_auto=True,
    )
    im_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### バブルチャート""")
    return


@app.cell
def _(px):
    gapminder_data = px.data.gapminder()
    gapminder_df = gapminder_data[gapminder_data["year"] == 2007]
    gapminder_df.head()
    return (gapminder_df,)


@app.cell
def _(gapminder_df, px):
    bubble_fig = px.scatter(
        gapminder_df,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
    )
    bubble_fig.show()
    return


if __name__ == "__main__":
    app.run()
