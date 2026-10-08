import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_simulation import make_recording
        self.assertTrue(make_recording(7).equals(make_recording(7)));self.assertFalse(make_recording(7).equals(make_recording(8)))

if __name__=="__main__":unittest.main()
