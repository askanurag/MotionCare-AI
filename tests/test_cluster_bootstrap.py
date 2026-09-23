import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.cluster_bootstrap import cluster_auc
        y=np.array([0,1]*10);p=np.array([.1,.9]*10);g=np.repeat(np.arange(10),2);r=cluster_auc(y,p,g,20);self.assertEqual(r['patients'],10);self.assertEqual(r['lower'],1);self.assertEqual(r['upper'],1)

if __name__=="__main__":unittest.main()
