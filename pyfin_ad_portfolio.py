# -*- coding: utf-8 -*-
#    NumPyの読み込み
import numpy as np
#    CVXPYの読み込み
import cvxpy as cvx
#    Pandasの読み込み
import pandas as pd
#    MatplotlibのPyplotモジュールの読み込み
import matplotlib.pyplot as plt
#    日本語フォントの設定
from matplotlib.font_manager import FontProperties
import sys
if sys.platform.startswith('win'):
    FontPath = 'C:\Windows\Fonts\meiryo.ttc'
elif sys.platform.startswith('darwin'):
    FontPath = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
elif sys.platform.startswith('linux'):
    FontPath = '/usr/share/fonts/truetype/takao-gothic/TakaoExGothic.ttf'
jpfont = FontProperties(fname=FontPath)
# %% 収益率データの読み込み
R = pd.read_csv('asset_return_data.csv', index_col=0)
T = R.shape[0]
N = R.shape[1]
Mu = R.mean().values
Return_Dev = (R - Mu).values / T
# %% 平均絶対偏差最小化問題の設定
Weight = cvx.Variable(N)
Deviation = cvx.Variable(T)
Target_Return = cvx.Parameter(sign='positive')
Risk_AD = cvx.norm(Deviation, 1)
Opt_Portfolio = cvx.Problem(cvx.Minimize(Risk_AD),
                            [Return_Dev * Weight == Deviation,
                             Weight.T * Mu == Target_Return,
                             cvx.sum_entries(Weight) == 1.0,
                             Weight >= 0.0])
# %% 最小平均絶対偏差フロンティアの計算
V_Target = np.linspace(Mu.min(), Mu.max(), num=250)
V_Risk = np.zeros(V_Target.shape)
for idx, Target_Return.value in enumerate(V_Target):
    Opt_Portfolio.solve()
    V_Risk[idx] = Risk_AD.value
# %% 最小平均絶対偏差フロンティアのグラフの作成
fig1 = plt.figure(1, facecolor='w')
plt.plot(V_Risk, V_Target, 'k-')
plt.plot((R - Mu).abs().mean().values, Mu, 'kx')
plt.legend([u'最小平均絶対偏差フロンティア', u'個別資産'],
           loc='best', frameon=False, prop=jpfont)
plt.xlabel(u'平均絶対偏差(%)', fontproperties=jpfont)
plt.ylabel(u'期待収益率(%)', fontproperties=jpfont)
plt.show()
