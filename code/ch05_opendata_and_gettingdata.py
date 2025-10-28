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
    # オープンデータとデータ取得

    ## オープンデータ

    ### オープンデータとは

    - [非営利組織Open Knowledge Foundation](https://okfn.org/en/)
    - [OPEN DATA HANDBOOK](https://opendatahandbook.org/guide/ja/what-is-open-data/)
    - [full Open Definition](http://opendefinition.org/okd/)
    - [オープンデータ基本指針](https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/f7fde41d-ffca-4b2a-9b25-94b8a701a037/f1e42cee/20240705_resources_data_guideline_01.pdf)
    - [官民データ活用推進基本法](https://laws.e-gov.go.jp/law/428AC1000000103)
    - [デジタル社会推進会](https://www.digital.go.jp/councils/social-promotion)
    - [政府CIO ポータル](https://cio.go.jp/policy-opendata)
    - [デジタル庁](https://www.digital.go.jp/resources/open_data)

    ### オープンデータの公開レベル

    [オープンデータのための5 つ星スキーム](https://5stardata.info/ja/)

    #### RDFとLOD

    - [W3C](https://www.w3.org/)
    - [e-Stat 統計LOD](https://data.e-stat.go.jp/lodw/outline/abstraction)

    ## データ取得

    ### CSV等ファイルダウンロード

    [EDINET](https://disclosure2.edinet-fsa.go.jp/week0010.aspx)
    """
    )
    return


@app.cell
def _():
    from pathlib import Path

    import pandas as pd

    current_dir = Path(__file__).parent
    data_path = (current_dir / "data" / "ch09").resolve()
    csv_data = pd.read_csv(
        data_path / "EdinetcodeDlInfo.csv", encoding="cp932", skiprows=1
    )
    csv_data.head()
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### APIとPythonのRequestsライブラリ

    #### REST API

    #### Pythonライブラリのrequests

    - [urllib.request](https://docs.python.org/ja/3/library/urllib.request.html)
    - [Requests](https://requests.readthedocs.io/en/latest/)
    - [Requests(GitHub)](https://github.com/psf/requests/blob/main/src/requests/sessions.py)
    """
    )
    return


@app.cell
def _():
    import requests

    url = "https://dashboard.e-stat.go.jp/api/1.0/Json/getData"
    params = {
        "IndicatorCode": "0704010101000010000",
        "TimeFrom": "20200100",
    }
    res = requests.get(url=url, params=params)
    return params, requests, res, url


@app.cell
def _(res):
    res.status_code
    return


@app.cell
def _(res):
    res.encoding
    return


@app.cell
def _(res):
    res.text[:100]
    return


@app.cell
def _(res):
    json_data = res.json()
    json_data.keys()
    return (json_data,)


@app.cell
def _(json_data):
    json_data["GET_STATS"]["STATISTICAL_DATA"]["DATA_INF"]["DATA_OBJ"][:2]
    return


@app.cell
def _(params, requests, url):
    with requests.Session() as session:
        res2 = session.request(method="GET", url=url, params=params)
        json_data2 = res2.json()
    return (json_data2,)


@app.cell
def _(json_data2):
    json_data2["GET_STATS"]["STATISTICAL_DATA"]["DATA_INF"]["DATA_OBJ"][:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### APIキーの設定""")
    return


@app.cell
def _(requests):
    import os

    api_key = os.getenv("E_STAT_API_KEY", "")
    data_url = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
    data_params = {
        "appId": api_key,
        "statsDataId": "0003000795",
        "limit": 100,
    }
    data_res = requests.get(url=data_url, params=data_params)
    data_res.json()["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"][:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### OpenAPIとSwagger

    - [OpenAPI](https://www.openapis.org/)
    - [Swagger](https://swagger.io/)
    - [gBizINFO REST API](https://info.gbiz.go.jp/hojin/swagger-ui/index.html)

    #### LODとSPARQL

    - [e-Stat 統計LOD](https://data.e-stat.go.jp/lodw/)
    - [SPARQL](https://www.w3.org/TR/sparql11-query/)
    - [e-Stat 統計LOD「統計表の基本的なデータ構造」](https://data.e-stat.go.jp/lodw/outline/abstraction#1-1-2-1-2)
    - [SPARQLWrapper](https://sparqlwrapper.readthedocs.io/en/latest/index.html)
    - [e-Stat 統計LOD「統計LOD の基本的な使い方」](https://data.e-stat.go.jp/lodw/lodw/index.php/guidelines/howto)
    """
    )
    return


@app.cell
def _():
    from SPARQLWrapper import JSON, SPARQLWrapper

    SPARQL_ENDPOINT = "http://data.e-stat.go.jp/lod/sparql/alldata/query"
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    sparql.setReturnFormat(JSON)
    return (sparql,)


@app.cell
def _(sparql):
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#>
    PREFIX estat-measure: <http://data.e-stat.go.jp/lod/ontology/measure/>
    PREFIX cd-dimension: <http://data.e-stat.go.jp/lod/ontology/crossDomain/dimension/>
    PREFIX cd-code: <http://data.e-stat.go.jp/lod/ontology/crossDomain/code/>
    PREFIX g00200521-dimension-2010:<http://data.e-stat.go.jp/lod/ontology/g00200521/dimension/2010/>
    PREFIX g00200521-code-2010:<http://data.e-stat.go.jp/lod/ontology/g00200521/code/2010/>
    select  ?year ?population
    where {
          ?s estat-measure:population ?population ;
             sdmx-dimension:refArea / rdfs:label "新宿区"@ja ;
             cd-dimension:timePeriod ?year ;
             cd-dimension:sex cd-code:sex-all ;
             cd-dimension:nationality cd-code:nationality-japan ;
             g00200521-dimension-2010:area g00200521-code-2010:area-all ;
             cd-dimension:age cd-code:age-all .
    }
        """)
    return


@app.cell
def _(sparql):
    ret = sparql.queryAndConvert()
    ret
    return (ret,)


@app.cell
def _(sparql):
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#>
    PREFIX estat-measure: <http://data.e-stat.go.jp/lod/ontology/measure/>
    PREFIX cd-dimension: <http://data.e-stat.go.jp/lod/ontology/crossDomain/dimension/>
    PREFIX cd-code: <http://data.e-stat.go.jp/lod/ontology/crossDomain/code/>
    PREFIX g00200521-dimension-2010:<http://data.e-stat.go.jp/lod/ontology/g00200521/dimension/2010/>
    PREFIX g00200521-code-2010:<http://data.e-stat.go.jp/lod/ontology/g00200521/code/2010/>
    select  ?s ?year ?population
    where {
          ?s estat-measure:population ?population ;
             sdmx-dimension:refArea / rdfs:label "新宿区"@ja ;
             cd-dimension:timePeriod ?year ;
             cd-dimension:sex cd-code:sex-all ;
             cd-dimension:nationality cd-code:nationality-japan ;
             g00200521-dimension-2010:area g00200521-code-2010:area-all ;
             cd-dimension:age cd-code:age-all .
    }
        """)
    ret2 = sparql.queryAndConvert()
    ret2
    return (ret2,)


@app.cell
def _(ret2):
    ret2.keys()
    return


@app.cell
def _(ret2):
    ret2["head"]
    return


@app.cell
def _(ret2):
    ret2["results"].keys()
    return


@app.cell
def _(pd, ret):
    sparql_df = pd.json_normalize(ret, record_path=["results", "bindings"])
    sparql_df
    return (sparql_df,)


@app.cell
def _(pd, sparql_df):
    sparql_df.columns = pd.MultiIndex.from_tuples(
        [tuple(col.split(".")) for col in sparql_df.columns]
    )
    sparql_df
    return


if __name__ == "__main__":
    app.run()
