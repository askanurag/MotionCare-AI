from pathlib import Path
import nbformat
from nbclient import NotebookClient
from healthcare_ai.paths import ROOT
for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
    nb=nbformat.read(path,as_version=4)
    NotebookClient(nb,timeout=180,kernel_name='python3',resources={'metadata':{'path':str(ROOT)}}).execute()
    nbformat.write(nb,path)
    print(path.name)
