# -*- coding: utf-8 -*-
#    NumPyの読み込み
import numpy as np
#    SciPyのstatsモジュールの読み込み
import scipy.stats as st
#    Pandasの読み込み
import pandas as pd
# %% 多変量正規分布からの乱数生成と保存
Mu = np.array([1.0, 3.0, 1.5, 6.0, 4.5])
Stdev = np.array([5.0, 10.0, 7.5, 15.0, 11.0])
CorrMatrix = np.array([[1.00, 0.25, 0.18, 0.10, 0.25],
                       [0.25, 1.00, 0.36, 0.20, 0.20],
                       [0.18, 0.36, 1.00, 0.25, 0.36],
                       [0.10, 0.20, 0.25, 1.00, 0.45],
                       [0.25, 0.20, 0.36, 0.45, 1.00]])
Sigma = np.diag(Stdev).dot(CorrMatrix).dot(np.diag(Stdev))
np.random.seed(9999)
T = 120
End_of_Month = pd.date_range('1/1/2007', periods=T, freq='M')
Asset_Names = [u'資産1', u'資産2', u'資産3', u'資産4', u'資産5']
Asset_Return = pd.DataFrame(st.multivariate_normal(Mu, Sigma).rvs(T),
                            index=End_of_Month, columns=Asset_Names)
Asset_Return.to_csv('asset_return_data.csv')
