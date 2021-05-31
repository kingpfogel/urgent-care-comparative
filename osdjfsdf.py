import pickle

from pathlib import Path

root = Path("../../Downloads/FürNiklas/urgent-care-comparative-master")
print(root)
my_path = root / "local_mimic"
print(my_path)
with open(my_path, "wb") as f:
    pickle.dump("1234", f)
