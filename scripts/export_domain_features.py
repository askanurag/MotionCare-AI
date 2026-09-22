from healthcare_ai.paths import ROOT
from healthcare_ai.domain_experiment import load_default_cohort
out=ROOT/'outputs';out.mkdir(exist_ok=True);frame=load_default_cohort();frame.to_csv(out/'domain_features.csv',index=False)
print('Exported',len(frame),'domain feature rows')
