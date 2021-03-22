import numpy as np
import pandas as pd
import os
import tqdm
import torch

from itertools import chain

import matplotlib.pyplot as plt


def read_all_png_in_dir(base_path : str, limit : int = None) -> dict:
    from os import listdir
    from os.path import isfile, join
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import tqdm

    imgs = [os.path.join(dir,f) for (dir, subdirs, fs) in os.walk(base_path) for f in fs]
    imgs = filter(lambda f: isfile(f) and '.png' == f[-4:], imgs)
    imgs = list(imgs)
    if limit is not None:
        imgs = imgs[:limit]
    data = {img : mpimg.imread(img) for img in imgs}
    return data
