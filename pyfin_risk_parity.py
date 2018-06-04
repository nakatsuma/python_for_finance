# -*- coding: utf-8 -*-
#   NumPyの読み込み
import numpy as np
#   NumPyのLinalgモジュールの読み込み
import numpy.linalg as lin
#   SciPyのoptimizeモジュールの読み込み
import scipy.optimize as opt
#%% リスク寄与度の平準化によるポートフォリオ選択
Mu = np.array([1.0, 3.0, 1.5, 6.0, 4.5])
Stdev = np.array([5.0, 10.0, 7.5, 15.0, 11.0])
CorrMatrix = np.array([[1.00, 0.25, 0.18, 0.10, 0.25],
                       [0.25, 1.00, 0.36, 0.20, 0.20],
                       [0.18, 0.36, 1.00, 0.25, 0.36],
                       [0.10, 0.20, 0.25, 1.00, 0.45],
                       [0.25, 0.20, 0.36, 0.45, 1.00]])
Sigma = np.diag(Stdev).dot(CorrMatrix).dot(np.diag(Stdev))
iota = np.ones(Mu.shape)
inv_Sigma = lin.inv(Sigma)
Weight_1N = np.tile(1.0/Mu.shape[0], Mu.shape[0])
Weight_MV = inv_Sigma.dot(iota) / iota.dot(inv_Sigma).dot(iota)
Weight_MD = inv_Sigma.dot(Stdev) / iota.dot(inv_Sigma).dot(Stdev)
F = lambda v, Sigma: np.r_[Sigma.dot(v[:-1])-v[-1]/v[:-1], v[:-1].sum()-1.0]
Weight_RP = opt.root(F, np.r_[Weight_1N, 0.0], args=Sigma).x[:-1]
np.set_printoptions(formatter={'float': '{:7.2f}'.format})
print(np.c_[Weight_1N, Weight_MV, Weight_RP, Weight_MD]*100)
