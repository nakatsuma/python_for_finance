# -*- coding: utf-8 -*-
#    NumPyの読み込み
import numpy as np
#    SciPyのstatsモジュールの読み込み
import scipy.stats as st
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
# %% 収益率データの読み込みとベンチマークの生成
R = pd.read_csv('asset_return_data.csv', index_col=0)
R = R.asfreq(pd.infer_freq(R.index))
T = R.shape[0]
N = R.shape[1]
np.random.seed(8888)
BenchmarkIndex = R.dot(np.tile(1.0/N, N)) + st.norm(0.0, 3.0).rvs(T)
# %% トラッキングエラー最小化問題のバックテスト
MovingWindow = 96
BackTesting = T - MovingWindow
V_Tracking = np.zeros(BackTesting)
Weight = cvx.Variable(N)
Error = cvx.Variable(MovingWindow)
TrackingError = cvx.sum_squares(Error)
Asset_srT = R / np.sqrt(T)
Index_srT = BenchmarkIndex / np.sqrt(T)
for Month in range(0, BackTesting):
    Asset = Asset_srT.values[Month:(Month + MovingWindow), :]
    Index = Index_srT.values[Month:(Month + MovingWindow)]
    Min_TrackingError = cvx.Problem(cvx.Minimize(TrackingError),
                                    [Index - Asset*Weight == Error,
                                     cvx.sum_entries(Weight) == 1.0,
                                     Weight >= 0.0])
    Min_TrackingError.solve()
    V_Tracking[Month] = R.values[Month + MovingWindow, :].dot(Weight.value)
# %% バックテストの結果のグラフ
fig1 = plt.figure(1, facecolor='w')
plt.plot(list(range(1, BackTesting + 1)), BenchmarkIndex[MovingWindow:], 'k-')
plt.plot(list(range(1, BackTesting + 1)), V_Tracking, 'k--')
plt.legend([u'ベンチマーク・インデックス', u'インデックス・ファンド'],
           loc='best', frameon=False, prop=jpfont)
plt.xlabel(u'運用期間(年）', fontproperties=jpfont)
plt.ylabel(u'収益率(%)', fontproperties=jpfont)
plt.xticks(list(range(12, BackTesting + 1, 12)),
           pd.date_range(R.index[MovingWindow], periods=BackTesting//12,
                         freq='AS').year)
plt.show()
