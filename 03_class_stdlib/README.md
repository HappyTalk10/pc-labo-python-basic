# クラスと標準ライブラリの読み方

PC-LABOを試すためのPython入門シリーズ第3回。クラス（class, `__init__`, self）の基本と、importによる標準ライブラリの使い方を、Productクラス・Nodeクラス・itertools・hashlibの例で確認する。

対応記事：PC-LABOを試すためのPython入門（第3回）～クラスと標準ライブラリの読み方～

## 実行方法

```
py class_stdlib.py
```

（Mac/Linuxの場合は `python3 class_stdlib.py`）

## 確認していること

- クラスの定義（`class`、`__init__`、`self`、メソッド）と、インスタンスの作成
- 2分探索木の記事で使うNodeクラスの基本形（`left=None` などのデフォルト引数）
- `import` と `from ... import ...` の2通りの書き方
- `itertools.product`、`hashlib.sha256` など、このブログで使う標準ライブラリの例
