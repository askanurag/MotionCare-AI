"""Bounded incremental window buffer; no filtering or alarm decisions."""
import numpy as np
from .signal_contracts import validate_signal
class WindowBuffer:
    def __init__(self,fs=50,seconds=4,stride=2):
        if min(fs,seconds,stride)<=0:raise ValueError('Positive dimensions required')
        self.fs=fs;self.size=round(fs*seconds);self.step=round(fs*stride)
        if self.size<3 or not 1<=self.step<=self.size:raise ValueError('Require 1 <= step <= window size')
        self.data=np.empty((0,6))
    def push(self,chunk):
        x=np.asarray(chunk,dtype=float)
        if x.ndim!=2 or x.shape[1]!=6 or not np.isfinite(x).all():raise ValueError('Finite six-channel chunk required')
        self.data=np.vstack([self.data,x]);out=[]
        while len(self.data)>=self.size:
            out.append(self.data[:self.size].copy());self.data=self.data[self.step:]
        return out
