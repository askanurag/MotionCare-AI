import matplotlib
matplotlib.use('Agg')
from healthcare_ai.paths import ROOT
from healthcare_ai.io import load_csv
from healthcare_ai.splits import split
from healthcare_ai.pipeline import build
from healthcare_ai.settings import FEATURES,TARGET
from healthcare_ai.plots import plot_roc
train,val,test=split(load_csv(ROOT/'data/demo.csv'));model=build().fit(train[FEATURES],train[TARGET])
fig=plot_roc(test[TARGET],model.predict_proba(test[FEATURES])[:,1]);out=ROOT/'outputs';out.mkdir(exist_ok=True);fig.savefig(out/'roc.png',dpi=180,bbox_inches='tight')
print(out/'roc.png')
