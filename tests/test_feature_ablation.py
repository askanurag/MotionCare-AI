import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.feature_ablation import ablate
        from healthcare_ai.synthetic import generate
        from healthcare_ai.splits import split
        from healthcare_ai.settings import FEATURES
        a,b,_=split(generate(150));r=ablate(a,b);self.assertEqual({x['omitted'] for x in r},set(FEATURES))

if __name__=="__main__":unittest.main()
