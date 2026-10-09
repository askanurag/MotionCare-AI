import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.inertial_features import inertial_summary
        x=np.zeros((100,6));x[:,2]=1;r=inertial_summary(x,50);self.assertEqual(r['accel_rms'],1);self.assertEqual(r['jerk_rms'],0);self.assertEqual(r['gyro_rms'],0)

if __name__=="__main__":unittest.main()
