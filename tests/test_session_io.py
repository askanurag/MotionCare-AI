import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.session_io import make_session,load_session
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'s.csv';make_session(7).to_csv(p,index=False);f,fs=load_session(p);self.assertAlmostEqual(fs,50);self.assertEqual(int(f.event_marker.sum()),2)

if __name__=="__main__":unittest.main()
