# pc-labo-python-basic

PC-LABO（pc-labo.online）の「基本情報技術者試験問題に挑戦しよう！」シリーズなど、Pythonのコードを使った記事を読むための、最低限のPython入門シリーズ用リポジトリである。

「つくって学ぶ」記事のコードを読み解けるようになることを目標に、3回に分けて構成している。

## 方針

- 1記事＝1フォルダとし、`01_xxx`, `02_xxx` のように連番で管理する
- 各フォルダには、記事中で「つくってみよう」として紹介したコードを置く
- 環境構築なしで、Python標準ライブラリのみで動くコードにする（`python3 xxx.py` で即実行できる状態を保つ）

## フォルダ構成

| フォルダ | 記事タイトル | 内容 |
| --- | --- | --- |
| [01_variables_types_print](./01_variables_types_print) | PC-LABOを試すためのPython入門（第1回）～変数・型・print～ | 変数・型・四則演算・比較演算子・f-stringの書式指定を、バイト⇔ビット変換プログラムで確認する |
| [02_if_for_function_dict](./02_if_for_function_dict) | PC-LABOを試すためのPython入門（第2回）～条件分岐・ループ・関数の引数・辞書～ | if/for/辞書/デフォルト引数を、得点からのランク判定＋集計プログラムで確認する |
| [03_class_stdlib](./03_class_stdlib) | PC-LABOを試すためのPython入門（第3回）～クラスと標準ライブラリの読み方～ | クラス（Product, Node）とimport、このブログで使う標準ライブラリを確認する |

## 動作環境

- Python 3.x（標準ライブラリのみ使用）
- 実行コマンドはOSによって異なる場合がある。Mac/Linuxは `python3 xxx.py`、Windowsは `py xxx.py` を試してほしい（`python`/`python3`はMicrosoft Storeへの誘導用ダミーに奪われていることがある）

## 関連ブログ

- [PC-LABO（つくって学ぶ体験型ブログ）](https://pc-labo.online/)
- [pc-labo-fe-exam-python](https://github.com/HappyTalk10/pc-labo-fe-exam-python)（基本情報技術者試験問題シリーズ用リポジトリ）
