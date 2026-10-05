import numpy as np
import pandas as pd
from .settings import SPEC, FEATURES, TARGET
def generate(n=600, seed=42):
    if n < 30: raise ValueError('Use at least 30 patients')
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(n, len(FEATURES)))
    x = np.asarray(SPEC['means']) + z * np.asarray(SPEC['scales'])
    frame = pd.DataFrame(x, columns=FEATURES)
    score = z @ np.asarray(SPEC['weights']) + rng.normal(0, .8, n)
    probability = 1 / (1 + np.exp(-np.clip(score, -30, 30)))
    frame[TARGET] = rng.binomial(1, probability)
    frame.insert(0, 'patient_id', ['SYN-%06d' % i for i in range(n)])
    return frame
