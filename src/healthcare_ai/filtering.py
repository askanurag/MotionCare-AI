"""Zero-phase low-pass filtering; intended for offline analysis only."""
from scipy.signal import butter,sosfiltfilt
from .signal_contracts import validate_signal
def lowpass(values,fs,cutoff=10,order=4):
    x=validate_signal(values,fs)
    if not 0<cutoff<fs/2:raise ValueError('Cutoff must lie below Nyquist')
    if order<1:raise ValueError('Order must be positive')
    sos=butter(order,cutoff,fs=fs,output='sos')
    if len(x)<=3*(2*len(sos)+1):raise ValueError('Signal too short for zero-phase padding')
    return sosfiltfilt(sos,x,axis=0)
