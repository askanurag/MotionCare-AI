"""Gravity-direction proxy; not a calibrated orientation estimator."""
import numpy as np
from .signal_contracts import validate_signal
def direction_change(values,fs):
    x=validate_signal(values,fs);a=x[:,:3];n=max(1,len(a)//4)
    first,last=a[:n].mean(axis=0),a[-n:].mean(axis=0);den=np.linalg.norm(first)*np.linalg.norm(last)
    if den<1e-12:return 0.
    return float(np.arccos(np.clip(first@last/den,-1,1)))
