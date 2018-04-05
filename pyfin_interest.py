# -*- coding: utf-8 -*-
#    NumPyの読み込み
import numpy as np
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
# %% 単利と複利の比較
r = 0.2        # 利率 20%
Maturity = 10  # 運用期間 10年
Simple_Rate = 1.0 + r * np.linspace(0, Maturity, Maturity + 1)
Compound_1year = np.r_[1.0, np.cumprod(np.tile(1.0 + r, Maturity))]
Compound_6month = np.r_[1.0, np.cumprod(np.tile((1.0 + r/2.0)**2, Maturity))]
Continuous_Rate = np.exp(r*np.linspace(0, Maturity, Maturity + 1))
fig1 = plt.figure(1, facecolor='w')
plt.plot(Simple_Rate, 'k-')
plt.plot(Compound_1year, 'k--')
plt.plot(Compound_6month, 'k-.')
plt.plot(Continuous_Rate, 'k:')
plt.legend([u'単利', u'1年複利', u'半年複利', u'連続複利'],
           loc='upper left', frameon=False, prop=jpfont)
plt.xlabel(u'時点 t', fontproperties=jpfont)
plt.ylabel(u'総収益 W(t)/W(0)', fontproperties=jpfont)
plt.show()
