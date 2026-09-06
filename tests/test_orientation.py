import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.orientation import direction_change
        x=np.zeros((100,6));x[:,2]=1;self.assertEqual(direction_change(x,50),0)
        x[-25:,:3]=[1,0,0];self.assertAlmostEqual(direction_change(x,50),np.pi/2)

if __name__=="__main__":unittest.main()
