"""Explicit distinction between simulator experiments and clinical validation."""
from datetime import datetime,timezone
from .settings import FEATURES,TARGET
def describe_model(task,patients):
    if patients<1:raise ValueError('Positive patient count required')
    return {'task':task,'features':FEATURES,'target':TARGET,'patients':int(patients),
      'data_origin':'synthetic','clinical_validation':False,'created_utc':datetime.now(timezone.utc).isoformat(),
      'limitations':['no real-patient evaluation','no external site evaluation','no clinical operating threshold']}
