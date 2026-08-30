import platform
import sklearn
import numpy as np
import hashlib
def provenance(frame,seed):
    digest=hashlib.sha256(frame.to_csv(index=False).encode()).hexdigest()
    return {'data_sha256':digest,'seed':seed,'python':platform.python_version(),'sklearn':sklearn.__version__,
      'numpy':np.__version__,'data_origin':'synthetic','clinical_validation':False}
