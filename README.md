# 中妻照雄「Pythonによるファイナンス入門」朝倉書店

[朝倉書店ウェブサイト](https://www.asakura.co.jp/books/isbn/978-4-254-12894-9/ "朝倉書店ウェブサイト")

## 正誤表

+ [ERRATA.md](ERRATA.md)

## PythonとCVXPYのインストール手順 (Anaconda 2019.03 対応)

### ステップ1: Anacondaのインストール

1. 古いAnacondaがインストールされているときは，この[手順](https://docs.anaconda.com/anaconda/install/uninstall/)でアンインストールしておく．

2. Anacondaのインストーラー (Windows, macOS or Linux) を[ここ](https://www.anaconda.com/distribution/)から入手する.

3. ダウンロードしたインストーラーをダブルクリックしてAnacondaのインストールを行う．

### ステップ2: Microsoft Visual Studio Build Toolsのインストール (Windowsのみで必要)

1. Microsoft Visual Studio Build Toolsのインストーラーを[ここ](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)から入手する．

2. ダウンロードしたインストーラーをダブルクリックしてインストールを行うが，インストールすべきものは`C++ build tools`だけである．[ここ](https://drive.google.com/file/d/0B4GsMXCRaSSIOWpYQkstajlYZ0tPVkNQSElmTWh1dXFaYkJr/view?usp=sharing)を参照．

### ステップ3: CVXPYを実行する環境の設定

`Anaconda Powershell Prompt` (Windows) あるいは `Terminal` (macOS, Linux) を立ち上げて，

```IPython
(base) PS C:\Users\Thomas> conda create -n finance jupyterlab seaborn spyder
```

とする．続けて

```IPython
(base) PS C:\Users\Thomas> conda activate finance
```

とすると，以下のようにプロンプトが変わる．

```IPython
(finance) PS C:\Users\Thomas>
```

**注意:** IPythonを開始する際には必ず`conda activate finance`を先に実行しておくこと．

さらに

```IPython
(finance) PS C:\Users\Thomas> python -m ipykernel install --user --name finance --display-name "Python (Finance)"
```

とすれば，環境の設定が完了する．

## Jupyter Notebookを始める方法

### 方法1: Anaconda Navigatorから起動する方法

`Anaconda Navigator`を`Start Menu` (Windows) か `Launchpad` (macOS) から起動する． あるいは，`Anaconda Powershell Prompt` (Windows) か `Terminal` (macOS, Linux) を立ち上げて，

```IPython
(base) PS C:\Users\Thomas> anaconda-navigator
```

としてもよい．そして，`Anaconda Navigator`で`Jupyter Notebook`の`Launch`ボタンをクリックする．

### 方法2: CLIから起動する方法

`Anaconda Powershell Prompt` (Windows) か `Terminal` (macOS, Linux) を立ち上げて，

```IPython
(base) PS C:\Users\Thomas> conda activate finance
(finance) PS C:\Users\Thomas> jupyter notebook
```

とする．

方法1あるいは方法2を実行すると，規定のブラウザーが立ち上がり，Jupyter Notebookが起動する．その画面の右上にある`New`のプルダウンメニューの中にある`Python (Finance)`を選んでNotebookを開始すればよい．

**注意:** `New`のプルダウンメニューの中にある`Python 3`を選んでNotebookを開始すると，CVXPYを使用することができない．

## Pythonコード

### CVXPY1.0リリースに伴う修正点

+ 「sign='positive'」を「nonneg=True」に変更する．
+ 「sum_entries」を「sum」に変更する．
+ 最適化問題を安定的に解くため，以下のようにソルバーをECOSに設定する．

```Python
  Opt_Portfolio.solve(solver=cvx.ECOS)
```

+ 修正を施したコードの名前の末尾には「_ver1」がついている．

### 第2章

+ コード2.1 [pyfin\_interest.py](pyfin_interest.py)
+ コード2.2 [pyfin\_npv\_irr.py](pyfin_npv_irr.py)

### 第3章

+ コード3.1 [pyfin\_bond\_yield\_price.py](pyfin_bond_yield_price.py)
+ コード3.2 [pyfin\_bond\_duration\_convexity.py](pyfin_bond_duration_convexity.py)
+ コード3.3 [pyfin\_bond\_yield\_price.py](pyfin_bond_yield_price.py)

### 第4章

+ コード4.1 [pyfin\_mvf\_example1.py](pyfin_mvf_example1.py)
+ コード4.2 [pyfin\_mvf\_example2.py](pyfin_mvf_example2.py), [pyfin\_mvf\_example2\_ver1.py](pyfin_mvf_example2_ver1.py)
+ コード4.3 [pyfin\_asset\_return\_simulation.py](pyfin_asset_return_simulation.py)
+ コード4.4 [pyfin\_mvf\_example3.py](pyfin_mvf_example3.py), [pyfin\_mvf\_example3\_ver1.py](pyfin_mvf_example3_ver1.py)

### 第5章

+ コード5.1 [pyfin\_ad\_portfolio.py](pyfin_ad_portfolio.py), [pyfin\_ad\_portfolio\_ver1.py](pyfin_ad_portfolio_ver1.py)
+ コード5.2 [pyfin\_sv\_portfolio.py](pyfin_sv_portfolio.py), [pyfin\_sv\_portfolio\_ver1.py](pyfin_sv_portfolio_ver1.py)
+ コード5.3 [pyfin\_es\_portfolio.py](pyfin_es_portfolio.py), [pyfin\_es\_portfolio\_ver1.py](pyfin_es_portfolio_ver1.py)
+ コード5.4 [pyfin\_risk\_parity.py](pyfin_risk_parity.py)
+ コード5.5 [pyfin\_min\_tracking\_error.py](pyfin_min_tracking_error.py), [pyfin\_min\_tracking\_error\_ver1.py](pyfin_min_tracking_error_ver1.py)

### 第6章

+ コード6.1 [pyfin\_option\_pricing.py](pyfin_option_pricing.py)
+ コード6.2 [pyfin\_black\_scholes.py](pyfin_black_scholes.py)

### コード4.3で生成した人工データの例

+ [asset\_return\_data.csv](asset_return_data.csv)
