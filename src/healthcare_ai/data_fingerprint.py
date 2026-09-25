"""Content hashes for ordered file manifests."""
import hashlib
from pathlib import Path
def file_digest(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(65536),b''):h.update(chunk)
    return h.hexdigest()
def manifest(paths):return [{'file':Path(p).name,'sha256':file_digest(p),'bytes':Path(p).stat().st_size} for p in sorted(map(Path,paths))]
