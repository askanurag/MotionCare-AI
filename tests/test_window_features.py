import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.window_features import extract_window,featurize_session
        from healthcare_ai.session_io import make_session
        from healthcare_ai.settings import FEATURES,TARGET
        r=extract_window(self.x,50);self.assertEqual(list(r),FEATURES)
        f=featurize_session(make_session(),50);self.assertEqual(len(f),11);self.assertEqual(set(f[TARGET]),{0,1})

if __name__=="__main__":unittest.main()
