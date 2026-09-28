"""Convert point-event timestamps to labels for half-open windows."""
import numpy as np
def label_window(start,end,event_times):
    if not np.isfinite([start,end]).all() or end<=start:raise ValueError('Invalid interval')
    events=np.asarray(event_times,dtype=float)
    if not np.isfinite(events).all():raise ValueError('Finite event times required')
    return int(((events>=start)&(events<end)).any())
