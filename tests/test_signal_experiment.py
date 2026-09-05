import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.signal_experiment import load_feature_sessions,run_signal_project
        from healthcare_ai.paths import ROOT
        from healthcare_ai.leakage import assert_disjoint
        from healthcare_ai.splits import split
        paths=sorted((ROOT/'data').glob('imu_session_*.csv'));f=load_feature_sessions(paths);self.assertTrue(assert_disjoint(*split(f)))
        b,r=run_signal_project(paths);self.assertEqual(r['signal_protocol']['patients'],10);self.assertGreater(r['test']['n'],0)

if __name__=="__main__":unittest.main()
