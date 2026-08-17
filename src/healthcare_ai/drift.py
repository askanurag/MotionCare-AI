import numpy as np
def standardized_shift(reference,current):
    result={}
    for col in reference.columns:
        scale=float(reference[col].std())
        result[col]=float(abs(reference[col].mean()-current[col].mean())/max(scale,1e-8))
    return result
