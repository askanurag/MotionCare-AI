from sklearn.model_selection import GroupKFold, cross_val_score
from .pipeline import build
from .settings import FEATURES,TARGET
def cross_validate_train(frame,name='logistic',folds=3,seed=42):
    return cross_val_score(build(name,seed),frame[FEATURES],frame[TARGET],groups=frame.patient_id,
        cv=GroupKFold(n_splits=folds),scoring='roc_auc',n_jobs=1).tolist()
