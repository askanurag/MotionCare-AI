import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.model_metadata import describe_model
        r=describe_model('synthetic test',10);self.assertFalse(r['clinical_validation']);self.assertEqual(r['patients'],10)
        with self.assertRaises(ValueError):describe_model('x',0)

if __name__=="__main__":unittest.main()
