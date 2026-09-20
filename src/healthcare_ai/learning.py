from sklearn.model_selection import learning_curve, GroupKFold
from .pipeline import build
from .settings import FEATURES,TARGET
def learning_profile(frame,seed=42):
    sizes,tr,va=learning_curve(build(seed=seed),frame[FEATURES],frame[TARGET],groups=frame.patient_id,
      cv=GroupKFold(n_splits=3),train_sizes=[.3,.6,1.],scoring='roc_auc',shuffle=True,random_state=seed)
    return {'sizes':sizes.tolist(),'train_auc':tr.mean(axis=1).tolist(),'validation_auc':va.mean(axis=1).tolist()}
