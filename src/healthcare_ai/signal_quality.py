"""Descriptive signal checks; no medically validated quality thresholds."""
import numpy as np
from .signal_contracts import validate_signal
def signal_quality(values,fs,clip_limit=5.):
    x=validate_signal(values,fs)
    if clip_limit<=0:raise ValueError('Positive clipping threshold required')
    return {'samples':len(x),'duration_seconds':len(x)/fs,
      'flat_channels':int(np.sum(x.std(axis=0)<1e-8)),
      'clipped_fraction':float((abs(x)>=clip_limit).mean()),
      'max_sample_jump':float(abs(np.diff(x,axis=0)).max())}
