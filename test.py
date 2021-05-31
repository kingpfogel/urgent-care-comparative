import pandas as pd
import pickle
import numpy as np

path_save = "./local_mimic/save/"

with open(path_save + 'labels_ohne_sepsis', 'rb') as f:
    labels = pickle.load(f)

with open(path_save + 'labels', 'rb') as f:
    labels2 = pickle.load(f)

print(labels)
print(labels2)
print(len(labels))


#with open(path_save + "y", "rb") as f:
#    y = pickle.load(f)
#print(y)
#print(len(y))

res = []
for key, value in labels2.items():
    bla = value["sepsis_v1"]
    res.append(bla)
print(res)