import numpy as np
import pandas as pd
import os
import tqdm
import torch

from itertools import chain

import matplotlib.pyplot as plt


from .dataset import LabeledDataset
from .applier import build_embd_dataset

def apply_all_models_to_test_dataset_gen(
    dataset_gen,
    backbone,
    model1,
    model2
) -> LabeledDataset:

    labels = []
    tags = []
    for batch in dataset_gen:
        emb_batch_dataset = build_embd_dataset(batch, backbone, batch_size=len(batch.samples), n_jobs=1)
        labels1 = model1.predict_proba(emb_batch_dataset.samples)[:, 0]
        labels2 = model2.predict(emb_batch_dataset.samples)
        labels_batch = [[l1,l2] for l1, l2 in zip(labels1, labels2)]
        labels.extend(labels_batch)
        tags.extend(emb_batch_dataset.tags)

    labels = np.array(labels)

    emb_dataset = LabeledDataset()
    emb_dataset.tags = tags
    emb_dataset.labels = labels

    return emb_dataset


def apply_all_models_to_test_dataset(
    d : LabeledDataset,
    backbone,
    model1,
    model2,
    key : str,
    _emb_cache={}
) -> LabeledDataset:
    if key not in _emb_cache:
        _emb_cache[key] = build_embd_dataset(d, backbone)
    emb_dataset = _emb_cache.get(key)

    labels1 = model1.predict_proba(emb_dataset.samples)[:, 0]
    labels2 = model2.predict(emb_dataset.samples)

    labels = np.stack([labels1, labels2]).T

    emb_dataset.labels = labels

    return emb_dataset
