import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_loader import load_recording
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'record.csv';self.record.to_csv(p,index=False);f=load_recording(p);self.assertEqual(len(f),len(self.record))

if __name__=="__main__":unittest.main()
