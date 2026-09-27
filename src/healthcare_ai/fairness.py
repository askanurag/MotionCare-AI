from .metrics import evaluate
def subgroup_metrics(y,p,groups,threshold=.5):
    import numpy as np
    y,p,groups=map(np.asarray,(y,p,groups))
    return {str(g):evaluate(y[groups==g],p[groups==g],threshold) for g in np.unique(groups)}
