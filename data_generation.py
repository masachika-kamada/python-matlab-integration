import numpy as np
import scipy.io

data1 = np.random.rand(102, 8, 8)
data2 = np.random.rand(102, 8, 8)

# .matファイルに保存
scipy.io.savemat("data.mat", {"data1": data1, "data2": data2})
