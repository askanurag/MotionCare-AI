import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_contract import validate_recording
        self.assertGreater(validate_recording(self.record),0)
        with self.assertRaises(ValueError):validate_recording(self.record.drop(columns='patient_id'))

if __name__=="__main__":unittest.main()
