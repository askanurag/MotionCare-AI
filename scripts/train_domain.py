import json
from healthcare_ai.paths import ROOT
from healthcare_ai.domain_experiment import run_domain
bundle,report=run_domain(output=ROOT/'outputs/domain_demo')
print(json.dumps(report,indent=2))
