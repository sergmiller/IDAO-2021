import numpy as np
import torch
from mobilenet_v3 import mobilenet_v3_small

import os
<<<<<<< HEAD
print(len(os.listdir('tests/public_test')))
print('example files', os.listdir('tests/public_test')[0:2])
from utils import file, dataset
PATH_TO_TEST_DIRS = os.path.abspath('./tests')
# d1 = file.read_all_png_in_dir(PATH_TO_TEST_DIRS, limit=10)
# print(len(d1))
# print(d1[0])
=======
print('Is your solution okie on private test?')
# from utils import file, dataset
# PATH_TO_TEST_DIRS = os.path.abspath('./tests')
# d1 = file.read_all_png_in_test_dir(PATH_TO_TEST_DIRS)
# print('len d1', len(d1))
>>>>>>> a6d9e623f0b6c58a32fc1bc80886e3634aa18dd3
# mobilenet = mobilenet_v3_small()
# mobilenet.load_state_dict(torch.load("mobilenet_state_dict"))
#
# np.random.seed(0)
# t = np.random.random((4,3,32,32))
# mobilenet.train(False)
# print(np.mean(t), np.std(t))
# with torch.no_grad():
#     res = mobilenet(torch.Tensor(t)).detach().numpy()
# print(np.mean(res), np.std(res))
