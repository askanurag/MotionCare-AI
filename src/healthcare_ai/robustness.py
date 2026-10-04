import numpy as np
def missingness_stress(model,x,rates=(0,.1,.3),seed=42):
    rng=np.random.default_rng(seed); result={}
    for rate in rates:
        altered=x.copy(); mask=rng.random(altered.shape)<rate; altered=altered.mask(mask)
        result[str(rate)]=model.predict_proba(altered)[:,1]
    return result
