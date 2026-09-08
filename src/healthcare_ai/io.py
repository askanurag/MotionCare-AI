import json
import pandas as pd
from .validation import validate
def load_csv(path, labeled=True): return validate(pd.read_csv(path), labeled)
def write_json(path, payload):
    from pathlib import Path
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, allow_nan=False))
