import unittest, tempfile
from pathlib import Path
import numpy as np
import pandas as pd
from healthcare_ai.synthetic import generate
from healthcare_ai.settings import FEATURES,TARGET
from healthcare_ai.validation import validate
from healthcare_ai.splits import split
from healthcare_ai.leakage import assert_disjoint
from healthcare_ai.pipeline import build
from healthcare_ai.metrics import evaluate
from healthcare_ai.calibration import expected_calibration_error
from healthcare_ai.bootstrap import auc_interval
from healthcare_ai.drift import standardized_shift
from healthcare_ai.persistence import save_bundle,load_bundle
from healthcare_ai.experiment import run
from healthcare_ai.inference import predict
from healthcare_ai.quality import quality_report

class TestCase(unittest.TestCase):
    def setUp(self):
        self.train,self.val,self.test=split(generate(150))

    def test_behavior(self):
        m=build().fit(self.train[FEATURES],self.train[TARGET]); x=self.test[FEATURES].copy(); x.iloc[0,0]=np.nan; self.assertTrue(np.isfinite(m.predict_proba(x)).all())

if __name__ == "__main__": unittest.main()
