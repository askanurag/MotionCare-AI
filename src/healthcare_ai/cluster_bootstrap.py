"""Percentile AUROC interval resampling complete patient clusters."""
import numpy as np
from sklearn.metrics import roc_auc_score
def cluster_auc(y,p,patient_ids,repetitions=100,seed=42):
    y,p,groups=np.asarray(y),np.asarray(p),np.asarray(patient_ids)
    if len(y)!=len(p) or len(y)!=len(groups) or len(y)==0:raise ValueError('Aligned nonempty arrays required')
    unique=np.unique(groups);rng=np.random.default_rng(seed);scores=[]
    for _ in range(repetitions):
        sample=rng.choice(unique,len(unique),replace=True)
        ix=np.concatenate([np.flatnonzero(groups==g) for g in sample])
        if len(np.unique(y[ix]))==2:scores.append(roc_auc_score(y[ix],p[ix]))
    if not scores:return {'lower':None,'upper':None,'valid_repetitions':0,'patients':len(unique)}
    lower,upper=np.quantile(scores,[.025,.975]);return {'lower':float(lower),'upper':float(upper),'valid_repetitions':len(scores),'patients':len(unique)}
