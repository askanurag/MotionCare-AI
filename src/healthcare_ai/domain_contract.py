import numpy as np
COLUMNS=['patient_id','hours','glucose_reading','activity','age','bmi','family_history','sleep_hours','latent_state']
def validate_recording(frame):
    if not set(COLUMNS)<=set(frame):raise ValueError('Missing glucose trace columns')
    if frame.patient_id.isna().any() or frame.patient_id.nunique()!=1:raise ValueError('One patient per trace required')
    t=frame.hours.to_numpy(dtype=float)
    if len(t)<12 or not np.isfinite(frame[COLUMNS[1:]].to_numpy(dtype=float)).all() or not (np.diff(t)>0).all():raise ValueError('Finite increasing trace required')
    dt=np.diff(t)
    if not np.allclose(dt,np.median(dt),rtol=.01):raise ValueError('Uniform trace sampling required')
    if not set(frame.latent_state.unique())<={0,1}:raise ValueError('Binary simulator states required')
    return 1/float(np.median(dt))
