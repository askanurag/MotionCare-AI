"""Polyphase offline resampling with anti-aliasing."""
from fractions import Fraction
import numpy as np
from scipy.signal import resample_poly
from .signal_contracts import validate_signal
def resample(values,fs,target_fs):
    x=validate_signal(values,fs)
    if not np.isfinite(target_fs) or target_fs<=0:raise ValueError('Positive finite target frequency required')
    ratio=Fraction(float(target_fs)/float(fs)).limit_denominator(10000)
    return resample_poly(x,ratio.numerator,ratio.denominator,axis=0)
