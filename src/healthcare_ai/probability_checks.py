"""Reject invalid or misaligned binary class probabilities."""
import numpy as np
def check_probabilities(probability,n=None):
    p=np.asarray(probability,dtype=float)
    if p.ndim!=1 or len(p)==0 or not np.isfinite(p).all():raise ValueError('Finite nonempty vector required')
    if ((p<0)|(p>1)).any():raise ValueError('Probabilities outside [0,1]')
    if n is not None and len(p)!=n:raise ValueError('Probability length mismatch')
    return p
