import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.signal_quality import signal_quality
        x=np.zeros((100,6));r=signal_quality(x,50);self.assertEqual(r['flat_channels'],6);self.assertEqual(r['clipped_fraction'],0)

if __name__=="__main__":unittest.main()
