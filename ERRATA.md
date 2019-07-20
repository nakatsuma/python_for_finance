# 「Pythonによるファイナンス入門」正誤表

## 2019年7月20日改定

### 誤植

#### 5ページ1行目

+ （誤）批々木 (2001)
+ （正）枇々木 (2001)

#### 16ページ表2.1

+ 丸印のマークの記号はo（小文字のオー）

#### 42ページ1行目

+ （誤）キャッシュフローは(3.2)で与えられるから，
+ （正）キャッシュフローは(3.1)で与えられるから，

#### 123ページ8行目

+ （誤）maximum difersification portfolio
+ （正）maximum diversification portfolio

#### コード3.2 pyfin\_bond\_duration\_convexity.py

+ 第52行の最後に＼を追加する

#### コード5.4 pyfin\_risk\_parity.py

+ 第6行のaをとる

### 動作環境

#### 最新版のCVXPYをインストールする方法（2019年7月20日に追記）

まずAnaconda Powershell Prompt (Windows) あるいはターミナル (macOS、Linux) を開き，

```IPython
(base) PS C:\Users\Thomas> conda create -n finance jupyterlab seaborn spyder
```

を実行する．

Windowsでは，これにより **Jupyter Notebook (finance)** および **Spyder (finance)** という項目がスタートメニューに作成されるので，ここからJupyter NotebookやSpyderを起動できる．

続いて，以下のコマンド

```IPython
(base) PS C:\Users\Thomas> conda activate finance
```

を実行すると，プロンプトが

```IPython
(finance) PS C:\Users\Thomas>
```

と変わる．ここで続けて

```IPython
(finance) PS C:\Users\Thomas> pip install cvxpy
```

を実行すると，CVXPYがインストールされる．最後に

```IPython
(finance) PS C:\Users\Thomas> python -m ipykernel install --user --name finance --display-name "Python (Finance)"
```

を実行すると，`Python (Finance)`というカーネルが作成される．

#### ターミナルからIPython，Jupyter Notebook，Spyderを起動する方法

Anaconda Powershell Prompt (Windows) あるいはターミナル (macOS、Linux) を開き，

```IPython
(base) PS C:\Users\Thomas> conda activate finance
```

を実行する．そして，以下を実行する．

+ IPythonを起動する場合

```IPython
(finance) PS C:\Users\Thomas> ipython
```

+ Jupyter Notebookを起動する場合

```IPython
(finance) PS C:\Users\Thomas> jupyter notebook
```

+ Spyderを起動する場合

```IPython
(finance) PS C:\Users\Thomas> spyder
```

#### CVXPY1.0リリースに伴う修正点（2019年7月20日に追記）

+ 「sign='positive'」を「nonneg=True」に変更する
+ 「sum_entries」を「sum」に変更する
+ 修正を施したコードの名前の末尾には「_ver1」がついている
+ 最適化問題を安定的に解くためにソルバーをECOSに変更した

#### Ubuntuにおける日本語フォントの変更（2018年11月7日に追記）

+ Ubuntuにおける日本語フォントをTakaoExGothic.ttfからTakaoPGothic.ttfに変更した．
