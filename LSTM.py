from deep_models import *
import numpy as np
import pickle
from sklearn.model_selection import *
import os
import utilities


X = np.load("local_mimic/save/X19.npy", allow_pickle=True)
input_shape = X.shape

with open(".\\local_mimic\\save\\labels", "rb") as f:
    labels = pickle.load(f)
res = []
for key, value in labels.items():
    bla = value["sepsis_v1"]
    res.append(bla)

ref_target = res
y = res

skf = StratifiedKFold(n_splits=5)

model = lstm_model(input_shape=input_shape, targets=1, hidden=256,
                   multiclass=False, learn_rate=0.005)


for train_index, test_index in skf.split(X, ref_target):
    X_tr, X_te = X[train_index], X[test_index]
    y_tr, y_te = y[train_index], y[test_index]

    if len(X_tr.shape) > 2:
        input_shape = (X_tr.shape[1], X_tr.shape[-1])
    else:
        input_shape = (X_tr.shape[-1],)

    xs, ys = utilities.balanced_subsample(X_tr, y_tr, 1.0)
    ys = np.array([[i] for i in ys])

    model.fit(x=xs, y=ys, batch_size=128,
              validation_split=.2, epochs=1, verbose=2)