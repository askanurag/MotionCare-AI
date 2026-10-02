import numpy as np
from .settings import FEATURES, TARGET
def validate(frame, labeled=True):
    required = ['patient_id'] + FEATURES + ([TARGET] if labeled else [])
    missing = set(required) - set(frame.columns)
    if missing: raise ValueError('Missing columns: ' + str(sorted(missing)))
    if frame.patient_id.isna().any(): raise ValueError('Missing patient identifiers')
    if not all(np.issubdtype(frame[c].dtype, np.number) for c in FEATURES): raise ValueError('Features must be numeric')
    if np.isinf(frame[FEATURES].to_numpy()).any(): raise ValueError('Infinite values are unsupported')
    if frame[FEATURES].isna().all().any(): raise ValueError('Entirely missing feature')
    if labeled and not set(frame[TARGET].unique()) <= {0, 1}: raise ValueError('Binary target required')
    return frame
