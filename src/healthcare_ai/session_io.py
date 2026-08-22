"""Synthetic six-axis session generation and CSV loading."""
import numpy as np
import pandas as pd
from .signal_contracts import CHANNELS,validate_signal
def make_session(seed=42,fs=50,seconds=24):
    if fs<=0 or seconds<8:raise ValueError('Use positive fs and at least 8 seconds')
    rng=np.random.default_rng(seed);t=np.arange(round(fs*seconds))/fs;phase=rng.uniform(0,6.28)
    a=np.column_stack([.35*np.sin(2*np.pi*1.3*t+phase),.2*np.cos(2*np.pi*1.3*t),np.ones(len(t))])
    g=np.column_stack([.1*np.sin(t),.12*np.cos(t),.05*np.sin(2*t)])
    events=[seconds*.29,seconds*.71]
    for event in events:
        pulse=np.exp(-.5*((t-event)/.07)**2)
        a+=pulse[:,None]*np.array([2.8,1.8,1.2]);g+=pulse[:,None]*np.array([1.2,.5,.8])
    x=np.column_stack([a,g])+rng.normal(0,.025,(len(t),6));df=pd.DataFrame(x,columns=CHANNELS)
    df.insert(0,'seconds',t);df['patient_id']='SIM-WEAR-%03d'%seed
    df['event_marker']=0
    for e in events:df.loc[int(np.argmin(abs(t-e))),'event_marker']=1
    return df
def load_session(path):
    frame=pd.read_csv(path);required=['seconds','patient_id','event_marker']+CHANNELS
    if not set(required)<=set(frame):raise ValueError('Missing session columns')
    if len(frame.patient_id.unique())!=1:raise ValueError('One patient per recording required')
    t=frame.seconds.to_numpy(dtype=float)
    if len(t)<3 or not np.isfinite(t).all() or not (np.diff(t)>0).all():raise ValueError('Strictly increasing finite timestamps required')
    delta=np.diff(t);fs=1/float(np.median(delta))
    if not np.allclose(delta,1/fs,rtol=.01,atol=1e-8):raise ValueError('Uniform timestamps required')
    validate_signal(frame[CHANNELS],fs)
    if frame.patient_id.isna().any() or not set(frame.event_marker.unique())<={0,1}:raise ValueError('Invalid identity or event marker')
    return frame,fs
