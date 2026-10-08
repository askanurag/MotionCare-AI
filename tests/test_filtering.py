import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.filtering import lowpass
        y=lowpass(self.x,50,10);self.assertEqual(y.shape,self.x.shape);self.assertTrue(np.isfinite(y).all())
        with self.assertRaises(ValueError):lowpass(self.x,50,30)

if __name__=="__main__":unittest.main()
