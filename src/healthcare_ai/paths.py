from pathlib import Path
_candidates = [Path.cwd(), Path.cwd().parent, Path(__file__).resolve().parents[2]]
ROOT = next((p for p in _candidates if (p/'data/schema.json').is_file()), _candidates[-1])
def resolve(path):
    p = Path(path)
    return p if p.is_absolute() else ROOT / p
