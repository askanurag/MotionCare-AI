from healthcare_ai.paths import ROOT
from healthcare_ai.domain_simulation import make_recording
for seed in range(1,11):make_recording(seed).to_csv(ROOT/f'data/domain_record_{seed:03d}.csv',index=False)
print('Generated ten synthetic domain recordings/cohorts')
