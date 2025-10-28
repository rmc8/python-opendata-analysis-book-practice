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
    # オープンデータ・経済統計・公的統計

    ## 経済統計と公的統計とは

    [統計法](https://www.soumu.go.jp/toukei_toukatsu/index/seido/1-1n.htm)

    ## 世界の公的機関とオープンデータ

    ### 国際連合のデータ

    - [国際連合](https://www.un.org/en/)
    - [国際連合 加盟国一覧](https://www.unic.or.jp/info/un/un_organization/member_nations/)
    - [国際連合 専門機関および関連機関](https://www.unic.or.jp/info/un/unsystem/specialized_agencies/)
    - [UNdata](http://data.un.org/Default.aspx)
    - [国連経済社会局人口部](https://www.un.org/development/desa/pd/)
    - [World Population Prospects](https://population.un.org/wpp/)
    - [World Population Prospects Download Files](https://population.un.org/wpp/downloads)

    ### Data CommonsとUN Data Commons for the SDGs

    - [Data Commons](https://datacommons.org/)
    - [Data Commons API](https://docs.datacommons.org/api/)
    - [UN Data Commons for the SDGs](https://unstats.un.org/UNSDWebsite/undatacommons/sdgs)

    ### 世界銀行のデータ

    - [世界銀行](https://www.worldbank.org/)
    - [World Bank Open Data](https://data.worldbank.org/)
    - [DataBank](https://databank.worldbank.org/)
    - [World Bank Data Catalog](https://datacatalog.worldbank.org/)
    - [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information)

    ### 国際通貨基金（I MF）のデータ

    - [国際通貨基金](https://www.imf.org/ja/Home)
    - [IMF DATA](https://www.imf.org/en/Data)

    ### 世界保健機関（WHO）のデータ

    - [世界保健機関](https://www.who.int/)
    - [data.who.int](https://data.who.int/)
    - [WHO のData ページ](https://www.who.int/data)
    - [COVID-19 のダッシュボード](https://covid19.who.int/)

    ### 世界貿易機関（WTO）のデータ

    - [世界貿易機関](https://www.wto.org/)
    - [WTO Data](https://data.wto.org/en)
    - [WTO Stats ポータルサイト](https://stats.wto.org/)

    ### 経済協力開発機構（OECD）のデータ

    - [経済協力開発機構](https://www.oecd.org/)
    - [OECD Data](https://data.oecd.org/)

    ### 欧州連合（EU）のEurostat

    - [欧州連合](https://european-union.europa.eu/index_en)
    - [Eurostat](https://ec.europa.eu/eurostat)
    - [Eurostat のDataサイト](https://ec.europa.eu/eurostat/web/main/data)

    ### 米国統計局のデータ

    - [商務省](https://www.commerce.gov/)
    - [国勢調査局](https://www.census.gov/)
    - [経済分析局](https://www.bea.gov/)
    - [USCB API](https://www.census.gov/data.html)
    - [BEA API](https://www.bea.gov/tools)
    - [Commerce Data Hub](https://data.commerce.gov/)
    - [労働統計局](https://www.bls.gov/)
    - [BLS Public Data API](https://www.bls.gov/developers/home.htm)

    ### 米国FRBのFRED

    - [連邦準備制度理事会](https://www.federalreserve.gov/)
    - [セントルイス連邦準備銀行](https://www.stlouisfed.org/)
    - [FRED](https://fred.stlouisfed.org/)

    ## 日本の公的機関とオープンデータ

    ### 政府統計の総合窓口e-Stat

    - [政府統計の総合窓口e-Stat](https://www.e-stat.go.jp/)
    - [総務省統計局](https://www.stat.go.jp/)

    ### 金融・市場データ

    - [日本銀行の時系列統計データ検索サイト](https://www.stat-search.boj.or.jp/index.html)
    - [EDINET](https://disclosure2.edinet-fsa.go.jp/WEEK0010.aspx)
    - [J-Quants](https://jpx-jquants.com/)
    - [投信総合検索ライブラリー](https://toushin-lib.fwg.ne.jp/FdsWeb/)

    ### 法人・産業データ

    - [法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)
    - [EDINET](https://disclosure2.edinet-fsa.go.jp/weee0010.aspx)
    - [日本年金機構](https://www.nenkin.go.jp/index.html)
    - [厚生年金保険・健康保険適用事業所検索システム](https://www2.nenkin.go.jp/do/search_section/)
    - [gBizINFO](https://info.gbiz.go.jp/)
    - [gBizINFO の出典元](https://info.gbiz.go.jp/resource/index.html)
    - [gBizINFO API](https://info.gbiz.go.jp/api/index.html)

    ### 地理・気象データ

    - [国土交通省](https://www.mlit.go.jp/)
    - [国土数値情報ダウンロードサイト](https://nlftp.mlit.go.jp/)
    - [国土交通省のGIS](https://nlftp.mlit.go.jp/kokjo/inspect/landclassification/download.html)
    - [e-Stat GIS](https://www.e-stat.go.jp/gis)
    - [不動産情報ライブラリ](https://www.reinfolib.mlit.go.jp/)
    - [不動産情報ライブラリ API](https://www.reinfolib.mlit.go.jp/help/apiManual/)
    - [国土地理院](https://www.gsi.go.jp/)
    - [地理院地図](https://maps.gsi.go.jp/)
    - [国土地理院 GitHub アカウント](https://github.com/gsi-cyberjapan)
    - [地理院地図 GitHub リポジトリ](https://github.com/gsi-cyberjapan/gsimaps)
    - [東京大学空間情報科学研究センター](https://www.csis.u-tokyo.ac.jp/)
    - [シンプルジオコーディング](https://geocode.csis.u-tokyo.ac.jp/home/simple-geocoding/)
    - [地理院地図とシンプルジオコーディング](https://github.com/gsi-cyberjapan/gsimaps/issues/29)
    - [気象庁](https://www.jma.go.jp/jma/index.html)
    - [気象庁の数値データページへのリンク集](https://www.jma.go.jp/jma/menu/arcdata.html)
    - [郵便番号・デジタルアドレスAPI](https://guide-biz.da.pf.japanpost.jp/api/)

    ### 地方のデータとRESAS

    - [地域経済分析システムRESAS](https://resas.go.jp/)
    - [東京都オープンデータカタログサイト](https://portal.data.metro.tokyo.lg.jp/)
    - [e-Govポータル データベースサイト一覧](https://data.e-gov.go.jp/info/databasesite)

    ### デジタル庁のe-GovポータルとJapan Dashboard

    - [e-Gov ポータル](https://www.e-gov.go.jp/)
    - [デジタル庁](https://www.digital.go.jp/)
    - [e-Gov ポータル 統計に関するページ](https://www.e-gov.go.jp/about-government/statistics.html)
    - [Japan Dashboard](https://www.digital.go.jp/resources/japandashboard)

    ## 日本の公的統計とe-Stat

    ### e-Statとは

    - [政府統計の総合窓口 e-Stat](https://www.e-stat.go.jp/)
    - [総務省統計局](https://www.stat.go.jp/)
    - [独立行政法人統計センター](https://www.nstac.go.jp/)
    - [利用ガイドのページ](https://www.e-stat.go.jp/usageguide)
    - [統計ダッシュボード](https://dashboard.e-stat.go.jp/)
    - [ユーザ登録](https://www.e-stat.go.jp/mypage/user/preregister/)

    ### e-Stat API機能

    - [e-Stat API機能](https://www.e-stat.go.jp/api/)

    ### e-Stat API登録とアプリケーションID取得

    - [政府統計の総合窓口(e-Stat)API 機能利用規約](https://www.e-stat.go.jp/api/terms-of-use)
    - [マイページへのログイン画面](https://www.e-stat.go.jp/mypage/login)

    ### e-Stat APIをPythonで利用する
    """
    )
    return


@app.cell
def _():
    from urllib.parse import urljoin
    import requests
    import pandas as pd

    return pd, requests, urljoin


@app.cell
def _():
    import os

    app_id = os.getenv("E_STAT_API_KEY")
    version = "3.0"
    base_url = f"https://api.e-stat.go.jp/rest/{version}/"
    return app_id, base_url


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### 統計表情報を取得する""")
    return


@app.cell
def _(app_id, base_url, requests, urljoin):
    statslist_endpoint = "app/json/getStatsList"
    statslist_url = urljoin(base_url, statslist_endpoint)
    statslist_params = {"appId": app_id, "serverYears": 2020, "limit": 100}
    statslist_res = requests.get(statslist_url, params=statslist_params)
    statslist_out = statslist_res.json()
    return (statslist_out,)


@app.cell
def _(statslist_out):
    statslist_out.keys()
    return


@app.cell
def _(statslist_out):
    statslist_out["GET_STATS_LIST"].keys()
    return


@app.cell
def _(statslist_out):
    statslist_out["GET_STATS_LIST"]["DATALIST_INF"].keys()
    return


@app.cell
def _(pd, statslist_out):
    table_inf = pd.json_normalize(
        statslist_out,
        record_path=["GET_STATS_LIST", "DATALIST_INF", "TABLE_INF"],
        sep="_",
    )
    table_inf.columns
    return (table_inf,)


@app.cell
def _(table_inf):
    table_inf[
        ["@id", "TITLE_SPEC_TABLE_NAME", "TITLE_$", "OVERALL_TOTAL_NUMBER"]
    ].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""https://www.e-stat.go.jp/api/api-dev/faq#q_5_7""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### メタ情報を取得する""")
    return


@app.cell
def _(app_id):
    stats_data_id = "0002070010"
    data_params = {
        "appId": app_id,
        "statsDataId": stats_data_id,
        "lvCata01": "4",
        "cdCat02": "04",
        "cdCat03": "A00",
        "cdTimeFrom": "2020000101",
        "cdTimeTo": "2020001212",
    }
    return (data_params,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### CSVで取得する""")
    return


@app.cell
def _(base_url, data_params, requests, urljoin):
    from io import StringIO

    csv_data_endpoint = "app/getSimpleStatsData"
    csv_data_url = urljoin(base_url, csv_data_endpoint)
    csv_data_res = requests.get(csv_data_url, params=data_params)
    print(csv_data_res.text[:1000])
    return StringIO, csv_data_res


@app.cell
def _(StringIO, csv_data_res, pd):
    pd.read_csv(StringIO(csv_data_res.text), skiprows=28).head()
    return


@app.cell
def _(StringIO, csv_data_res, pd):
    # 最初の[1]で2分割したリストの2つ目を指定し、[1:]で冒頭の改行\nを除く
    pd.read_csv(StringIO(csv_data_res.text.split('"VALUE"')[1][1:])).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### JSONで取得する""")
    return


@app.cell
def _(base_url, data_params, requests, urljoin):
    data_endpoint = "app/json/getStatsData"
    data_url = urljoin(base_url, data_endpoint)
    data_res = requests.get(data_url, params=data_params)
    data = data_res.json()
    return (data,)


@app.cell
def _(data):
    data.keys()
    return


@app.cell
def _(data):
    data["GET_STATS_DATA"].keys()
    return


@app.cell
def _(data):
    data["GET_STATS_DATA"]["STATISTICAL_DATA"].keys()
    return


@app.cell
def _(data):
    data["GET_STATS_DATA"]["STATISTICAL_DATA"]["CLASS_INF"].keys()
    return


@app.cell
def _(data):
    data["GET_STATS_DATA"]["STATISTICAL_DATA"]["CLASS_INF"]["CLASS_OBJ"][0].keys()
    return


@app.cell
def _(data):
    data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"].keys()
    return


@app.cell
def _(data, pd):
    value_df = pd.json_normalize(
        data, record_path=["GET_STATS_DATA", "STATISTICAL_DATA", "DATA_INF", "VALUE"]
    )
    value_df.head()
    return (value_df,)


@app.cell
def _(value_df):
    renamed_df = value_df.rename(
        columns=lambda col: col.lstrip("@").replace("$", "value")
    )
    renamed_df.head()
    return (renamed_df,)


@app.cell
def _(data):
    note = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["NOTE"]
    note
    return (note,)


@app.cell
def _(note, renamed_df):
    import numpy as np

    note_char = [n["@char"] for n in note]
    assigned_df = renamed_df.assign(
        **{"value": lambda df: df["value"].replace(note_char, np.nan).astype(float)}
    )
    return assigned_df, np


@app.cell
def _(np, pd):
    def missing_to_nan(
        value: pd.DataFrame,
        note: dict[str, str] | dict[dict[str, str]],
    ) -> pd.DataFrame:
        if isinstance(note, list):
            note_cher = [n["@char"] for n in note]
        elif isinstance(note, dict):
            note_char = note["@char"]
        else:
            print(f"引数noteの型は辞書またはリストではありません： {type:note}")
            return value
        return value.assign(
            **{"value": lambda df: df["value"].replace(note_char, np.nan).astype(float)}
        )

    return


@app.cell
def _(assigned_df, data, pd):
    def _(assigned_df: pd.DataFrame):
        class_obj = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["CLASS_INF"]["CLASS_OBJ"]
        for co in class_obj:
            class_entries = co["CLASS"]
            # "CLASS"はlistとdictの場合があります
            if isinstance(class_entries, list):
                cls_df = pd.DataFrame(class_entries)
            elif isinstance(class_entries, dict):
                cls_df = pd.DataFrame(pd.Series(class_entries)).T
            else:
                print(
                    "想定外のCLASS の型:",
                    type(class_entries),
                    "\nCLASS の値: ",
                    class_entries,
                )
                continue
            cls_df = cls_df.set_index("@code").rename(
                columns=lambda col: f"{co['@name']}{col.lstrip('@')}"
            )
            assigned_df = assigned_df.merge(
                cls_df, left_on=co["@id"], right_index=True, how="left"
            ).rename(columns={co["@id"]: f"{co['@name']}code"})
        return assigned_df

    combined_df = _(assigned_df)
    combined_df.columns
    return (combined_df,)


@app.cell
def _(combined_df):
    attr_map = {
        "value": "値",
        "code": "コード",
        "name": "",
        "level": "階層レベル",
        "unit": "単位",
        "parentCode": "親コード",
        "addInf": "追加情報",
        "tab": "表章項目",
        "cat": "分類",
        "area": "地域",
        "time": "時間軸",
        "annotation": "注釈記号",
    }

    def _convert(c):
        for k, v in attr_map.items():
            if k in c:
                return c.replace(k, v)
        return c

    converted_df = combined_df.rename(columns=_convert)
    return (converted_df,)


@app.cell
def _(converted_df):
    converted_df.head(1).T
    return


@app.cell
def _():
    from estat import (
        get_metainfo,
        get_statsdata,
        cleansing_statsdata,
        colname_to_japanese,
        create_hierarchy_dataframe,
    )
    from utils import time_magic

    return (
        cleansing_statsdata,
        colname_to_japanese,
        get_metainfo,
        get_statsdata,
        time_magic,
    )


@app.cell
def _(app_id, get_metainfo):
    statsDataId = "0002070010"
    meta = get_metainfo(app_id, statsDataId)
    metadata = meta["GET_META_INFO"]["METADATA_INF"]
    total_num = metadata["TABLE_INF"]["OVERALL_TOTAL_NUMBER"]
    total_num
    return (statsDataId,)


@app.cell
def _(app_id, get_statsdata, statsDataId, time_magic):
    @time_magic
    def _():
        res = get_statsdata(app_id, statsDataId)
        print(res["GET_STATS_DATA"]["STATISTICAL_DATA"]["RESULT_INF"]["NEXT_KEY"])
        return res

    data2 = _()
    data2
    return (data2,)


@app.cell
def _(
    app_id,
    cleansing_statsdata,
    colname_to_japanese,
    data,
    data2,
    get_statsdata,
    pd,
    statsDataId,
    time_magic,
):
    @time_magic
    def _():
        dfs = []
        dfs.append(colname_to_japanese(cleansing_statsdata(data2)))
        max_position = 50000
        while "NEXT_KEY" in data2["GET_STATS_DATA"]["STATISTICAL_DATA"]["RESULT_INF"]:
            start_position = data2["GET_STATS_DATA"]["STATISTICAL_DATA"][
                "RESULT_INF"
            ].get("NEXT_KEY")
            print(f"NEXT_KEY: {start_position}")
            if start_position > max_position:
                break
            data3 = get_statsdata(
                app_id, statsDataId, params={"startPosition": start_position}
            )
            dfs.append(colname_to_japanese(cleansing_statsdata(data)))
        df = pd.concat(dfs)
        return df

    df = _()
    df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 統計Dashboard API

    - [e-Stat 統計ダッシュボード](https://dashboard.e-stat.go.jp/)
    - [統計ダッシュボードWebAPI](https://dashboard.e-stat.go.jp/static/api)
    - [利用規約](https://dashboard.e-stat.go.jp/static/terms)
    """
    )
    return


@app.cell
def _(requests):
    indicator_url = "https://dashboard.e-stat.go.jp/api/1.0/Json/getIndicatorInfo"
    indicator_params = {"StatName": "家計調査"}
    indicator_res = requests.get(indicator_url, params=indicator_params)
    indicator = indicator_res.json()
    indicator_metadata = indicator["GET_META_INDICATOR_INF"]["METADATA_INF"]
    indicator_classobj = indicator_metadata["CLASS_INF"]["CLASS_OBJ"][0]
    print(indicator_classobj["@name"], indicator_classobj["@code"])
    return


@app.cell
def _(requests):
    data_url_ = "https://dashboard.e-stat.go.jp/api/1.0/Json/getData"
    data_params_ = {"IndicatorCode": "0704010101000010000", "TimeFrom": "20200100"}
    data_res_ = requests.get(data_url_, params=data_params_)
    data_ = data_res_.json()
    data_["GET_STATS"]["STATISTICAL_DATA"]["DATA_INF"]["DATA_OBJ"][:2]
    return (data_,)


@app.cell
def _(data_, pd):
    data_df_ = pd.DataFrame(
        [
            d["VALUE"]
            for d in data_["GET_STATS"]["STATISTICAL_DATA"]["DATA_INF"]["DATA_OBJ"]
        ]
    )
    data_df = data_df_.rename(columns=lambda col: col.lstrip("@").replace("$", "value"))
    data_df.head()
    return (data_df,)


@app.cell
def _(pd, requests):
    region_url = "https://dashboard.e-stat.go.jp/api/1.0/Json/getRegionInfo"
    region_res = requests.get(region_url)
    region = region_res.json()
    region_dfs = []
    region_co = region["GET_META_REGION_INF"]["METADATA_INF"]["CLASS_INF"]["CLASS_OBJ"]
    for c in region_co:
        region_dfs += [pd.DataFrame(c["CLASS"])]
    region_df = pd.concat(region_dfs)
    region_df = region_df.rename(
        columns=lambda col: col.lstrip("@").replace("name", "地域")
    )
    region_df.tail()
    return (region_df,)


@app.cell
def _(data_df, region_df):
    data_df__ = data_df.merge(
        region_df[["regionCode", "地域"]], on="regionCode", how="left"
    )
    return (data_df__,)


@app.cell
def _(data_df__, pd):
    data_df___ = data_df__.assign(
        **{
            "年": lambda df: df["time"].astype(int) // 10000,
            "月": lambda df: df["time"].str[4:6].astype(int),
            "年月": lambda df: pd.to_datetime(
                df["年"].astype(str) + "-" + df["月"].astype(str) + "-01"
            ),
        }
    )
    data_df___.head()
    return


@app.cell
def _(pd, requests):
    socialevent_url = "https://dashboard.e-stat.go.jp/api/1.0/Json/getSocialEventInfo"
    socialevent_params = {"TimeFrom": "20200100"}
    socialevent_res = requests.get(socialevent_url, params=socialevent_params)
    socialevent = socialevent_res.json()
    socialevent_df = pd.json_normalize(
        socialevent,
        record_path=["GET_META_SOCIAL_INFO", "METADATA_INF", "CLASS_INF", "CLASS_OBJ"],
    )
    socialevent_df.drop("CLASS", axis=1)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
