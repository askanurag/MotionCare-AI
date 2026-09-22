from healthcare_ai.paths import ROOT
from healthcare_ai.signal_experiment import load_feature_sessions
out=ROOT/'outputs';out.mkdir(exist_ok=True)
f=load_feature_sessions(sorted((ROOT/'data').glob('imu_session_*.csv')));f.to_csv(out/'signal_features.csv',index=False)
print('Exported',len(f),'labeled signal windows')
