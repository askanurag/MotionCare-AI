import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_experiment import load_default_cohort
        from healthcare_ai.splits import split
        from healthcare_ai.leakage import assert_disjoint
        from healthcare_ai.settings import FEATURES,TARGET
        f=load_default_cohort();self.assertEqual(list(f),['patient_id']+FEATURES+[TARGET]);self.assertTrue(assert_disjoint(*split(f)))

if __name__=="__main__":unittest.main()
