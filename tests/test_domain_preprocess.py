import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_preprocess import clean_signal
        x=np.ones(31);x[15]=20;y=clean_signal(x,cutoff=5);self.assertEqual(y[15],1)
        with self.assertRaises(ValueError):clean_signal(x,cutoff=4)

if __name__=="__main__":unittest.main()
