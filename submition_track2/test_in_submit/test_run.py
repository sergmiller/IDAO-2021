import numpy as np
import torch


import time
start = time.time()
for i in np.arange(100):
    t = np.random.random((32,3,500,500))
    with torch.no_grad():
        res = mobilenet(torch.Tensor(t)).detach().numpy()

import pandas as pd
import sys
sys.appned('../..')
from utilz import file, dataset
PATH_TO_TEST_DIRS = 'tests/'
d1 = file.read_all_png_in_dir(PATH_TO_TEST_DIRS)
res = []
for key in dataset._fix_tags(read_all_png_in_dir(path).keys()):
    res.append([key, 0, 0])
data_frame = pd.DataFrame(res, columns=["id", "classification_predictions", "regression_predictions"])
data_frame.to_csv('submission.csv', index=False, header=True)
