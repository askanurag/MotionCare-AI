import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.dummy_baselines import dummy_scores
        from healthcare_ai.synthetic import generate
        from healthcare_ai.splits import split
        a,b,_=split(generate(100));r=dummy_scores(a,b);self.assertEqual(r['prior']['auroc'],.5)

if __name__=="__main__":unittest.main()
