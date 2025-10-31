import marimo

__generated_with = "0.17.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import os
    from pathlib import Path

    import numpy as np
    import pandas as pd
    import plotly
    import plotly.express as px
    import plotly.graph_objs as go
    import requests
    from dotenv import load_dotenv
    from estat import (cleansing_statsdata, colname_to_japanese, get_metainfo,
                       get_statsdata)
    from plotly.subplots import make_subplots
    from utils import time_magic

    return (
        Path,
        cleansing_statsdata,
        colname_to_japanese,
        get_metainfo,
        get_statsdata,
        go,
        make_subplots,
        os,
        px,
    )


@app.cell
def _(Path, os):
    app_id = os.getenv("E_STAT_API_KEY")
    current_dir = Path(__file__).parent
    data_path = (current_dir / "data" / "ch07").resolve()
    return (app_id,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 人口と国勢調査

    - [国勢調査](https://www.e-stat.go.jp/statistics/00200521)
    - [令和2 年国勢調査（2020 年）の公表](https://www.stat.go.jp/data/kokusei/2020/pdf/schedule.pdf)
    """
    )
    return


@app.cell
def _(app_id, get_metainfo):
    pop_statsDataId = "0003410380"
    pop_meta = get_metainfo(app_id, pop_statsDataId)
    pop_metadata = pop_meta["GET_META_INFO"]["METADATA_INF"]
    poo_total_num = pop_metadata["TABLE_INF"]["OVERALL_TOTAL_NUMBER"]
    poo_total_num
    return (pop_statsDataId,)


@app.cell
def _(
    app_id,
    cleansing_statsdata,
    colname_to_japanese,
    get_statsdata,
    pop_statsDataId,
):
    pop_data = get_statsdata(app_id, pop_statsDataId)
    pop_value = colname_to_japanese(cleansing_statsdata(pop_data))
    pop_value.columns
    return (pop_value,)


@app.cell
def _(mo):
    mo.md(r"""### 人口ピラミッド""")
    return


@app.cell
def _(pop_value):
    pop_value["男女_時系列"].unique()
    return


@app.cell
def _(pop_value):
    pyramid_cols = [
        "年齢（５歳階級）_時系列コード",
        "年齢（５歳階級）_時系列",
        "男女_時系列",
        "値",
    ]
    pyramid_cond = pop_value["表章項目"] == "人口"
    pyramid_cond &= pop_value["男女_時系列"] != "総数"
    pyramid_cond &= pop_value["年齢（５歳階級）_時系列"] != "総数"
    pyramid_cond &= ~pop_value["年齢（５歳階級）_時系列"].str.contains("再掲")
    pyramid_cond &= pop_value["時間軸（調査年）"] == "2020年_不詳補完値"
    pyramid_df = pop_value.loc[pyramid_cond, pyramid_cols]
    pyramid_df.head()
    return (pyramid_df,)


@app.cell
def _(pyramid_df):
    pop_pyramid = (
        pyramid_df.sort_values("年齢（５歳階級）_時系列コード")
        .assign(
            **{
                "人口": pyramid_df["値"].mask(
                    pyramid_df["男女_時系列"] == "男", -pyramid_df["値"]
                )
            }
        )
        .rename(
            columns={
                "年齢（５歳階級）_時系列": "年齢（５歳階級）",
                "男女_時系列": "性別",
            }
        )
    )
    pop_pyramid.head()
    return (pop_pyramid,)


@app.cell
def _(go, pop_pyramid, px):
    pyramid_fig = px.bar(
        pop_pyramid, x="人口", y="年齢（５歳階級）", color="性別", orientation="h"
    )
    pyramid_fig.update_layout(
        width=900,
        height=600,
        font={"size": 14},
        xaxis=go.layout.XAxis(
            tickvals=[-4_000_000, -2_000_000, 0, 2_000_000, 4_000_000],
            ticktext=["400万", "200万", "0", "200万", "400万"],
        ),
    )
    pyramid_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 人口推移""")
    return


@app.cell
def _(pop_value):
    pop_cols = [
        "時間軸（調査年）コード",
        "年齢（５歳階級）_時系列コード",
        "年齢（５歳階級）_時系列",
        "値",
    ]
    pop_cond = pop_value["表章項目"] == "人口"
    pop_cond &= pop_value["男女_時系列"] == "総数"
    pop_cond &= pop_value["年齢（５歳階級）_時系列"] != "総数"
    pop_cond &= ~pop_value["年齢（５歳階級）_時系列"].str.contains("再掲")
    pop_cond &= ~pop_value["時間軸（調査年）"].str.contains("不詳補完値")
    pop_df_tmp = pop_value.loc[pop_cond, pop_cols]
    return (pop_df_tmp,)


@app.cell
def _(pop_df_tmp):
    pop_df = pop_df_tmp.assign(
        **{
            "年": pop_df_tmp["時間軸（調査年）コード"].astype(int) // 1_000_000,
            "年齢（５歳階級）": pop_df_tmp["年齢（５歳階級）_時系列コード"]
            + "_"
            + pop_df_tmp["年齢（５歳階級）_時系列"],
        }
    )
    return (pop_df,)


@app.cell
def _(pop_df, px):
    pop_colors = px.colors.sequential.dense[:3]
    pop_colors += px.colors.sequential.matter[:10]
    pop_colors += px.colors.sequential.deep[:11]
    pop_fig = px.bar(
        pop_df,
        x="年",
        y="値",
        color="年齢（５歳階級）",
        color_discrete_sequence=pop_colors,
    )
    pop_fig.update_layout(
        width=900,
        height=700,
        font={"size": 14},
        xaxis={"ticksuffix": "年", "title": None},
        yaxis={"tickformat": ",.0f", "ticksuffix": "人", "title": None},
    )
    pop_fig.show()
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 人口動態

    - [人口動態調査](https://www.mhlw.go.jp/toukei/list/81-1.html)
    - [公表](https://www.mhlw.go.jp/toukei/kouhyou/e-stat_81-1.xml)
    """
    )
    return


@app.cell
def _(app_id, get_metainfo):
    vital_statsDataId = "0003411561"
    vital_meta = get_metainfo(app_id, vital_statsDataId)
    vital_metadata = vital_meta["GET_META_INFO"]["METADATA_INF"]
    vital_total_num = vital_metadata["TABLE_INF"]["OVERALL_TOTAL_NUMBER"]
    vital_total_num
    return (vital_statsDataId,)


@app.cell
def _(
    app_id,
    cleansing_statsdata,
    colname_to_japanese,
    get_statsdata,
    vital_statsDataId,
):
    vital_data = get_statsdata(app_id, vital_statsDataId)
    vital_value_df = colname_to_japanese(cleansing_statsdata(vital_data))
    vital_value_df.columns
    return (vital_value_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 出生数と死亡数""")
    return


@app.cell
def _(vital_value_df):
    vital_value = vital_value_df.assign(
        **{
            "年": vital_value_df["時間軸(年次)コード"].astype(int) // 1_000_000
        }  # vital_value => vital_value_df
    )
    vital_cond = vital_value["人口動態総覧"].isin(["出生数", "死亡数"])
    vital_df = vital_value.loc[vital_cond, ["年", "人口動態総覧", "値"]]
    vital_df.head()
    return vital_df, vital_value


@app.cell
def _(vital_value):
    vital_delta = vital_value.loc[
        vital_value["人口動態総覧"] == "自然増減数", ["年", "値"]
    ]
    delta_pop = vital_delta.sort_values("年").rename(columns={"値": "自然増減数"})
    return (delta_pop,)


@app.cell
def _(delta_pop, px, vital_df):
    vital_fig = px.line(vital_df, x="年", y="値", color="人口動態総覧", markers=True)
    vital_fig.add_bar(x=delta_pop["年"], y=delta_pop["自然増減数"], name="自然増減数")
    vital_fig.update_layout(
        width=1200,
        height=650,
        font={"size": 24},
        xaxis={"ticksuffix": "年", "title": None},
        yaxis={"tickformat": ",.0f", "ticksuffix": "人", "title": None},
    )
    vital_fig.show()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### 合計特殊出生率

    -[人口置換水準](https://www.ipss.go.jp/syoushika/tohkei/Popular/Popular2020.asp?chap=0)
    """
    )
    return


@app.cell
def _(vital_value):
    tfr_cond = vital_value["人口動態総覧"] == "合計特殊出生率"
    tfr_cond &= vital_value["値"].notna()
    tfr_df = vital_value.loc[tfr_cond, ["年", "人口動態総覧", "値"]]
    tfr_df.head()
    return (tfr_df,)


@app.cell
def _(go, px, tfr_df):
    tfr_fig = px.line(tfr_df, x="年", y="値", color="人口動態総覧")
    tfr_fig.add_trace(
        go.Scatter(
            x=[1947, 2021],
            y=[2.07, 2.07],
            mode="lines",
            line={"dash": "dash"},
            name="人口置換水準",
        )
    )
    tfr_fig.update_layout(
        width=900,
        height=450,
        font={"size": 18},
        xaxis={"ticksuffix": "年", "title": None},
        yaxis={"ticksuffix": "人", "title": None},
    )
    tfr_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 婚姻件数と離婚件数""")
    return


@app.cell
def _(app_id, get_metainfo):
    devorce_statsDataId = "0003411864"
    divorce_meta = get_metainfo(app_id, devorce_statsDataId)
    devorce_metadata = divorce_meta["GET_META_INFO"]["METADATA_INF"]
    devorce_total_num = devorce_metadata["TABLE_INF"]["OVERALL_TOTAL_NUMBER"]
    devorce_total_num
    return (devorce_statsDataId,)


@app.cell
def _(
    app_id,
    cleansing_statsdata,
    colname_to_japanese,
    devorce_statsDataId,
    get_statsdata,
):
    divorce_data = get_statsdata(app_id, devorce_statsDataId)
    divorce_value = colname_to_japanese(cleansing_statsdata(divorce_data))
    divorce_value.columns
    return (divorce_value,)


@app.cell
def _(divorce_value):
    divorce_cols = ["時間軸(年次)コード", "同居期間コード", "同居期間", "値"]
    divorce_cond = divorce_value["単位"] == "件"
    divorce_cond &= ~divorce_value["同居期間"].isin(
        ["離婚件数_総数", "離婚件数_5年未満"]
    )
    divorce_df_tmp = divorce_value.loc[divorce_cond, divorce_cols]
    return (divorce_df_tmp,)


@app.cell
def _(divorce_df_tmp):
    divorce_df = divorce_df_tmp.assign(
        **{
            "同居期間": divorce_df_tmp["同居期間コード"].str[-3:]
            + "_"
            + divorce_df_tmp["同居期間"],
            "年": divorce_df_tmp["時間軸(年次)コード"].astype(int) // 1_000_000,
        }
    )
    return (divorce_df,)


@app.cell
def _(vital_value):
    marriage_cond = vital_value["人口動態総覧"].isin(["婚姻件数", "離婚件数"])
    marriage_cond &= vital_value["年"] >= 1947
    marriage_df = vital_value.loc[marriage_cond, ["年", "人口動態総覧", "値"]]
    pivot_df = marriage_df.pivot(columns="人口動態総覧", index="年", values="値")
    pivot_df.head()
    return (pivot_df,)


@app.cell
def _(divorce_df, go, make_subplots, pivot_df, px):
    # サブプロットの作成
    marriage_fig = make_subplots(
        rows=1, cols=2, subplot_titles=("婚姻・離婚件数", "離婚内訳")
    )
    # 左側の婚姻・離婚件数グラフ
    marriage_fig.add_trace(
        go.Scatter(
            x=pivot_df.index, y=pivot_df["婚姻件数"], mode="lines", name="婚姻件数"
        ),
        row=1,
        col=1,
    )
    marriage_fig.add_trace(
        go.Scatter(
            x=pivot_df.index, y=pivot_df["離婚件数"], mode="lines", name="離婚件数"
        ),
        row=1,
        col=1,
    )
    # 右側の離婚内訳エリアグラフ(matterのカラーが不足するので一つカラーコード追加)
    divorce_colors = px.colors.sequential.matter + ["#EF553B"]
    for n, t in enumerate(divorce_df["同居期間"].unique()):
        df_filtered = divorce_df[divorce_df["同居期間"] == t]
        marriage_fig.add_trace(
            go.Scatter(
                x=df_filtered["年"],
                y=df_filtered["値"],
                name=t,
                marker={"color": divorce_colors[n]},
                stackgroup="divorcegroup",
            ),
            row=1,
            col=2,
        )
    marriage_fig.update_layout(width=1200, height=550, font={"size": 14})
    # 左側グラフのX軸とY軸の設定
    marriage_fig.update_xaxes(ticksuffix="年", row=1, col=1)
    marriage_fig.update_yaxes(tickformat=",", ticksuffix="人", row=1, col=1)
    # 右側グラフのX軸とY軸の設定
    marriage_fig.update_xaxes(ticksuffix="年", row=1, col=2)
    marriage_fig.update_yaxes(tickformat=",", ticksuffix="人", row=1, col=2)
    marriage_fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 人口推計

    - [人口推計](https://www.stat.go.jp/data/jinsui/index.html)
    - [公表](https://www.stat.go.jp/data/kouhyou/e-stat_jinsui.xml)

    """
    )
    return


@app.cell
def _(app_id, estimates_total_num, get_metainfo):
    pop_estimates_statsDataId = "0003448228"
    estimates_meta = get_metainfo(app_id, pop_estimates_statsDataId)
    estimates_metadata = estimates_meta["GET_META_INFO"]["METADATA_INF"]
    estimate_total_num = estimates_metadata["TABLE_INFO"]["OVERALL_TOTAL_NUMBER"]
    estimates_total_num
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
