"""Fit separate pipelines after removing one input feature."""
from .settings import FEATURES,TARGET
from .pipeline import build
from .metrics import evaluate
def ablate(train,validation,seed=42):
    results=[]
    for omitted in FEATURES:
        cols=[c for c in FEATURES if c!=omitted];m=build(seed=seed).fit(train[cols],train[TARGET])
        results.append({'omitted':omitted,**evaluate(validation[TARGET],m.predict_proba(validation[cols])[:,1])})
    return results
