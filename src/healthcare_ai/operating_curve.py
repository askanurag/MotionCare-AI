"""Validation threshold tradeoffs; no clinical cost assumption."""
import numpy as np
import pandas as pd
from .metrics import evaluate
def operating_curve(y,p,thresholds=None):
    grid=np.linspace(.1,.9,9) if thresholds is None else thresholds
    rows=[]
    for t in grid:
        if not 0<=t<=1:raise ValueError('Threshold outside [0,1]')
        r=evaluate(y,np.asarray(p),t);r['positive_rate']=float((np.asarray(p)>=t).mean());rows.append(r)
    return pd.DataFrame(rows)
