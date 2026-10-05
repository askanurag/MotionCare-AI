"""Deterministic fixed-length windows; trailing partial windows are omitted."""
import numpy as np
from .signal_contracts import validate_signal
def window_indices(n,fs,seconds=4,stride=2):
    if not np.isfinite([fs,seconds,stride]).all() or min(fs,seconds,stride)<=0:raise ValueError('Positive finite dimensions required')
    size,step=round(seconds*fs),round(stride*fs)
    if size<3 or step<1:raise ValueError('Window or stride too short')
    return [(start,start+size) for start in range(0,n-size+1,step)]
def windows(values,fs,seconds=4,stride=2):
    x=validate_signal(values,fs)
    return [(a,b,x[a:b].copy()) for a,b in window_indices(len(x),fs,seconds,stride)]
