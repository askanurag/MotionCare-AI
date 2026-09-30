import pandas as pd
from .settings import FEATURES
from .validation import validate
def predict(bundle,frame):
    validate(frame,labeled=False)
    p=bundle['model'].predict_proba(frame[FEATURES])[:,1]
    return pd.DataFrame({'patient_id':frame.patient_id.to_numpy(),'probability':p,'predicted_class':(p>=bundle['threshold']).astype(int)})
