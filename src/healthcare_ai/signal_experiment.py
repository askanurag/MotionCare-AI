"""Patient-separated training from actual simulated IMU feature windows."""
from pathlib import Path
import json
import pandas as pd
from .session_io import load_session
from .window_features import featurize_session
from .experiment import run
from .splits import split
from .pipeline import build
from .settings import FEATURES,TARGET
from .metrics import evaluate
from .augmentation import jitter
from .signal_contracts import CHANNELS
def load_feature_sessions(paths,seconds=4,stride=2,noise_sigma=0.,seed=42):
    tables=[]
    for i,path in enumerate(paths):
        frame,fs=load_session(path)
        if noise_sigma:frame.loc[:,CHANNELS]=jitter(frame[CHANNELS],fs,noise_sigma,seed+i)
        tables.append(featurize_session(frame,fs,seconds,stride))
    if not tables:raise ValueError('At least one session file required')
    result=pd.concat(tables,ignore_index=True)
    if len(result)==0:raise ValueError('No complete windows')
    return result
def run_signal_project(paths,seconds=4,stride=2,output=None):
    frame=load_feature_sessions(paths,seconds,stride);bundle,report=run(frame,output=output)
    report['signal_protocol']={'window_seconds':seconds,'stride_seconds':stride,'patients':int(frame.patient_id.nunique()),'unit':'window','origin':'simulated raw IMU recordings'}
    if output:
        from .io import write_json
        write_json(Path(output)/'metrics.json',report)
    return bundle,report
def scenario_validation(paths,config):
    frame=load_feature_sessions(paths,config['window_seconds'],config['stride_seconds'],config['noise_sigma'])
    train,val,_=split(frame);model=build().fit(train[FEATURES],train[TARGET])
    return evaluate(val[TARGET],model.predict_proba(val[FEATURES])[:,1])
