import pandas as pd
from .domain_contract import validate_recording
from .domain_windows import segments
from .domain_features import segment_features
from .domain_labels import segment_label
from .settings import FEATURES,TARGET
def cohort_from_paths(paths,window_size=6,stride_size=6,noise_sigma=0.,seed=42):
    # Glucose window and stride units are hours.
    import numpy as np
    from .domain_loader import load_recording
    rng=np.random.default_rng(seed);rows=[]
    if noise_sigma<0:raise ValueError('Nonnegative noise required')
    for path in paths:
        f=load_recording(path);fs=validate_recording(f)
        if noise_sigma:f.glucose_reading+=rng.normal(0,noise_sigma,len(f))
        for part in segments(f,window_size,stride_size):rows.append({'patient_id':f.patient_id.iloc[0],**segment_features(part,fs),TARGET:segment_label(part)})
    if not rows:raise ValueError('No complete traces/windows')
    return pd.DataFrame(rows,columns=['patient_id']+FEATURES+[TARGET])
