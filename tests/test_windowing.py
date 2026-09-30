import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.windowing import windows
        w=windows(self.x,50,4,2);self.assertEqual(len(w),5);self.assertEqual(w[1][0],100)
        with self.assertRaises(ValueError):windows(self.x,50,0,2)

if __name__=="__main__":unittest.main()
