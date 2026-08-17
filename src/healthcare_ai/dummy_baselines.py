"""Compare class-prior and majority-class baselines fitted on training only."""
from sklearn.dummy import DummyClassifier
from .settings import FEATURES,TARGET
from .metrics import evaluate
def dummy_scores(train,validation):
    result={}
    for strategy in ['prior','most_frequent']:
        m=DummyClassifier(strategy=strategy).fit(train[FEATURES],train[TARGET])
        if len(m.classes_)!=2:raise ValueError('Two training classes required')
        result[strategy]=evaluate(validation[TARGET],m.predict_proba(validation[FEATURES])[:,1])
    return result
