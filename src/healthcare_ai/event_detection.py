"""Threshold heuristic used as a comparator, not a medical alarm."""
import numpy as np
from .signal_contracts import validate_signal
def magnitude_peaks(values,fs,threshold=2.,refractory=.5):
    from scipy.signal import find_peaks
    x=validate_signal(values,fs)
    if refractory<=0:raise ValueError('Positive refractory period required')
    magnitude=np.linalg.norm(x[:,:3],axis=1)
    indices,_=find_peaks(magnitude,height=threshold,distance=max(1,round(refractory*fs)))
    return indices.tolist()
