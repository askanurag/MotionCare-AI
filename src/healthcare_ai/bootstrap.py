import numpy as np
from sklearn.metrics import roc_auc_score
def auc_interval(y,p,repetitions=200,seed=42):
    y,p=np.asarray(y),np.asarray(p); rng=np.random.default_rng(seed); scores=[]
    for _ in range(repetitions):
        ix=rng.integers(0,len(y),len(y))
        if len(np.unique(y[ix])) == 2: scores.append(roc_auc_score(y[ix],p[ix]))
    if not scores: return {'lower':None,'upper':None,'valid_repetitions':0}
    low,high=np.quantile(scores,[.025,.975])
    return {'lower':float(low),'upper':float(high),'valid_repetitions':len(scores)}
