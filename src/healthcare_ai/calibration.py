import numpy as np
from sklearn.calibration import calibration_curve
def reliability(y, p, bins=8):
    observed, predicted = calibration_curve(y,p,n_bins=bins,strategy='quantile')
    return {'predicted': predicted.tolist(), 'observed': observed.tolist()}
def expected_calibration_error(y,p,bins=10):
    y,p=np.asarray(y),np.asarray(p); total=0.
    for i in range(bins):
        mask=(p >= i/bins) & ((p <= 1) if i==bins-1 else (p < (i+1)/bins))
        if mask.any(): total += mask.mean()*abs(y[mask].mean()-p[mask].mean())
    return float(total)
