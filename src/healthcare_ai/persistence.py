import joblib
from pathlib import Path
def save_bundle(path,model,threshold,metadata):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    joblib.dump({'model':model,'threshold':threshold,'metadata':metadata},p)
def load_bundle(path):
    # Only load files produced locally or obtained from a trusted source.
    return joblib.load(path)
