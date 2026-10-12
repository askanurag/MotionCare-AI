import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.signal_contracts import validate_signal
        self.assertEqual(validate_signal(self.x,50).shape,(600,6))
        with self.assertRaises(ValueError):validate_signal(self.x[:,:3],50)
        with self.assertRaises(ValueError):validate_signal(self.x,0)

if __name__=="__main__":unittest.main()
