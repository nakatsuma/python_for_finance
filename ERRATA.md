# 「Pythonによるファイナンス入門」正誤表

## 2018年11月12日改定

### 誤植

#### 5ページ1行目

+ （誤）批々木 (2001)
+ （正）枇々木 (2001)

#### 16ページ表2.1

+ 丸印のマークの記号はo（小文字のオー）

#### 42ページ1行目

+ （誤）キャッシュフローは(3.2)で与えられるから，
+ （正）キャッシュフローは(3.1)で与えられるから，

#### コード3.2 pyfin\_bond\_duration\_convexity.py

+ 第52行の最後に＼を追加する

#### コード5.4 pyfin\_risk\_parity.py

+ 第6行のaをとる

### 動作環境

#### CVXPYとWindows版Anacondaの互換性（2018年3月16日に確認，2018年11月12日に追記）

+ Anacondaのバージョン5.1.0において，CVXPYが3.x系においてもWindows上で動作することを確認した．
+ しかし，CVXPYはバージョン3.7に未対応のため，Anacondaのバージョン5.3以降では，以下の方法でインストールする必要がある．

```IPython
(base) C:\Users\Thomas> conda create -n finance python=3.6 jupyterlab seaborn spyder cvxgrp::cvxpy
```

+ この方法でインストールされるCVXPYはバージョン0.4である
+ これにより **Jupyter Notebook (finance)** および **Spyder (finance)** という項目がスタートメニューに作成される．ここからJupyter NotebookやSpyderを起動すればCVXPYを使用できる．
+ IPythonを使用する場合は，以下のコマンドを実行してからIPythonを開始する．

```IPython
(base) C:\Users\Thomas> conda activate finance
```

#### CVXPY1.0リリースに伴う修正点

+ 「sign='positive'」を「nonneg=True」に変更する
+ 「sum_entries」を「sum」に変更する
+ 修正を施したコードの名前の末尾には「_ver1」がついている

#### Ubuntuにおける日本語フォントの変更（2018年11月7日に追記）

+ Ubuntuにおける日本語フォントをTakaoExGothic.ttfからTakaoPGothic.ttfに変更した．
