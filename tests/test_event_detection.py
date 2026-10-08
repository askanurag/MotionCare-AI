import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.event_detection import magnitude_peaks
        x=np.zeros((500,6));x[:,2]=1;x[100,0]=5;x[300,0]=5
        self.assertEqual(magnitude_peaks(x,50),[100,300])

if __name__=="__main__":unittest.main()
