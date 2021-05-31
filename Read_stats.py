import pandas as pd
import pickle
import numpy as np

path_save = "./local_mimic/save/checkpoint/svm-sepsis_v1-x48-w2v/"

with open(path_save + 'best_model', 'rb') as f:
    model = pickle.load(f)

with open(path_save + '/scores/raw_stats', 'rb') as f:
    stats = pickle.load(f)

print(model)
print(stats)