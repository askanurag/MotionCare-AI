import json
from healthcare_ai.paths import ROOT
from healthcare_ai.signal_experiment import scenario_validation
from healthcare_ai.io import write_json
paths=sorted((ROOT/'data').glob('imu_session_*.csv'));results=[]
for path in sorted((ROOT/'configs').glob('signal_*.json')):
    config=json.loads(path.read_text());results.append({'config':path.name,'validation':scenario_validation(paths,config)})
write_json(ROOT/'outputs/signal_scenarios.json',results)
print('Saved 12 validation-only signal scenarios')
