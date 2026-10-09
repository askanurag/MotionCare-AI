"""Scenario comparisons use validation only; no holdout model selection."""
from .domain_experiment import load_default_cohort
from .splits import split
from .pipeline import build
from .metrics import evaluate
from .settings import FEATURES,TARGET
def validation_scenario(config):
    if config['window_size']<=0 or config['stride_size']<=0 or config['noise_sigma']<0:raise ValueError('Invalid scenario')
    frame=load_default_cohort(config['window_size'],config['stride_size'],config['noise_sigma'])
    train,validation,_=split(frame)
    model=build().fit(train[FEATURES],train[TARGET])
    return evaluate(validation[TARGET],model.predict_proba(validation[FEATURES])[:,1])
