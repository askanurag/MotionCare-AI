import json
from healthcare_ai.paths import ROOT
from healthcare_ai.io import load_csv,write_json
from healthcare_ai.settings import FEATURES,TARGET
from healthcare_ai.splits import split
from healthcare_ai.config import read_config
from healthcare_ai.pipeline import build
from healthcare_ai.metrics import evaluate
frame=load_csv(ROOT/'data/demo.csv'); results=[]
for path in sorted((ROOT/'configs').glob('*.json')):
    cfg=read_config(path);train,val,_=split(frame,cfg['seed'])
    m=build(cfg['model'],cfg['seed']).fit(train[FEATURES],train[TARGET])
    results.append(dict(cfg,validation=evaluate(val[TARGET],m.predict_proba(val[FEATURES])[:,1])))
write_json(ROOT/'outputs/grid_validation.json',results)
print('Wrote 30 validation-only experiments')
