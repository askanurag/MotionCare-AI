"""Connected domain data workflow with patient-level partitions."""
from .paths import ROOT
from .domain_cohort import cohort_from_paths
from .experiment import run
DEFAULT_WINDOW=6
DEFAULT_STRIDE=6
UNIT='hours'
def recording_paths():return sorted((ROOT/'data').glob('domain_record_*.csv'))
def load_default_cohort(window_size=DEFAULT_WINDOW,stride_size=DEFAULT_STRIDE,noise_sigma=0.):
    return cohort_from_paths(recording_paths(),window_size,stride_size,noise_sigma)
def run_domain(output=None):
    frame=load_default_cohort();bundle,report=run(frame,output=output)
    report['domain_protocol']={'description':'glucose traces and injected elevated states','window_size':DEFAULT_WINDOW,'stride_size':DEFAULT_STRIDE,'unit':UNIT,
        'patients':int(frame.patient_id.nunique()),'clinical_validation':False,'data_origin':'synthetic'}
    if output:
        from pathlib import Path
        from .io import write_json
        write_json(Path(output)/'metrics.json',report)
    return bundle,report
