import json
from healthcare_ai.io import load_csv
from healthcare_ai.paths import ROOT
from healthcare_ai.quality import quality_report
print(json.dumps(quality_report(load_csv(ROOT/'data/demo.csv')),indent=2))
