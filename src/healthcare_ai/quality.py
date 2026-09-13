from .settings import FEATURES, TARGET
def quality_report(frame):
    result={'rows':len(frame),'patients':int(frame.patient_id.nunique()),'duplicate_patient_rows':int(frame.patient_id.duplicated().sum()),
    'missing_fraction':{c:float(frame[c].isna().mean()) for c in FEATURES}}
    if TARGET in frame: result['positive_fraction']=float(frame[TARGET].mean())
    return result
