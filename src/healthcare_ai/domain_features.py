from .settings import FEATURES
def segment_features(segment,fs=None):
    r={'age':float(segment.age.iloc[0]),'bmi':float(segment.bmi.iloc[0]),'glucose':float(segment.glucose_reading.mean()),
       'activity_minutes':float(segment.activity.mean()),'family_history':float(segment.family_history.iloc[0]),'sleep_hours':float(segment.sleep_hours.iloc[0])}
    return {f:r[f] for f in FEATURES}
