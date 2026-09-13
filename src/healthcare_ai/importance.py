from sklearn.inspection import permutation_importance
from .settings import FEATURES
def feature_importance(model,x,y,seed=42):
    result=permutation_importance(model,x,y,scoring='roc_auc',n_repeats=5,random_state=seed,n_jobs=1)
    return sorted([{'feature':f,'mean':float(m),'std':float(s)} for f,m,s in zip(FEATURES,result.importances_mean,result.importances_std)],key=lambda r:-r['mean'])
