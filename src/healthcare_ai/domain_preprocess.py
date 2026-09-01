import numpy as np
from scipy.signal import medfilt
def clean_signal(x,fs=None,cutoff=5):
    x=np.asarray(x,dtype=float);kernel=int(cutoff)
    if x.ndim!=1 or not np.isfinite(x).all() or kernel<1 or kernel%2==0 or kernel>len(x):raise ValueError('Finite vector and odd kernel required')
    return medfilt(x,kernel_size=kernel)
