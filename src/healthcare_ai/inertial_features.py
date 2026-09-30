"""Time-domain feature definitions in arbitrary simulator units."""
import numpy as np
from .signal_contracts import validate_signal
def inertial_summary(values,fs):
    x=validate_signal(values,fs);a=x[:,:3];g=x[:,3:];mag=np.linalg.norm(a,axis=1);jerk=np.diff(a,axis=0)*fs
    return {'accel_rms':float(np.sqrt(np.mean(mag**2))),'accel_variance':float(mag.var()),
      'jerk_rms':float(np.sqrt(np.mean(np.sum(jerk**2,axis=1)))),'gyro_rms':float(np.sqrt(np.mean(np.sum(g**2,axis=1))))}
