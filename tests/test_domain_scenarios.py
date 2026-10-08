import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_scenarios import validation_scenario
        from healthcare_ai.domain_experiment import DEFAULT_WINDOW,DEFAULT_STRIDE
        r=validation_scenario({'window_size':DEFAULT_WINDOW,'stride_size':DEFAULT_STRIDE,'noise_sigma':0});self.assertIn('auroc',r);self.assertGreater(r['n'],0)

if __name__=="__main__":unittest.main()
