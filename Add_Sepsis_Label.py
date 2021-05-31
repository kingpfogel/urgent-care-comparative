import pandas as pd
import pickle

path_save = "./local_mimic/save/"

with open(path_save + 'labels_ohne_sepsis', 'rb') as f:
    labels = pickle.load(f)

df = pd.read_csv("./local_mimic/sepsis_onset_hadm_id.csv", quotechar='"', sep=',')

for key, value in labels.items():
    bla = df.loc[df["hadm_id"] == value["hadm_id"]].sepsis_onset_betaversion.tolist()[0]
    value["sepsis_v1"] = bla

with open(path_save + 'labels', 'wb') as f:
    pickle.dump(labels, f)

