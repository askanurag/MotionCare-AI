from healthcare_ai.paths import ROOT
from healthcare_ai.signal_experiment import run_signal_project
import json
bundle,report=run_signal_project(sorted((ROOT/'data').glob('imu_session_*.csv')),output=ROOT/'outputs/signal_demo')
print(json.dumps(report,indent=2))
