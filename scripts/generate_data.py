from healthcare_ai.synthetic import generate
from healthcare_ai.paths import ROOT
generate().to_csv(ROOT/'data/demo.csv',index=False)
print('Regenerated synthetic demo records')
