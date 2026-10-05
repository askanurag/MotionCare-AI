"""Connect raw six-axis recordings to the tabular model feature contract."""
import pandas as pd
from .signal_contracts import CHANNELS,validate_signal
from .windowing import windows
from .inertial_features import inertial_summary
from .spectral_features import spectral_summary
from .orientation import direction_change
from .event_labels import label_window
from .settings import FEATURES,TARGET
def extract_window(values,fs):
    x=validate_signal(values,fs);result=inertial_summary(x,fs)
    result['dominant_frequency']=spectral_summary(x,fs)['dominant_frequency']
    result['orientation_change']=direction_change(x,fs)
    return {f:result[f] for f in FEATURES}
def featurize_session(frame,fs,seconds=4,stride=2):
    if frame.patient_id.nunique()!=1:raise ValueError('Each session must have one patient')
    x=frame[CHANNELS].to_numpy();t=frame.seconds.to_numpy();events=frame.loc[frame.event_marker==1,'seconds'].to_numpy();rows=[]
    for a,b,window in windows(x,fs,seconds,stride):
        row={'patient_id':str(frame.patient_id.iloc[0]),**extract_window(window,fs),TARGET:label_window(t[a],t[a]+(b-a)/fs,events)}
        rows.append(row)
    return pd.DataFrame(rows,columns=['patient_id']+FEATURES+[TARGET])
