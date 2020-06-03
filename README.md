# 中妻照雄「Pythonによるファイナンス入門」朝倉書店

[朝倉書店ウェブサイト](https://www.asakura.co.jp/books/isbn/978-4-254-12894-9/ "朝倉書店ウェブサイト")

---

+ [正誤表](ERRATA.md)
+ [PythonとCVXPYのインストール手順](#python%e3%81%a8cvxpy%e3%81%ae%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e6%89%8b%e9%a0%86)
  + [ステップ1: Anacondaのインストール](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%971-Anaconda%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  + [ステップ2: Microsoft Visual Studio Build Toolsのインストール (Windowsのみで必要)](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%972-Microsoft-Visual-Studio-Build-Tools%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB-Windows%E3%81%AE%E3%81%BF%E3%81%A7%E5%BF%85%E8%A6%81)
  + [ステップ3: CVXPYを実行する環境の設定](#%E3%82%B9%E3%83%86%E3%83%83%E3%83%973-CVXPY%E3%82%92%E5%AE%9F%E8%A1%8C%E3%81%99%E3%82%8B%E7%92%B0%E5%A2%83%E3%81%AE%E8%A8%AD%E5%AE%9A)
+ [Jupyter Notebookを始める方法](#Jupyter-Notebook%E3%82%92%E5%A7%8B%E3%82%81%E3%82%8B%E6%96%B9%E6%B3%95)
  + [方法1: Anaconda Navigatorから起動する方法](#%E6%96%B9%E6%B3%951-Anaconda-Navigator%E3%81%8B%E3%82%89%E8%B5%B7%E5%8B%95%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)
  + [方法2: CLIから起動する方法](#%E6%96%B9%E6%B3%952-CLI%E3%81%8B%E3%82%89%E8%B5%B7%E5%8B%95%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)
+ [Pythonコード](#Python%E3%82%B3%E3%83%BC%E3%83%89)
  + [CVXPY1.0リリースに伴う修正点](#CVXPY10%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E3%81%AB%E4%BC%B4%E3%81%86%E4%BF%AE%E6%AD%A3%E7%82%B9)
  + [第2章](#%E7%AC%AC2%E7%AB%A0)
  + [第3章](#%E7%AC%AC3%E7%AB%A0)
  + [第4章](#%E7%AC%AC4%E7%AB%A0)
  + [第5章](#%E7%AC%AC5%E7%AB%A0)
  + [第6章](#%E7%AC%AC6%E7%AB%A0)

---

## 正誤表

+ [ERRATA.md](ERRATA.md)
  
## PythonとCVXPYのインストール手順

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

ここで

```IPython
(finance) PS C:\Users\Thomas> pip install cvxpy
```

とすると，CVXPYがインストールされる．最後に

```IPython
(finance) PS C:\Users\Thomas> python -m ipykernel install --user --name finance --display-name "Python (Finance)"
```

とすれば，環境の設定が完了する．

**注意:** Windowsでは，この作業により **Jupyter Notebook (finance)** および **Spyder (finance)** という項目がスタートメニューに作成されるので，ここからJupyter NotebookやSpyderを起動できる．

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

### CVXPY1.1リリースに伴う修正点

+ `Parameter()`で定義される変数は最適化問題の中で和か積の形で使われるようにする．ここでは期待ショートフォール最適化問題が当てはまる．
+ 行列やベクトルの積を表現するには`*`の代わりに`@`を使う．
+ 修正を施したコードの名前の末尾には「_ver1_1」がついている．

### CVXPY1.0リリースに伴う修正点

+ 「sign='positive'」を「nonneg=True」に変更する．
+ 「sum_entries」を「sum」に変更する．
+ 最適化問題を安定的に解くため，以下のようにソルバーをECOSに設定する．

```Python
  Opt_Portfolio.solve(solver=cvx.ECOS)
```

+ 修正を施したコードの名前の末尾には「_ver1」がついている．

### 第2章

+ コード2.1 [pyfin\_interest.py](python/pyfin_interest.py)
+ コード2.2 [pyfin\_npv\_irr.py](python/pyfin_npv_irr.py)

### 第3章

+ コード3.1 [pyfin\_bond\_yield\_price.py](python/pyfin_bond_yield_price.py)
+ コード3.2 [pyfin\_bond\_duration\_convexity.py](python/pyfin_bond_duration_convexity.py)
+ コード3.3 [pyfin\_bond\_yield\_price.py](python/pyfin_bond_yield_price.py)

### 第4章

+ コード4.1 [pyfin\_mvf\_example1.py](python/pyfin_mvf_example1.py)
+ コード4.2 [pyfin\_mvf\_example2.py](python/pyfin_mvf_example2.py), [pyfin\_mvf\_example2\_ver1.py](python/pyfin_mvf_example2_ver1.py),[pyfin\_mvf\_example2\_ver1\_1.py](python/pyfin_mvf_example2_ver1_1.py)
+ コード4.3 [pyfin\_asset\_return\_simulation.py](python/pyfin_asset_return_simulation.py)
+ コード4.3で生成した人工データの例 [asset\_return\_data.csv](python/asset_return_data.csv)
+ コード4.4 [pyfin\_mvf\_example3.py](python/pyfin_mvf_example3.py), [pyfin\_mvf\_example3\_ver1.py](python/pyfin_mvf_example3_ver1.py),
[pyfin\_mvf\_example3\_ver1\_1.py](python/pyfin_mvf_example3_ver1_1.py)

### 第5章

+ コード5.1 [pyfin\_ad\_portfolio.py](python/pyfin_ad_portfolio.py), [pyfin\_ad\_portfolio\_ver1.py](python/pyfin_ad_portfolio_ver1.py),
[pyfin\_ad\_portfolio\_ver1\_1.py](python/pyfin_ad_portfolio_ver1_1.py)
+ コード5.2 [pyfin\_sv\_portfolio.py](python/pyfin_sv_portfolio.py), [pyfin\_sv\_portfolio\_ver1.py](python/pyfin_sv_portfolio_ver1.py),
[pyfin\_sv\_portfolio\_ver1\_1.py](python/pyfin_sv_portfolio_ver1_1.py)
+ コード5.3 [pyfin\_es\_portfolio.py](python/pyfin_es_portfolio.py), [pyfin\_es\_portfolio\_ver1.py](python/pyfin_es_portfolio_ver1.py),
[pyfin\_es\_portfolio\_ver1\_1.py](python/pyfin_es_portfolio_ver1_1.py)
+ コード5.4 [pyfin\_risk\_parity.py](python/pyfin_risk_parity.py)
+ コード5.5 [pyfin\_min\_tracking\_error.py](python/pyfin_min_tracking_error.py), [pyfin\_min\_tracking\_error\_ver1.py](python/pyfin_min_tracking_error_ver1.py),
[pyfin\_min\_tracking\_error\_ver1\_1.py](python/pyfin_min_tracking_error_ver1_1.py)

### 第6章

+ コード6.1 [pyfin\_option\_pricing.py](python/pyfin_option_pricing.py)
+ コード6.2 [pyfin\_black\_scholes.py](python/pyfin_black_scholes.py)
