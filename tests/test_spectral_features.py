import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.spectral_features import spectral_summary
        t=np.arange(500)/50;x=np.zeros((500,6));x[:,2]=1+.2*np.sin(2*np.pi*3*t)
        s=spectral_summary(x,50);self.assertAlmostEqual(s['dominant_frequency'],3,places=1)

if __name__=="__main__":unittest.main()
