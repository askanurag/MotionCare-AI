"""Validation for six-channel simulated IMU recordings."""
import numpy as np
CHANNELS=['ax','ay','az','gx','gy','gz']
def validate_signal(values,fs):
    x=np.asarray(values,dtype=float)
    if not np.isfinite(fs) or fs<=0:raise ValueError('Positive finite sampling frequency required')
    if x.ndim!=2 or x.shape[1]!=6 or len(x)<3:raise ValueError('Expected at least 3 rows and 6 channels')
    if not np.isfinite(x).all():raise ValueError('Signal must contain finite measurements')
    return x
