"""Train-only measurement perturbations; preserve shape and determinism."""
import numpy as np
from .signal_contracts import validate_signal
def jitter(values,fs,sigma=.05,seed=42):
    x=validate_signal(values,fs)
    if sigma<0 or not np.isfinite(sigma):raise ValueError('Nonnegative finite noise required')
    return x+np.random.default_rng(seed).normal(0,sigma,x.shape)
def rotate_z(values,fs,angle):
    x=validate_signal(values,fs).copy();c,s=np.cos(angle),np.sin(angle)
    rotation=np.array([[c,-s,0],[s,c,0],[0,0,1]])
    x[:,:3]=x[:,:3]@rotation.T;x[:,3:]=x[:,3:]@rotation.T
    return x
