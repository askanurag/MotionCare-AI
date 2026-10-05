import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.augmentation import jitter,rotate_z
        np.testing.assert_array_equal(jitter(self.x,50,seed=7),jitter(self.x,50,seed=7))
        a=rotate_z(self.x,50,.4);np.testing.assert_allclose(np.linalg.norm(a[:,:3],axis=1),np.linalg.norm(self.x[:,:3],axis=1))

if __name__=="__main__":unittest.main()
