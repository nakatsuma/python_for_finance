# -*- coding: utf-8 -*-
#   NumPyの読み込み
import numpy as np
#   NumPyのPolynomialモジュールの読み込み
import numpy.polynomial.polynomial as pol
#   MatplotlibのPyplotモジュールの読み込み
import matplotlib.pyplot as plt
#   日本語フォントの設定
from matplotlib.font_manager import FontProperties
import sys
if sys.platform.startswith('win'):
    FontPath = 'C:\Windows\Fonts\meiryo.ttc'
elif sys.platform.startswith('darwin'):
    FontPath = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
elif sys.platform.startswith('linux'):
    FontPath = '/usr/share/fonts/truetype/takao-gothic/TakaoExGothic.ttf'
jpfont = FontProperties(fname=FontPath)
#%% キャッシュフローのグラフ
Periods = np.linspace(0, 4, 5)
V_CF = np.array([[-5.0, 1.5, 1.5, 1.5, 1.5],
                 [-7.0, 2.0, 2.0, 2.0, 2.0],
                 [-9.0, 4.0, 3.0, 2.0, 1.0],
                 [-9.0, 1.0, 2.0, 3.0, 4.0]])
V_Title = [u'事業A', u'事業B', u'事業C', u'事業D']
fig1 = plt.figure(1, facecolor='w')
for fig_num in range(4):
    plt.subplot(2, 2, fig_num + 1)
    plt.bar(Periods, V_CF[fig_num, :], color=(0.5, 0.5, 0.5))
    plt.title(V_Title[fig_num], fontproperties=jpfont)
    plt.axhline(color='k', linewidth=0.5)
    plt.ylim(-10, 5)
    if fig_num == 2 or fig_num == 3:
        plt.xlabel(u'時点', fontproperties=jpfont)
    if fig_num == 0 or fig_num == 2:
        plt.ylabel(u'キャッシュフロー', fontproperties=jpfont)
    if fig_num == 0 or fig_num == 1:
        plt.xticks([])
plt.show()
#%% 正味現在価値の計算
def NPV(r, CF):
    #       r: 割引率 (%)
    #      CF: キャッシュフロー
    #  Output: 正味現在価値
    x = 1.0 / (1.0 + 0.01 * r)
    return pol.polyval(x, CF)
r = 5 # 割引率はパーセント単位
V_NPV = np.zeros(4)
for cf_num in range(4):
    V_NPV[cf_num] = NPV(r, V_CF[cf_num, :])
#%% 内部収益率の計算
def IRR(CF):
    #      CF: キャッシュフロー
    #  Output: 内部収益率 (%)
    Roots = pol.polyroots(CF)
    Real = np.real(Roots[np.isreal(Roots)])
    Positive = np.asscalar(Real[Real > 0.0])
    return (1.0 / Positive - 1.0) * 100
V_IRR = np.zeros(4)
for cf_num in range(4):
    V_IRR[cf_num] = IRR(V_CF[cf_num, :])
