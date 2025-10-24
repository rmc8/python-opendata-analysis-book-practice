# Repository Guidelines

## このリポジトリについて
- 『Pythonではじめるオープンデータ分析』の練習用リポジトリです。
- 原著リポジトリ: https://github.com/python-opendata-analysis/python-opendata-analysis-book
- uv と marimo を使って環境管理・実行・ノート作成を行います。

## プロジェクト構成と配置
- ルート: `main.py`(エントリポイント), `pyproject.toml`(依存定義), `uv.lock`, `README.md`。
- データ: `code/data/chXX/` に章ごとの CSV/XLSX と補足 README。
- 分析コード: `code/` 配下に追加し、章と内容で命名 (例: `code/ch13_analysis.py`)。既存データの移動や改名は避ける。

## 開発・実行コマンド (uv)
- 環境構築: `uv sync` (仮想環境作成 + 依存インストール)
- 実行: `uv run python main.py`
- 依存追加: `uv add <package>` (自動で `pyproject.toml` と `uv.lock` を更新)
- テスト(任意): `uv run pytest -q`

## Marimo ワークフロー
- 置き場所: `notebooks/` (例: `notebooks/ch10_overview.py`)
- 作成: `uv run marimo new notebooks/ch10_overview.py`
- 編集: `uv run marimo edit notebooks/ch10_overview.py`
- 起動: `uv run marimo run notebooks/ch10_overview.py --port 8888`
- 出力: `uv run marimo export html notebooks/ch10_overview.py -o reports/ch10_overview.html`

## コーディング規約と命名
- Python 3.13。公開関数は型ヒントと docstring を付与。
- PEP 8、インデント 4 スペース、行長 88–100 目安。整形/静的解析を導入する場合は Black/Ruff を推奨。
- 命名: モジュール/関数/変数は `snake_case`、クラスは `PascalCase`。派生データは小文字 `snake_case`。

## テスト方針
- フレームワーク: `pytest`。`tests/` に `test_*.py` を配置。
- 外部ネットワーク禁止。fixtures や `tests/data/` のキャッシュを使用。
- 主要変換処理と入出力境界を重点的にカバー。

## コミット / PR
- コミットは簡潔な現在形。`feat:` `fix:` `docs:` `refactor:` `chore:` を推奨。
- PR は目的・主要変更・実行/確認手順・データ出典を記載し、関連 Issue をリンク。無関係ファイルの一括整形は避ける。

## セキュリティと注意
- 秘密情報は `.env` に保存し (コミット禁止)、`python-dotenv` で読み込み。必要に応じて `.env.example` を用意。
- 50MB 超のバイナリはコミットしない。データは `code/data/` に配置し、可能なら取得手順を README 等に記載。
