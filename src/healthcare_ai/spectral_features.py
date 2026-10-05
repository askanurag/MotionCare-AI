"""Spectrum summaries from the acceleration magnitude."""
import numpy as np
from .signal_contracts import validate_signal
def spectrum(values,fs):
    x=validate_signal(values,fs);m=np.linalg.norm(x[:,:3],axis=1);m-=m.mean()
    power=abs(np.fft.rfft(m*np.hanning(len(m))))**2
    return np.fft.rfftfreq(len(m),1/fs),power
def spectral_summary(values,fs):
    f,p=spectrum(values,fs);total=p.sum()
    if total<1e-12:return {'dominant_frequency':0.,'spectral_entropy':0.,'spectral_centroid':0.}
    w=p/total;return {'dominant_frequency':float(f[np.argmax(p)]),'spectral_entropy':float(-np.sum(w*np.log(w+1e-12))),
    'spectral_centroid':float(np.sum(f*w))}
