import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.resampling import resample
        r=resample(self.x,50,25);self.assertEqual(r.shape,(300,6))
        with self.assertRaises(ValueError):resample(self.x,50,-5)

if __name__=="__main__":unittest.main()
