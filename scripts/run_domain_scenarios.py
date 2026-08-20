import json
from healthcare_ai.paths import ROOT
from healthcare_ai.domain_scenarios import validation_scenario
from healthcare_ai.io import write_json
results=[]
for path in sorted((ROOT/'configs').glob('domain_*.json')):
    config=json.loads(path.read_text());results.append({'config':path.name,'validation':validation_scenario(config)})
write_json(ROOT/'outputs/domain_scenarios.json',results)
print('Completed 12 validation-only domain scenarios')
