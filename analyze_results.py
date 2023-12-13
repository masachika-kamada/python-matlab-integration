import scipy.io
import numpy as np

# 結果を読み込み
results_mat = scipy.io.loadmat('results.mat')
results = results_mat['results']
print(results[0, 0].dtype)
print(results[0, 0].dtype.names)
print(results[0, 0]["C"].shape)

C = np.array([results[0, i]['C'] for i in range(102)])
C_diag = np.array([np.diag(C[i]) for i in range(102)])
S = np.array([results[0, i]['S'] for i in range(102)])
S_diag = np.array([np.diag(S[i]) for i in range(102)])
X = np.array([results[0, i]['X'] for i in range(102)])
print(C_diag.shape)
print(S_diag.shape)
print(X.shape)